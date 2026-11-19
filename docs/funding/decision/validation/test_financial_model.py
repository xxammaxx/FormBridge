"""Reproducible regression suite for the exact-decimal funding model.

Run from the repository root:

    python3 -m unittest discover -s docs/funding/decision/validation -p 'test_*.py' -v

Every expected monetary value is written as a literal.  The suite therefore
does not merely re-run the implementation against itself: changing a model
formula without changing the documented expectation fails the test.
"""

from __future__ import annotations

import unittest
from decimal import Decimal

from financial_model import (
    COMM_MAX_FUNDING,
    COMM_SECOND_FUNDING,
    COMM_TEN_MONTH_FUNDING,
    DEMINIMIS_LIMIT,
    MAX_COST_REGULAR,
    MAX_COST_SECOND,
    MAX_COST_TEN_MONTH,
    ModelError,
    cash_flow,
    combined_deminimis_check,
    combined_ten_month_budget,
    compute_budget,
    floor_money,
    money,
    quarterly_schedule,
    rate_threshold_for_cost_cap,
    second_stage_budget,
)

D = Decimal


class TestBaseline(unittest.TestCase):
    """The conservative 950-hour baseline, cent by cent."""

    def setUp(self) -> None:
        self.b = compute_budget(950)

    def test_personnel_costs(self) -> None:
        self.assertEqual(self.b.pk, D("47500.00"))

    def test_overhead_is_five_percent_of_personnel(self) -> None:
        self.assertEqual(self.b.gk, D("2375.00"))

    def test_total_eligible_costs(self) -> None:
        self.assertEqual(self.b.g, D("49875.00"))

    def test_strict_funding(self) -> None:
        self.assertEqual(self.b.f, D("47381.25"))

    def test_own_contribution(self) -> None:
        self.assertEqual(self.b.ea, D("2493.75"))

    def test_funding_rate_is_exactly_95_percent(self) -> None:
        self.assertEqual(self.b.f, self.b.g * D("0.95"))

    def test_cost_identity(self) -> None:
        self.assertEqual(self.b.g, self.b.pk + self.b.gk)

    def test_financing_identity(self) -> None:
        self.assertEqual(self.b.g, self.b.f + self.b.ea)

    def test_own_contribution_is_exactly_five_percent(self) -> None:
        self.assertEqual(self.b.ea, self.b.g * D("0.05"))

    def test_baseline_is_compliant(self) -> None:
        self.assertTrue(self.b.compliant, self.b.violations)

    def test_gap_to_communicated_funding(self) -> None:
        self.assertEqual(COMM_MAX_FUNDING - self.b.f, D("118.75"))

    def test_gap_to_communicated_own_contribution(self) -> None:
        self.assertEqual(D("2500.00") - self.b.ea, D("6.25"))

    def test_cost_headroom_to_50000(self) -> None:
        self.assertEqual(MAX_COST_REGULAR - self.b.g, D("125.00"))

    def test_no_overhead_scenario(self) -> None:
        a = compute_budget(950, apply_overhead=False)
        self.assertEqual(a.pk, D("47500.00"))
        self.assertEqual(a.gk, D("0.00"))
        self.assertEqual(a.g, D("47500.00"))
        self.assertEqual(a.f, D("45125.00"))
        self.assertEqual(a.ea, D("2375.00"))

    def test_overhead_effect_on_funding(self) -> None:
        a = compute_budget(950, apply_overhead=False)
        self.assertEqual(self.b.f - a.f, D("2256.25"))


