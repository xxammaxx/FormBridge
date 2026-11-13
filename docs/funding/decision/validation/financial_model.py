"""Exact-decimal Prototype-Fund cost and financing model (Revision 4).

Scope
-----
This module models the *six-month regular phase* and the *four-month Second
Stage* of the German Prototype Fund (BMFTR "Software Sprint" guideline).
It deliberately separates:

    cost accounting      G = PK + GK
    financing            G = F + EA
    funding rate         F <= 0.95 * G
    own contribution     EA >= 0.05 * G

The model does **not** claim that the communicated 47,500 EUR maximum is a
legal entitlement.  It computes what the binding guideline plus the published
FAQ arithmetic actually yields.  The unresolved public-source ambiguity is
documented in ../financial-model.md (Q3).

Rounding contract
-----------------
* All monetary inputs and outputs are Decimal, never float.
* PK is rounded half-up to the cent.
* GK is rounded **down** to the cent, so GK never exceeds 5 % of PK.
* G is the exact sum of the cent-rounded PK and GK.
* F is rounded **down** to the cent, so F never exceeds 95 % of G.
* EA is the exact residual G - F; the financing identity therefore holds to
  the cent after rounding.
* Periodic cash-flow amounts are rounded down; the last period receives the
  residual, so the sum equals F exactly.

These rules are intentionally conservative: a one-cent rounding gain may never
turn into an over-claim against the funding ceiling.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP, getcontext
from typing import Iterable, Sequence

getcontext().prec = 28

CENT = Decimal("0.01")
ZERO = Decimal("0.00")
ONE = Decimal("1")
D95 = Decimal("0.95")
D5 = Decimal("0.05")

MAX_HOURS_REGULAR = 950
MAX_COST_REGULAR = Decimal("50000.00")
MAX_COST_SECOND = Decimal("33337.00")
MAX_COST_TEN_MONTH = MAX_COST_REGULAR + MAX_COST_SECOND  # 83,337.00

DEMINIMIS_LIMIT = Decimal("300000.00")

# Communicated (not legally binding) ceilings.  Kept separate from the
# computed values so that no document can silently present communication as
# law.
COMM_MAX_FUNDING = Decimal("47500.00")
COMM_SECOND_FUNDING = Decimal("31667.00")
COMM_TEN_MONTH_FUNDING = Decimal("79167.00")

STANDARD_RATE = Decimal("50.00")
STANDARD_OVERHEAD_RATE = Decimal("0.05")


class ModelError(ValueError):
    """Raised for inputs that are not merely non-compliant but nonsensical."""


def money(value: Decimal | str | int) -> Decimal:
    """Round half-up to the cent (normal monetary display)."""
    return Decimal(value).quantize(CENT, rounding=ROUND_HALF_UP)


def floor_money(value: Decimal | str | int) -> Decimal:
    """Round down to the cent (never over-claim)."""
    return Decimal(value).quantize(CENT, rounding=ROUND_DOWN)


@dataclass(frozen=True)
class Budget:
    """Result of one regular or Second-Stage budget calculation."""

    phase: str
    hours: int
    rate: Decimal
    overhead_rate: Decimal
    apply_overhead: bool
    rate_proof: bool
    pk: Decimal
    gk: Decimal
    g: Decimal
    f: Decimal
    ea: Decimal
    cost_cap: Decimal
    hours_cap: int
    funding_communication_cap: Decimal
    prior_deminimis: Decimal = ZERO
    f_available: Decimal = DEMINIMIS_LIMIT
    f_effective: Decimal = ZERO
    ea_effective: Decimal = ZERO
    violations: tuple[str, ...] = field(default_factory=tuple)

    @property
    def compliant(self) -> bool:
        return not self.violations

    @property
    def deminimis_reduced(self) -> bool:
        return self.f_effective < self.f

    def as_dict(self) -> dict[str, str | int | bool | list[str]]:
        return {
            "phase": self.phase,
            "hours": self.hours,
            "rate": str(self.rate),
            "overhead_rate": str(self.overhead_rate),
            "apply_overhead": self.apply_overhead,
            "rate_proof": self.rate_proof,
            "pk": str(self.pk),
            "gk": str(self.gk),
            "g": str(self.g),
            "f": str(self.f),
            "ea": str(self.ea),
            "f_effective": str(self.f_effective),
            "ea_effective": str(self.ea_effective),
            "f_available": str(self.f_available),
            "prior_deminimis": str(self.prior_deminimis),
            "cost_cap": str(self.cost_cap),
            "hours_cap": self.hours_cap,
            "funding_communication_cap": str(self.funding_communication_cap),
            "compliant": self.compliant,
            "violations": list(self.violations),
        }


def _validate_inputs(
    hours: int,
    rate: Decimal,
    overhead_rate: Decimal,
    rate_proof: bool,
    phase: str,
    cost_cap: Decimal,
    hours_cap: int,
    prior_deminimis: Decimal,
) -> list[str]:
    violations: list[str] = []

    if isinstance(hours, bool) or not isinstance(hours, int):
        raise ModelError("hours must be an integer")
    if hours < 0:
        raise ModelError("hours must not be negative")
    if hours == 0:
        violations.append("zero_hours")

    if rate <= 0:
        raise ModelError("rate must be positive")
    if overhead_rate < 0:
        raise ModelError("overhead_rate must not be negative")
    if prior_deminimis < 0:
        raise ModelError("prior_deminimis must not be negative")
    if cost_cap <= 0 or hours_cap <= 0:
        raise ModelError("caps must be positive")
    if phase not in {"regular", "second"}:
        raise ModelError("phase must be 'regular' or 'second'")

    if hours > hours_cap:
        violations.append("hours_cap_exceeded")
    if rate > STANDARD_RATE:
        if phase == "second":
            violations.append("second_stage_rate_cap_exceeded")
        elif not rate_proof:
            violations.append("rate_above_50_without_invoice_proof")
    if overhead_rate > STANDARD_OVERHEAD_RATE:
        violations.append("overhead_above_5_percent_of_personnel")
    return violations


def compute_budget(
    hours: int,
    rate: Decimal | str | int = STANDARD_RATE,
    overhead_rate: Decimal | str | int = STANDARD_OVERHEAD_RATE,
    *,
    apply_overhead: bool = True,
    rate_proof: bool = False,
    prior_deminimis: Decimal | str | int = ZERO,
    phase: str = "regular",
    cost_cap: Decimal | str | int | None = None,
    hours_cap: int | None = None,
    funding_communication_cap: Decimal | str | int | None = None,
) -> Budget:
    """Compute one budget and all identity checks.

    A non-compliant result is returned (not raised) when the input is
    numerically meaningful but violates a cap; this lets tests inspect the
    exact violation instead of just catching an exception.
    """

    rate_d = Decimal(rate)
    overhead_d = Decimal(overhead_rate) if apply_overhead else ZERO
    prior_d = Decimal(prior_deminimis)

    if phase == "regular":
        cost_cap_d = Decimal(cost_cap) if cost_cap is not None else MAX_COST_REGULAR
        hours_cap_i = int(hours_cap) if hours_cap is not None else MAX_HOURS_REGULAR
        comm_cap = (
            Decimal(funding_communication_cap)
            if funding_communication_cap is not None
            else COMM_MAX_FUNDING
        )
    else:
        cost_cap_d = Decimal(cost_cap) if cost_cap is not None else MAX_COST_SECOND
        hours_cap_i = int(hours_cap) if hours_cap is not None else MAX_HOURS_REGULAR
        comm_cap = (
            Decimal(funding_communication_cap)
            if funding_communication_cap is not None
            else COMM_SECOND_FUNDING
        )

    violations = _validate_inputs(
        hours=hours,
        rate=rate_d,
        overhead_rate=overhead_d,
        rate_proof=rate_proof,
        phase=phase,
        cost_cap=cost_cap_d,
        hours_cap=hours_cap_i,
        prior_deminimis=prior_d,
    )

    pk = money(Decimal(hours) * rate_d)
    gk = floor_money(pk * overhead_d)
    g = pk + gk

    if g > cost_cap_d:
        violations.append("total_cost_cap_exceeded")

    f = floor_money(g * D95)
    ea = g - f

    if f > comm_cap:
        violations.append("communicated_funding_cap_exceeded")

    # De-minimis is a ceiling on the aid, not on eligible costs.  If the
    # remaining allowance is lower than the computed funding, the grant is
    # reduced and the own contribution rises; the financing identity remains.
    f_available = DEMINIMIS_LIMIT - prior_d
    if f_available < 0:
        f_available = ZERO
    f_effective = min(f, f_available)
    ea_effective = g - f_effective

    if prior_d >= DEMINIMIS_LIMIT:
        violations.append("deminimis_exhausted")
    if prior_d + f_effective > DEMINIMIS_LIMIT:
        violations.append("deminimis_limit_exceeded")

    # Identity checks after rounding.  These are asserted here so that a
    # future model change cannot silently break them.
    if g != pk + gk:
        violations.append("K1_cost_identity_failed")
    if g != f_effective + ea_effective:
        violations.append("K2_financing_identity_failed")
    if f_effective > (g * D95):
        violations.append("K3_funding_rate_exceeded")
    if ea_effective < (g * D5):
        violations.append("K4_own_contribution_too_low")
    if gk > (pk * D5).quantize(CENT, rounding=ROUND_HALF_UP):
        violations.append("K7_overhead_base_exceeded")
    for label, value in (("PK", pk), ("GK", gk), ("G", g), ("F", f_effective), ("EA", ea_effective)):
        if value != value.quantize(CENT, rounding=ROUND_HALF_UP):
            violations.append(f"K8_{label}_not_cent_exact")

    return Budget(
        phase=phase,
        hours=hours,
        rate=rate_d,
        overhead_rate=overhead_d,
        apply_overhead=apply_overhead,
        rate_proof=rate_proof,
        pk=pk,
        gk=gk,
        g=g,
        f=f,
        ea=ea,
        cost_cap=cost_cap_d,
        hours_cap=hours_cap_i,
        funding_communication_cap=comm_cap,
        prior_deminimis=prior_d,
        f_available=f_available,
        f_effective=f_effective,
        ea_effective=ea_effective,
        violations=tuple(dict.fromkeys(violations)),
    )


def second_stage_budget(
    hours: int,
    regular_hours: int = MAX_HOURS_REGULAR,
    rate: Decimal | str | int = STANDARD_RATE,
    overhead_rate: Decimal | str | int = STANDARD_OVERHEAD_RATE,
    *,
    apply_overhead: bool = True,
    prior_deminimis: Decimal | str | int = ZERO,
) -> Budget:
    """Second Stage: four months, 50 EUR/h cap, max. 33,337 EUR costs."""

    if isinstance(regular_hours, bool) or not isinstance(regular_hours, int):
        raise ModelError("regular_hours must be an integer")
    if regular_hours < 0:
        raise ModelError("regular_hours must not be negative")
    if hours > regular_hours:
        # Let the generic cap check record it, but the cap is the regular
        # phase hour count, not 950 by default.
        pass
    return compute_budget(
        hours=hours,
        rate=rate,
        overhead_rate=overhead_rate,
        apply_overhead=apply_overhead,
        rate_proof=False,
        prior_deminimis=prior_deminimis,
        phase="second",
        cost_cap=MAX_COST_SECOND,
        hours_cap=regular_hours,
        funding_communication_cap=COMM_SECOND_FUNDING,
    )


def combined_ten_month_budget(
    regular: Budget,
    second: Budget,
) -> dict[str, Decimal | bool | list[str]]:
    """Combine a regular and a Second-Stage budget into the legal 10-month frame.

    Guideline No. 5 caps the second phase at 33,337 EUR costs, so the total
    cost ceiling is 83,337 EUR.  The funding ceiling is 95 % of that total.
    """

    if regular.phase != "regular" or second.phase != "second":
        raise ModelError("combined_ten_month_budget needs one regular and one second-phase budget")
    total_g = regular.g + second.g
    total_f = regular.f_effective + second.f_effective
    total_ea = total_g - total_f
    violations: list[str] = []
    if total_g > MAX_COST_TEN_MONTH:
        violations.append("ten_month_total_cost_cap_exceeded")
    if total_f > floor_money(MAX_COST_TEN_MONTH * D95):
        violations.append("ten_month_funding_cap_exceeded")
    if total_g != total_f + total_ea:
        violations.append("ten_month_financing_identity_failed")
    return {
        "total_g": total_g,
        "total_f": total_f,
        "total_ea": total_ea,
        "total_hours": regular.hours + second.hours,
        "cost_cap": MAX_COST_TEN_MONTH,
        "max_strict_funding": floor_money(MAX_COST_TEN_MONTH * D95),
        "communicated_funding": COMM_TEN_MONTH_FUNDING,
        "compliant": not violations and regular.compliant and second.compliant,
        "violations": violations,
    }


def rate_threshold_for_cost_cap(
    hours: int = MAX_HOURS_REGULAR,
    overhead_rate: Decimal | str | int = STANDARD_OVERHEAD_RATE,
    cost_cap: Decimal | str | int = MAX_COST_REGULAR,
) -> Decimal:
    """Highest hourly rate at which 1.05 * hours * rate still fits the cost cap.

    Exact, unrounded threshold.  For 950 h and 50,000 EUR this is
    50,000 / (950 * 1.05) = 50.1253132832... EUR/h.
    """

    if hours <= 0:
        raise ModelError("hours must be positive")
    overhead_d = Decimal(overhead_rate)
    if overhead_d < 0:
        raise ModelError("overhead_rate must not be negative")
    return Decimal(cost_cap) / (Decimal(hours) * (ONE + overhead_d))


def quarterly_schedule(
    funding: Decimal | str | int,
    weights: Sequence[int] = (1, 3, 2),
) -> list[Decimal]:
    """Split funding into quarter calls, rounding down and assigning residual last.

    Default weights are the months June (1), July-September (3), October-
    November (2) of the six-month regular phase.  The sum is exactly the
    input funding to the cent.
    """

    f = Decimal(funding).quantize(CENT, rounding=ROUND_HALF_UP)
    if not weights or any(w < 0 for w in weights):
        raise ModelError("weights must be a non-empty non-negative sequence")
    total_weight = sum(weights)
    if total_weight <= 0:
        raise ModelError("weights must sum to a positive value")

    parts: list[Decimal] = []
    allocated = ZERO
    for weight in weights[:-1]:
        part = floor_money(f * Decimal(weight) / Decimal(total_weight))
        parts.append(part)
        allocated += part
    parts.append(f - allocated)
    if any(p < 0 for p in parts):
        raise ModelError("funding too small for the requested schedule")
    if sum(parts) != f:
        raise ModelError("schedule does not preserve the funding total")
    return parts


def combined_deminimis_check(
    prior_deminimis: Decimal | str | int,
    budgets: Sequence[Budget],
) -> dict[str, Decimal | bool]:
    """Check the rolling three-year de-minimis ceiling across several phases."""

    prior = Decimal(prior_deminimis)
    if prior < 0:
        raise ModelError("prior_deminimis must not be negative")
    total_aid = sum((b.f_effective for b in budgets), ZERO)
    available = max(ZERO, DEMINIMIS_LIMIT - prior)
    return {
        "prior": prior,
        "total_aid": total_aid,
        "available": available,
        "remaining_after": DEMINIMIS_LIMIT - prior - total_aid,
        "compliant": prior + total_aid <= DEMINIMIS_LIMIT,
    }


def cash_flow(budget: Budget) -> dict[str, Decimal]:
    """Conservative cash-flow figures for a six-month regular budget."""

    if budget.phase != "regular":
        raise ModelError("cash_flow is defined for the regular phase")
    parts = quarterly_schedule(budget.f_effective)
    # Costs are spread evenly over six months; the first call covers June
    # only, the second covers July-September, the third October-November.
    monthly_cost = money(budget.g / Decimal(6))
    quarter_cost = money(budget.g / Decimal(2))
    monthly_ea = floor_money(budget.ea_effective / Decimal(6))
    return {
        "first_call": parts[0],
        "second_call": parts[1],
        "third_call": parts[2],
        "total_funding": sum(parts),
        "monthly_cost": monthly_cost,
        "quarter_cost": quarter_cost,
        "monthly_own_contribution": monthly_ea,
        "peak_external_prefinancing": parts[1],
        "peak_total_cash_need": quarter_cost,
    }


def scenario_rows() -> Iterable[dict[str, str]]:
    """The documented scenarios A-I, for the archived report."""

    a = compute_budget(950, apply_overhead=False)
    b = compute_budget(950)
    c = compute_budget(950, rate=rate_threshold_for_cost_cap(), rate_proof=True)
    d = [compute_budget(h) for h in (700, 800, 850, 950)]
    e = compute_budget(950, overhead_rate=(Decimal("2500") / Decimal("47500")))
    f = compute_budget(200)
    g633 = second_stage_budget(633)
    g634 = second_stage_budget(634)
    h = compute_budget(950, prior_deminimis="260000.00")
    i = combined_ten_month_budget(b, g634)

    rows: list[dict[str, str]] = []

    def add(name: str, budget: Budget) -> None:
        rows.append(
            {
                "scenario": name,
                "hours": str(budget.hours),
                "rate": str(budget.rate),
                "pk": str(budget.pk),
                "gk": str(budget.gk),
                "g": str(budget.g),
                "f": str(budget.f_effective),
                "ea": str(budget.ea_effective),
                "violations": ", ".join(budget.violations) or "none",
            }
        )

    add("A 950 h, no overhead", a)
    add("B 950 h, 5 % overhead (baseline)", b)
    add("C 950 h, exact rate threshold (proof)", c)
    for row in d:
        add(f"D {row.hours} h, 5 % overhead", row)
    add("E FAQ logic (5.263 % overhead on PK)", e)
    add("F 200 h part-time", f)
    add("G1 Second Stage 633 h", g633)
    add("G2 Second Stage 634 h", g634)
    rows.append(
        {
            "scenario": "H de-minimis prior 260,000",
            "hours": "950",
            "rate": "50.00",
            "pk": str(h.pk),
            "gk": str(h.gk),
            "g": str(h.g),
            "f": str(h.f_effective),
            "ea": str(h.ea_effective),
            "violations": ", ".join(h.violations) or "none",
        }
    )
    rows.append(
        {
            "scenario": "I 10-month (950 h + 634 h)",
            "hours": str(i["total_hours"]),
            "rate": "50.00",
            "pk": "-",
            "gk": "-",
            "g": str(i["total_g"]),
            "f": str(i["total_f"]),
            "ea": str(i["total_ea"]),
            "violations": ", ".join(i["violations"]) or "none",  # type: ignore[arg-type]
        }
    )
    return rows


if __name__ == "__main__":  # pragma: no cover - manual report helper
    print("| Szenario | Stunden | Satz | PK | GK | G | F | EA | Verstöße |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|---|")
    for row in scenario_rows():
        print(
            "| {scenario} | {hours} | {rate} | {pk} | {gk} | {g} | {f} | {ea} | {violations} |".format(
                **row
            )
        )
