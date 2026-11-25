#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Integritätsprüfung der Forschungs-Evidenz (Standardbibliothek, offline).

Prüft ausschließlich die im Repository abgelegten Forschungsartefakte:

* ``reference-dataset.json``  — 30 Referenzfelder mit Koordinaten und Klassifikation
* ``fim-fields-S00000159V1.4.json`` — extrahierter FIM-Metadatenindex
* ``synthetic-instance.xml``  — synthetische, normalisierte Testinstanz
* ``EVIDENCE.md``             — Hashregister der lokalen Artefakte

Abgrenzung (project-boundary.md §C.1): Dieses Modul ist ein Analyse-/Validierungsskript.
Es enthält **keine** FormBridge-Pipeline (keine PDF-Extraktion, keine Feldzuordnung,
keine FIM-Auflösung) und implementiert kein Forschungsziel. Es belegt lediglich, dass die
veröffentlichten Artefakte strukturell und hashseitig unverändert sind.

Ausführen::

    python3 -m unittest discover -s docs/research/evidence -p 'test_*.py' -v
"""

import hashlib
import json
import os
import re
import unittest
import xml.etree.ElementTree as ET

EVIDENCE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET = os.path.join(EVIDENCE_DIR, "reference-dataset.json")
FIM_INDEX = os.path.join(EVIDENCE_DIR, "fim-fields-S00000159V1.4.json")
INSTANCE = os.path.join(EVIDENCE_DIR, "synthetic-instance.xml")
MANIFEST = os.path.join(EVIDENCE_DIR, "EVIDENCE.md")

ID_PATTERN = re.compile(r"[FG]\d{8}V\d+\.\d+")
CLASSIFICATIONS = {
    "MAPPED", "CONTEXT_REQUIRED", "VALUE_CODELIST", "STRUCTURAL_EXPANSION",
    "STRUCTURAL_MISMATCH", "AMBIGUOUS_SEMANTIC", "COVERAGE_GAP", "UNMATCHED",
}
# im Repository dokumentierte Verteilung (validation-report.md: "7/7/4/4/2/3/3")
EXPECTED_CLASSIFICATION_COUNTS = {
    "MAPPED": 7,
    "CONTEXT_REQUIRED": 7,
    "VALUE_CODELIST": 4,
    "STRUCTURAL_EXPANSION": 3,
    "STRUCTURAL_MISMATCH": 1,
    "AMBIGUOUS_SEMANTIC": 2,
    "COVERAGE_GAP": 3,
    "UNMATCHED": 3,
}
EXPECTED_NODES = {"group": 185, "field": 88, "builtin": 367}  # 640 Knoten gesamt


def _load_json(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _manifest_hashes():
    """Liest das Hashregister aus EVIDENCE.md: | `datei` | bytes | zeilen | `sha256` |."""
    rows = {}
    with open(MANIFEST, encoding="utf-8") as handle:
        for line in handle:
            match = re.match(
                r"^\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*`([0-9a-f]{64})`\s*\|\s*$",
                line.rstrip("\n"),
            )
            if match:
                name, size, lines, sha = match.groups()
                rows[name] = {"bytes": int(size), "lines": int(lines), "sha256": sha}
    return rows


class ReferenceDatasetTest(unittest.TestCase):
    """30-Feld-Referenzdatensatz: Struktur und dokumentierte Klassifikation."""

    @classmethod
    def setUpClass(cls):
        cls.entries = _load_json(DATASET)

    def test_is_list_of_thirty_entries(self):
        self.assertIsInstance(self.entries, list)
        self.assertEqual(len(self.entries), 30)

    def test_entry_schema(self):
        allowed = {"n", "page", "bbox", "pdf_label", "fim", "classification", "note"}
        for entry in self.entries:
            with self.subTest(n=entry.get("n")):
                self.assertEqual(set(entry), allowed)
                self.assertIsInstance(entry["n"], int)
                self.assertIsInstance(entry["page"], int)
                self.assertGreaterEqual(entry["page"], 1)
                self.assertIsInstance(entry["bbox"], list)
                self.assertEqual(len(entry["bbox"]), 4)
                for value in entry["bbox"]:
                    self.assertIsInstance(value, int)
                self.assertLess(entry["bbox"][0], entry["bbox"][2])
                self.assertLess(entry["bbox"][1], entry["bbox"][3])
                self.assertTrue(entry["pdf_label"].strip())
                self.assertIsInstance(entry["fim"], str)
                self.assertIn(entry["classification"], CLASSIFICATIONS)
                self.assertIsInstance(entry["note"], str)

    def test_numbering_is_sequential(self):
        self.assertEqual([entry["n"] for entry in self.entries], list(range(1, 31)))

    def test_classification_distribution(self):
        counts = {}
        for entry in self.entries:
            counts[entry["classification"]] = counts.get(entry["classification"], 0) + 1
        self.assertEqual(counts, EXPECTED_CLASSIFICATION_COUNTS)
        self.assertEqual(sum(counts.values()), 30)

    def test_documented_counts(self):
        """7 umsetzbare Felder, 7 Kontext-Mehrdeutigkeiten, 4 Codelisten, 4 Strukturtransformationen, 3 Deckungslücken."""
        counts = {}
        for entry in self.entries:
            counts[entry["classification"]] = counts.get(entry["classification"], 0) + 1
        self.assertEqual(counts["MAPPED"], 7)  # 7/30 trivial abbildbar
        self.assertEqual(counts["CONTEXT_REQUIRED"], 7)  # Kontext-Mehrdeutigkeiten
        self.assertEqual(counts["VALUE_CODELIST"], 4)  # Codelisten
        structural = counts["STRUCTURAL_EXPANSION"] + counts["STRUCTURAL_MISMATCH"]
        self.assertEqual(structural, 4)  # Strukturtransformationen
        self.assertEqual(counts["COVERAGE_GAP"], 3)  # fachliche Deckungslücken

    def test_target_path_consistency(self):
        for entry in self.entries:
            with self.subTest(n=entry["n"], classification=entry["classification"]):
                if entry["classification"] == "MAPPED":
                    self.assertTrue(entry["fim"].startswith("/"))
                if entry["classification"] in {"UNMATCHED", "COVERAGE_GAP"}:
                    self.assertEqual(entry["fim"], "—")


class FimIndexTest(unittest.TestCase):
    """Extrahierter FIM-Metadatenindex: Wohlgeformtheit und dokumentierte Invarianten."""

    @classmethod
    def setUpClass(cls):
        cls.nodes = _load_json(FIM_INDEX)

    def test_is_list_of_640_nodes(self):
        self.assertIsInstance(self.nodes, list)
        self.assertEqual(len(self.nodes), 640)

    def test_node_schema(self):
        allowed = {"path", "id", "label", "kind", "type", "depth"}
        for node in self.nodes:
            with self.subTest(id=node.get("id"), path=node.get("path")):
                self.assertEqual(set(node), allowed)
                self.assertIn(node["kind"], {"group", "field", "builtin"})
                self.assertRegex(node["id"], ID_PATTERN)
                self.assertTrue(node["path"].startswith("/"))
                self.assertTrue(node["path"].endswith(node["id"]))
                self.assertTrue(node["label"].strip())
                self.assertTrue(node["type"].strip())
                self.assertIsInstance(node["depth"], int)
                self.assertGreaterEqual(node["depth"], 0)

    def test_documented_kind_distribution(self):
        counts = {}
        for node in self.nodes:
            counts[node["kind"]] = counts.get(node["kind"], 0) + 1
        self.assertEqual(counts, EXPECTED_NODES)
        self.assertEqual(sum(counts.values()), 640)
        self.assertEqual(counts["group"], 185)
        self.assertEqual(counts["field"], 88)

    def test_paths_are_unique(self):
        paths = [node["path"] for node in self.nodes]
        self.assertEqual(len(paths), len(set(paths)))

    def test_depth_is_consistent_with_path(self):
        for node in self.nodes:
            with self.subTest(path=node["path"]):
                self.assertEqual(node["depth"], node["path"].count("/") - 1)


class SyntheticInstanceTest(unittest.TestCase):
    """Synthetische Instanz: Wohlgeformtheit und Bindung an den Feldindex."""

    @classmethod
    def setUpClass(cls):
        cls.tree = ET.parse(INSTANCE)
        cls.root = cls.tree.getroot()
        cls.index_ids = {node["id"] for node in _load_json(FIM_INDEX)}
        cls.element_ids = [
            element.tag.split("}")[1] for element in cls.root.iter() if element is not cls.root
        ]

    def test_root_and_namespace(self):
        namespace, _, localname = self.root.tag.partition("}")
        self.assertEqual(localname, "Wohngeld_Mietzuschuss_Erstantrag")
        self.assertEqual(namespace.lstrip("{"), "urn:xoev-de:xfall:standard:fim-s00000159_1.4")

    def test_ten_top_level_groups(self):
        children = list(self.root)
        self.assertEqual(len(children), 10)
        for child in children:
            name = child.tag.split("}")[1]
            self.assertTrue(name.startswith("G"), name)
            self.assertRegex(name, ID_PATTERN)

    def test_element_ids_match_documented_pattern(self):
        self.assertEqual(len(self.element_ids), 99)
        self.assertEqual(len(set(self.element_ids)), 99)
        for element_id in self.element_ids:
            self.assertRegex(element_id, ID_PATTERN)

    def test_every_element_exists_in_the_fim_index(self):
        unknown = sorted(set(self.element_ids) - self.index_ids)
        self.assertEqual(unknown, [])

    def test_values_are_synthetic(self):
        values = [(element.text or "").strip() for element in self.root.iter()]
        joined = " ".join(value for value in values if value)
        for marker in ("Mustermann", "Mustergeb", "Musterstadt"):
            self.assertIn(marker, joined)


class EvidenceManifestTest(unittest.TestCase):
    """Hashregister in EVIDENCE.md stimmt mit den lokalen Artefakten überein."""

    ARTIFACTS = {
        "reference-dataset.json": DATASET,
        "fim-fields-S00000159V1.4.json": FIM_INDEX,
        "synthetic-instance.xml": INSTANCE,
    }

    def test_manifest_lists_all_artifacts(self):
        rows = _manifest_hashes()
        for name in self.ARTIFACTS:
            with self.subTest(artifact=name):
                self.assertIn(name, rows, f"{name} fehlt im Hashregister von EVIDENCE.md")

    def test_hashes_match_files(self):
        rows = _manifest_hashes()
        for name, path in self.ARTIFACTS.items():
            with self.subTest(artifact=name):
                self.assertIn(name, rows)
                expected = rows[name]
                self.assertEqual(_sha256(path), expected["sha256"], "SHA-256 weicht ab")
                self.assertEqual(os.path.getsize(path), expected["bytes"], "Bytegröße weicht ab")

    def test_manifest_documents_reproduction_not_redistribution(self):
        with open(MANIFEST, encoding="utf-8") as handle:
            content = handle.read()
        self.assertIn("nicht redistribuiert", content)
        self.assertIn("Reproduktionsbefehle", content)


if __name__ == "__main__":
    unittest.main(verbosity=2)