class TestScenarios(unittest.TestCase):
    """Documented scenarios D, F, C and the communication frame E."""

    def test_700_hours(self) -> None:
        b = compute_budget(700)
        self.assertEqual((b.pk, b.gk, b.g, b.f, b.ea), (
            D("35000.00"), D("1750.00"), D("36750.00"), D("34912.50"), D("1837.50")
        ))

    def test_800_hours(self) -> None:
        b = compute_budget(800)
        self.assertEqual((b.pk, b.gk, b.g, b.f, b.ea), (
            D("40000.00"), D("2000.00"), D("42000.00"), D("39900.00"), D("2100.00")
        ))

    def test_850_hours(self) -> None:
        b = compute_budget(850)
        self.assertEqual((b.pk, b.gk, b.g, b.f, b.ea), (
            D("42500.00"), D("2125.00"), D("44625.00"), D("42393.75"), D("2231.25")
        ))

    def test_950_hours(self) -> None:
        b = compute_budget(950)
        self.assertEqual((b.pk, b.gk, b.g, b.f, b.ea), (
            D("47500.00"), D("2375.00"), D("49875.00"), D("47381.25"), D("2493.75")
        ))

    def test_part_time_200_hours(self) -> None:
        b = compute_budget(200)
        self.assertEqual((b.pk, b.gk, b.g, b.f, b.ea), (
            D("10000.00"), D("500.00"), D("10500.00"), D("9975.00"), D("525.00")
        ))

    def test_rate_lever_50_12(self) -> None:
        b = compute_budget(950, rate="50.12", rate_proof=True)
        self.assertEqual(b.pk, D("47614.00"))
        self.assertEqual(b.gk, D("2380.70"))
        self.assertEqual(b.g, D("49994.70"))
        self.assertEqual(b.f, D("47494.96"))
        self.assertEqual(b.ea, D("2499.74"))
        self.assertTrue(b.compliant, b.violations)

    def test_rate_lever_50_1253(self) -> None:
        b = compute_budget(950, rate="50.1253", rate_proof=True)
        self.assertEqual(b.g, D("49999.99"))
        self.assertEqual(b.f, D("47499.99"))
        self.assertEqual(b.ea, D("2500.00"))
        self.assertTrue(b.compliant, b.violations)

    def test_rate_lever_exact_threshold(self) -> None:
        threshold = rate_threshold_for_cost_cap()
        self.assertEqual(threshold.quantize(D("0.000001")), D("50.125313"))
        b = compute_budget(950, rate=threshold, rate_proof=True)
        self.assertEqual(b.g, D("50000.00"))
        self.assertEqual(b.f, D("47500.00"))
        self.assertEqual(b.ea, D("2500.00"))
        self.assertTrue(b.compliant, b.violations)

    def test_rate_lever_above_threshold_fails(self) -> None:
        b = compute_budget(950, rate="50.13", rate_proof=True)
        self.assertEqual(b.g, D("50004.67"))
        self.assertIn("total_cost_cap_exceeded", b.violations)
        self.assertFalse(b.compliant)

    def test_faq_frame_e_exact_funding(self) -> None:
        # 2,500 EUR overhead is 5 % of the 50,000 EUR total, not 5 % of PK.
        e = compute_budget(950, overhead_rate=(D("2500") / D("47500")))
        self.assertEqual(e.pk, D("47500.00"))
        self.assertEqual(e.gk, D("2500.00"))
        self.assertEqual(e.g, D("50000.00"))
        self.assertEqual(e.f, D("47500.00"))
        self.assertEqual(e.ea, D("2500.00"))

    def test_faq_frame_e_violates_overhead_rule(self) -> None:
        e = compute_budget(950, overhead_rate=(D("2500") / D("47500")))
        self.assertIn("overhead_above_5_percent_of_personnel", e.violations)
        self.assertIn("K7_overhead_base_exceeded", e.violations)
        self.assertFalse(e.compliant)

    def test_alternative_1000_hours_without_overhead(self) -> None:
        # 950 funded + 50 own hours at 50 EUR/h and no overhead is the only
        # *zero-overhead* construction of 47,500 EUR funding; it exceeds the
        # handbook's 950-hour total only if that cap is read as total hours.
        b = compute_budget(1000, apply_overhead=False, hours_cap=1000)
        self.assertEqual(b.g, D("50000.00"))
        self.assertEqual(b.f, D("47500.00"))
        self.assertEqual(b.ea, D("2500.00"))

    def test_alternative_1000_hours_violates_950_cap(self) -> None:
        b = compute_budget(1000, apply_overhead=False)
        self.assertIn("hours_cap_exceeded", b.violations)


