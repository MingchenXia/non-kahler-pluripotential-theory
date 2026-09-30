#!/usr/bin/env python3
"""Focused checks for public page numbering and the bounded homepage edit."""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("publisher", Path(__file__).with_name("publish-homepage.py"))
publisher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publisher)


class PublicationTests(unittest.TestCase):
    def test_printed_number_is_not_pdf_length(self):
        with patch.object(publisher, "run", side_effect=["Pages: 907\n", "Index       883\nRegularization 38\n"]):
            self.assertEqual(publisher.printed_page_number(Path("book.pdf")), (883, 907, 907))

    def test_trailing_blank_page(self):
        with patch.object(publisher, "run", side_effect=["Pages: 908\n", "\f", "883    Index\n"]):
            self.assertEqual(publisher.printed_page_number(Path("book.pdf")), (883, 908, 907))

    def test_body_number_is_not_page_number(self):
        with self.assertRaises(RuntimeError):
            publisher.index_page_number("Index\nRegularization 883\n")

    def test_only_book_abstract_changes(self):
        old = "A research monograph. 899 pages. Updated September 27, 2026."
        source = f"- Other book\n\n  > **Abstract.** {old}\n\n- {publisher.BOOK_LINK}\n\n  > **Abstract.** {old}\n\n- Next paper\n  > **Abstract.** Unchanged.\n"
        updated, description = publisher.update_abstract(source, 883, "September 30, 2026")
        self.assertEqual(updated, source.replace(old, description, 2).replace(description, old, 1))
        self.assertIn("883 pages", description)

    def test_missing_or_duplicate_book_entry_stops(self):
        for source in ["Other page", publisher.BOOK_LINK * 2]:
            with self.assertRaises(RuntimeError):
                publisher.update_abstract(source, 883, "September 30, 2026")

    def test_custom_abstract_is_preserved(self):
        with self.assertRaises(RuntimeError):
            publisher.update_abstract(publisher.BOOK_LINK + "\n> **Abstract.** New author text.\n", 883, "September 30, 2026")

    def test_nested_source_package_cannot_publish(self):
        with patch.object(publisher, "run", side_effect=[str(publisher.ROOT.parent), publisher.SOURCE_REMOTE]):
            self.assertFalse(publisher.is_authoring_checkout())


if __name__ == "__main__":
    unittest.main()
