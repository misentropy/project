"""Tests for pcap_summary parsing and counting. They need no tshark or capture."""

import unittest
from unittest import mock

import pcap_summary


class ParseRowsTests(unittest.TestCase):
    def test_splits_on_tabs(self):
        self.assertEqual(
            pcap_summary.parse_rows("a\tb\nc\td\n", 2), [["a", "b"], ["c", "d"]]
        )

    def test_pads_short_rows(self):
        # tshark leaves trailing fields out when a packet lacks them
        self.assertEqual(pcap_summary.parse_rows("a\n", 2), [["a", ""]])

    def test_empty_output(self):
        self.assertEqual(pcap_summary.parse_rows("", 1), [])


class CountTests(unittest.TestCase):
    def test_count_column_ignores_empty(self):
        rows = [["x"], ["y"], ["x"], [""]]
        self.assertEqual(pcap_summary.count_column(rows, 0), {"x": 2, "y": 1})


class SectionTests(unittest.TestCase):
    def test_protocol_counts_uses_innermost(self):
        rows = [["eth:ethertype:ip:udp:dns"], ["eth:ethertype:ip:tcp:tls"], [""]]
        with mock.patch.object(pcap_summary, "run_tshark", return_value=rows):
            counts = pcap_summary.protocol_counts("x.pcapng")
        self.assertEqual(counts, {"dns": 1, "tls": 1})

    def test_dns_names_counts_queries(self):
        rows = [["archlinux.org"], ["archlinux.org"], ["example.com"]]
        with mock.patch.object(pcap_summary, "run_tshark", return_value=rows):
            names = pcap_summary.dns_names("x.pcapng")
        self.assertEqual(names.most_common(1), [("archlinux.org", 2)])

    def test_hostile_values_are_only_counted(self):
        # packet data may contain shell metacharacters; it must just be text
        rows = [["$(touch /tmp/pwned);`id`"]]
        with mock.patch.object(pcap_summary, "run_tshark", return_value=rows):
            names = pcap_summary.dns_names("x.pcapng")
        self.assertEqual(sum(names.values()), 1)


if __name__ == "__main__":
    unittest.main()