class TestCapsAndBoundaries(unittest.TestCase):
    """Hour, cost, rate and overhead boundaries."""

    def test_950_hours_allowed(self) -> None:
        self.assertTrue(compute_budget(950).compliant)

    def test_951_hours_rejected(self) -> None:
        b = compute_budget(951)
        self.assertIn("hours_cap_exceeded", b.violations)

    def test_zero_hours_flagged(self) -> None:
        b = compute_budget(0)
        self.assertIn("zero_hours", b.violations)

    def test_negative_hours_raise(self) -> None:
        with self.assertRaises(ModelError):
            compute_budget(-1)

    def test_non_integer_hours_raise(self) -> None:
        with self.assertRaises(ModelError):
            compute_budget(950.5)  # type: ignore[arg-type]

    def test_bool_hours_raise(self) -> None:
        with self.assertRaises(ModelError):
            compute_budget(True)  # type: ignore[arg-type]

    def test_zero_rate_raises(self) -> None:
        with self.assertRaises(ModelError):
            compute_budget(950, rate=0)

    def test_negative_rate_raises(self) -> None:
        with self.assertRaises(ModelError):
            compute_budget(950, rate="-1")

    def test_rate_above_50_without_proof_rejected(self) -> None:
        b = compute_budget(950, rate="50.10", rate_proof=False)
        self.assertIn("rate_above_50_without_invoice_proof", b.violations)

    def test_rate_above_50_with_proof_allowed(self) -> None:
        b = compute_budget(950, rate="50.10", rate_proof=True)
        self.assertNotIn("rate_above_50_without_invoice_proof", b.violations)

    def test_overhead_above_5_percent_rejected(self) -> None:
        b = compute_budget(950, overhead_rate="0.0501")
        self.assertIn("overhead_above_5_percent_of_personnel", b.violations)

    def test_negative_overhead_raises(self) -> None:
        with self.assertRaises(ModelError):
            compute_budget(950, overhead_rate="-0.01")

    def test_cost_cap_exactly_50000_allowed(self) -> None:
        b = compute_budget(950, rate=rate_threshold_for_cost_cap(), rate_proof=True)
        self.assertEqual(b.g, D("50000.00"))
        self.assertTrue(b.compliant, b.violations)

    def test_cost_cap_50000_01_rejected(self) -> None:
        # Exact rate that produces G = 50,000.01 after cent rounding.
        rate = D("50000.01") / (D("950") * D("1.05"))
        b = compute_budget(950, rate=rate, rate_proof=True)
        self.assertEqual(b.g, D("50000.01"))
        self.assertIn("total_cost_cap_exceeded", b.violations)

    def test_no_overhead_zero_gk(self) -> None:
        b = compute_budget(950, apply_overhead=False)
        self.assertEqual(b.gk, D("0.00"))

    def test_prior_deminimis_negative_raises(self) -> None:
        with self.assertRaises(ModelError):
            compute_budget(950, prior_deminimis="-1")

    def test_invalid_phase_raises(self) -> None:
        with self.assertRaises(ModelError):
            compute_budget(950, phase="third")


class TestRounding(unittest.TestCase):
    """Cent rounding and the no-over-claim contract."""

    def test_money_half_up(self) -> None:
        self.assertEqual(money("2.345"), D("2.35"))
        self.assertEqual(money("2.344"), D("2.34"))

    def test_floor_money(self) -> None:
        self.assertEqual(floor_money("2.349"), D("2.34"))
        self.assertEqual(floor_money("2.999"), D("2.99"))

    def test_funding_is_floored_not_half_up(self) -> None:
        # 95 % of 36,750.01 is 34,912.5095.  Half-up would be 34,912.51,
        # which is above 95 %.  The model must output 34,912.50.
        g = D("36750.01")
        f = floor_money(g * D("0.95"))
        self.assertEqual(f, D("34912.50"))
        self.assertLessEqual(f, g * D("0.95"))

    def test_funding_floor_preserves_identity(self) -> None:
        b = compute_budget(700)
        self.assertEqual(b.g, b.f + b.ea)
        self.assertLessEqual(b.f, b.g * D("0.95"))

    def test_quarterly_schedule_baseline(self) -> None:
        parts = quarterly_schedule(D("47381.25"))
        self.assertEqual(parts, [D("7896.87"), D("23690.62"), D("15793.76")])
        self.assertEqual(sum(parts), D("47381.25"))

    def test_quarterly_schedule_small_amount(self) -> None:
        parts = quarterly_schedule(D("1.00"))
        self.assertEqual(parts, [D("0.16"), D("0.50"), D("0.34")])
        self.assertEqual(sum(parts), D("1.00"))

    def test_quarterly_schedule_one_cent(self) -> None:
        parts = quarterly_schedule(D("0.01"))
        self.assertEqual(parts, [D("0.00"), D("0.00"), D("0.01")])
        self.assertEqual(sum(parts), D("0.01"))

    def test_quarterly_schedule_preserves_total_for_many_values(self) -> None:
        for cents in range(1, 100):
            f = D(cents) / D(100)
            self.assertEqual(sum(quarterly_schedule(f)), f)

    def test_every_value_is_cent_exact(self) -> None:
        b = compute_budget(950, rate="50.1253", rate_proof=True)
        for value in (b.pk, b.gk, b.g, b.f, b.ea):
            self.assertEqual(value, value.quantize(D("0.01")))

    def test_gk_never_exceeds_five_percent(self) -> None:
        for hours in (1, 7, 199, 333, 634, 950):
            b = compute_budget(hours)
            self.assertLessEqual(b.gk, b.pk * D("0.05"))

    def test_gk_floor_not_half_up(self) -> None:
        # 47,619.05 * 5 % = 2,380.9525; floor is 2,380.95, half-up would be
        # 2,380.95 as well here, so use a value with an exact half-cent.
        b = compute_budget(1, rate="0.10")  # PK 0.10, 5 % = 0.005
        self.assertEqual(b.gk, D("0.00"))


class TestSecondStage(unittest.TestCase):
    """Four-month Second Stage arithmetic."""

    def test_633_hours(self) -> None:
        b = second_stage_budget(633)
        self.assertEqual((b.pk, b.gk, b.g, b.f, b.ea), (
            D("31650.00"), D("1582.50"), D("33232.50"), D("31570.87"), D("1661.63")
        ))
        self.assertTrue(b.compliant, b.violations)

    def test_634_hours(self) -> None:
        b = second_stage_budget(634)
        self.assertEqual((b.pk, b.gk, b.g, b.f, b.ea), (
            D("31700.00"), D("1585.00"), D("33285.00"), D("31620.75"), D("1664.25")
        ))
        self.assertTrue(b.compliant, b.violations)

    def test_635_hours_exceeds_cost_cap(self) -> None:
        b = second_stage_budget(635)
        self.assertEqual(b.g, D("33337.50"))
        self.assertIn("total_cost_cap_exceeded", b.violations)
        self.assertFalse(b.compliant)

    def test_exact_cost_cap_funding_ceiling(self) -> None:
        self.assertEqual(floor_money(MAX_COST_SECOND * D("0.95")), D("31670.15"))

    def test_633_hours_does_not_reach_communicated_31667(self) -> None:
        b = second_stage_budget(633)
        self.assertEqual(COMM_SECOND_FUNDING - b.f, D("96.13"))

    def test_634_hours_does_not_reach_communicated_31667(self) -> None:
        b = second_stage_budget(634)
        self.assertEqual(COMM_SECOND_FUNDING - b.f, D("46.25"))

    def test_second_stage_rate_cap_is_50(self) -> None:
        b = second_stage_budget(633, rate="50.01", apply_overhead=True)
        self.assertIn("second_stage_rate_cap_exceeded", b.violations)

    def test_second_stage_hours_cap_is_regular_hours(self) -> None:
        b = second_stage_budget(951, regular_hours=950)
        self.assertIn("hours_cap_exceeded", b.violations)

    def test_second_stage_no_overhead(self) -> None:
        b = second_stage_budget(633, apply_overhead=False)
        self.assertEqual(b.g, D("31650.00"))
        self.assertEqual(b.f, D("30067.50"))
        self.assertEqual(b.ea, D("1582.50"))

    def test_second_stage_633_funding_rate(self) -> None:
        b = second_stage_budget(633)
        self.assertEqual(b.f, D("31570.87"))
        self.assertLessEqual(b.f, b.g * D("0.95"))

    def test_old_31650_funding_claim_is_invalid(self) -> None:
        # Claiming 31,650 EUR funding on 33,232.50 EUR costs would be 95.24 %.
        g = D("33232.50")
        self.assertGreater(D("31650.00") / g, D("0.95"))
        self.assertEqual((D("31650.00") / g * D("100")).quantize(D("0.001")), D("95.238"))


class TestCashFlow(unittest.TestCase):
    """Quarterly calls and pre-financing."""

    def setUp(self) -> None:
        self.b = compute_budget(950)
        self.cf = cash_flow(self.b)

    def test_first_call(self) -> None:
        self.assertEqual(self.cf["first_call"], D("7896.87"))

    def test_second_call(self) -> None:
        self.assertEqual(self.cf["second_call"], D("23690.62"))

    def test_third_call(self) -> None:
        self.assertEqual(self.cf["third_call"], D("15793.76"))

    def test_calls_sum_to_funding(self) -> None:
        self.assertEqual(
            self.cf["first_call"] + self.cf["second_call"] + self.cf["third_call"],
            self.b.f,
        )

    def test_monthly_cost(self) -> None:
        self.assertEqual(self.cf["monthly_cost"], D("8312.50"))

    def test_quarter_cost(self) -> None:
        self.assertEqual(self.cf["quarter_cost"], D("24937.50"))

    def test_peak_external_prefinancing(self) -> None:
        self.assertEqual(self.cf["peak_external_prefinancing"], D("23690.63"))

    def test_cumulative_peak_total_cash_need(self) -> None:
        self.assertEqual(self.cf["cumulative_peak_cash_need"], D("25353.13"))

    def test_cumulative_peak_own_contribution(self) -> None:
        self.assertEqual(self.cf["cumulative_peak_own"], D("1662.50"))

    def test_cumulative_peak_external(self) -> None:
        self.assertEqual(self.cf["cumulative_peak_external"], D("23690.63"))

    def test_peak_total_cash_need(self) -> None:
        self.assertEqual(self.cf["peak_total_cash_need"], D("25353.13"))

    def test_quarter_cost_is_not_cumulative_peak(self) -> None:
        self.assertEqual(self.cf["quarter_cost"], D("24937.50"))
        self.assertEqual(
            self.cf["cumulative_peak_cash_need"] - self.cf["quarter_cost"],
            D("415.63"),
        )

    def test_first_month_gap(self) -> None:
        gap = self.cf["monthly_cost"] - self.cf["first_call"]
        self.assertEqual(gap, D("415.63"))

    def test_monthly_own_contribution_is_floor(self) -> None:
        self.assertEqual(self.cf["monthly_own_contribution"], D("415.62"))


class TestDeminimis(unittest.TestCase):
    """Rolling three-year de-minimis ceiling, not a calendar-year rule."""

    def test_no_prior_aid(self) -> None:
        b = compute_budget(950, prior_deminimis="0")
        self.assertEqual(b.f_effective, D("47381.25"))
        self.assertFalse(b.deminimis_reduced)

    def test_prior_aid_reduces_funding(self) -> None:
        b = compute_budget(950, prior_deminimis="260000.00")
        self.assertEqual(b.f_available, D("40000.00"))
        self.assertEqual(b.f_effective, D("40000.00"))
        self.assertEqual(b.ea_effective, D("9875.00"))
        self.assertEqual(b.g, b.f_effective + b.ea_effective)
        self.assertTrue(b.compliant, b.violations)

    def test_prior_aid_leaves_only_100_euro(self) -> None:
        b = compute_budget(950, prior_deminimis="299900.00")
        self.assertEqual(b.f_effective, D("100.00"))
        self.assertEqual(b.ea_effective, D("49775.00"))
        self.assertTrue(b.compliant, b.violations)

    def test_exhausted_allowance_blocks_funding(self) -> None:
        b = compute_budget(950, prior_deminimis="300000.00")
        self.assertEqual(b.f_effective, D("0.00"))
        self.assertIn("deminimis_exhausted", b.violations)
        self.assertFalse(b.compliant)

    def test_prior_aid_above_limit_blocks_funding(self) -> None:
        b = compute_budget(950, prior_deminimis="310000.00")
        self.assertEqual(b.f_effective, D("0.00"))
        self.assertIn("deminimis_exhausted", b.violations)

    def test_combined_regular_and_second_stage_below_limit(self) -> None:
        regular = compute_budget(950)
        second = second_stage_budget(634)
        check = combined_deminimis_check("220000.00", [regular, second])
        self.assertTrue(check["compliant"])
        self.assertEqual(check["total_aid"], D("79002.00"))

    def test_combined_regular_and_second_stage_above_limit(self) -> None:
        regular = compute_budget(950)
        second = second_stage_budget(634)
        check = combined_deminimis_check("250000.00", [regular, second])
        self.assertFalse(check["compliant"])
        self.assertEqual(check["remaining_after"], D("-29002.00"))

    def test_limit_constant(self) -> None:
        self.assertEqual(DEMINIMIS_LIMIT, D("300000.00"))


class TestInvalidModels(unittest.TestCase):
    """Negative tests against previously published or plausible wrong models."""

    def test_old_model_a_breaks_financing_identity(self) -> None:
        # F = 47,500 on G = 47,500 with EA = 2,500 double-counts the own
        # contribution: 47,500 + 2,500 != 47,500.
        g, f, ea = D("47500.00"), D("47500.00"), D("2500.00")
        self.assertNotEqual(g, f + ea)
        self.assertEqual(f / g, D("1"))

    def test_old_model_a_breaks_95_percent(self) -> None:
        g, f = D("47500.00"), D("47500.00")
        self.assertGreater(f, g * D("0.95"))

    def test_overhead_on_total_instead_of_personnel_breaks_rule(self) -> None:
        pk, gk, g = D("47500.00"), D("2500.00"), D("50000.00")
        self.assertEqual(g, pk + gk)
        self.assertGreater(gk / pk, D("0.05"))
        self.assertEqual((gk / pk * D("100")).quantize(D("0.001")), D("5.263"))

    def test_funding_above_95_percent_is_invalid(self) -> None:
        g, f = D("49875.00"), D("47500.00")
        self.assertGreater(f / g, D("0.95"))

    def test_own_contribution_below_5_percent_is_invalid(self) -> None:
        g, ea = D("49875.00"), D("2493.74")
        self.assertLess(ea / g, D("0.05"))

    def test_old_second_stage_funding_claim_breaks_95_percent(self) -> None:
        g, f = D("33232.50"), D("31650.00")
        self.assertGreater(f / g, D("0.95"))

    def test_47500_as_personnel_cost_is_not_47500_funding(self) -> None:
        b = compute_budget(950, apply_overhead=False)
        self.assertEqual(b.pk, D("47500.00"))
        self.assertEqual(b.f, D("45125.00"))
        self.assertNotEqual(b.f, D("47500.00"))

    def test_half_up_funding_can_exceed_95_percent(self) -> None:
        g = D("36750.01")
        half_up = (g * D("0.95")).quantize(D("0.01"))
        floor = floor_money(g * D("0.95"))
        self.assertGreater(half_up, g * D("0.95"))
        self.assertLessEqual(floor, g * D("0.95"))


class TestTenMonth(unittest.TestCase):
    """The guideline's ten-month frame: 50,000 + 33,337 EUR costs."""

    def setUp(self) -> None:
        self.regular = compute_budget(950)
        self.second = second_stage_budget(634)
        self.combined = combined_ten_month_budget(self.regular, self.second)

    def test_total_cost_cap(self) -> None:
        self.assertEqual(MAX_COST_TEN_MONTH, D("83337.00"))

    def test_max_strict_funding(self) -> None:
        self.assertEqual(self.combined["max_strict_funding"], D("79170.15"))

    def test_total_costs(self) -> None:
        self.assertEqual(self.combined["total_g"], D("83160.00"))

    def test_total_funding(self) -> None:
        self.assertEqual(self.combined["total_f"], D("79002.00"))

    def test_total_own_contribution(self) -> None:
        self.assertEqual(self.combined["total_ea"], D("4158.00"))

    def test_total_hours(self) -> None:
        self.assertEqual(self.combined["total_hours"], 1584)

    def test_financing_identity(self) -> None:
        self.assertEqual(
            self.combined["total_g"],
            self.combined["total_f"] + self.combined["total_ea"],
        )

    def test_communicated_10_month_gap(self) -> None:
        self.assertEqual(
            self.combined["max_strict_funding"] - COMM_TEN_MONTH_FUNDING,
            D("3.15"),
        )

    def test_second_phase_above_cap_breaks_combined(self) -> None:
        too_high = second_stage_budget(635)
        combined = combined_ten_month_budget(self.regular, too_high)
        self.assertFalse(combined["compliant"])

    def test_second_stage_hours_must_not_exceed_regular_hours(self) -> None:
        short_regular = compute_budget(600)
        second = second_stage_budget(634, regular_hours=950)
        combined = combined_ten_month_budget(short_regular, second)
        self.assertFalse(combined["compliant"])
        self.assertIn(
            "K5_second_stage_hours_exceed_regular_phase",
            combined["violations"],
        )

    def test_child_violations_are_propagated(self) -> None:
        short_regular = compute_budget(600)
        second = second_stage_budget(635)  # itself over the Second-Stage cost cap
        combined = combined_ten_month_budget(short_regular, second)
        self.assertFalse(combined["compliant"])
        self.assertTrue(
            any("second:total_cost_cap_exceeded" in v for v in combined["violations"]),
            combined["violations"],
        )

    def test_second_stage_hours_equal_regular_hours_is_allowed(self) -> None:
        regular = compute_budget(633)
        second = second_stage_budget(633, regular_hours=633)
        combined = combined_ten_month_budget(regular, second)
        self.assertTrue(combined["compliant"], combined["violations"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
