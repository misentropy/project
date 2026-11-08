#!/usr/bin/env python3
"""Summarise a packet capture using tshark.

Usage:
    python pcap_summary.py capture.pcapng [--top N]

Prints top source IPs, protocol counts, most-queried DNS names, TLS server
names (SNI) and TCP reset counts. Needs `tshark` (Arch: `pacman -S wireshark-cli`).

Packet contents are attacker-controlled, so everything read from a capture is
treated as untrusted text: tshark is called with an argument list (no shell),
and output is only counted and printed, never executed or evaluated.
"""

import argparse
import shutil
import subprocess
import sys
from collections import Counter


def run_tshark(pcap, display_filter, fields):
    """Return a list of rows (each a list of field strings) from tshark."""
    cmd = ["tshark", "-r", pcap, "-T", "fields", "-E", "separator=/t"]
    if display_filter:
        cmd += ["-Y", display_filter]
    for field in fields:
        cmd += ["-e", field]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return parse_rows(result.stdout, len(fields))


def parse_rows(output, n_fields):
    """Split tshark tab-separated output into rows padded to n_fields."""
    rows = []
    for line in output.splitlines():
        parts = line.split("\t")
        parts += [""] * (n_fields - len(parts))
        rows.append(parts[:n_fields])
    return rows


def count_column(rows, index):
    """Count non-empty values in one column."""
    return Counter(row[index] for row in rows if row[index])


def top_sources(pcap):
    return count_column(run_tshark(pcap, "ip", ["ip.src"]), 0)


def protocol_counts(pcap):
    rows = run_tshark(pcap, "", ["frame.protocols"])
    counts = Counter()
    for (chain,) in rows:
        if chain:
            counts[chain.split(":")[-1]] += 1  # innermost protocol
    return counts


def dns_names(pcap):
    rows = run_tshark(pcap, "dns.flags.response == 0", ["dns.qry.name"])
    return count_column(rows, 0)


def tls_server_names(pcap):
    rows = run_tshark(
        pcap,
        "tls.handshake.type == 1",
        ["tls.handshake.extensions_server_name"],
    )
    return count_column(rows, 0)


def reset_sources(pcap):
    rows = run_tshark(pcap, "tcp.flags.reset == 1", ["ip.src"])
    return count_column(rows, 0)


def print_section(title, counter, top):
    print(f"\n== {title} ==")
    if not counter:
        print("  (none)")
        return
    for value, count in counter.most_common(top):
        print(f"  {count:>7}  {value}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Summarise a capture with tshark")
    parser.add_argument("pcap", help="path to a .pcap or .pcapng file")
    parser.add_argument("--top", type=int, default=10, help="rows per section")
    args = parser.parse_args(argv)

    if shutil.which("tshark") is None:
        sys.exit("tshark not found. On Arch: sudo pacman -S wireshark-cli")

    try:
        print_section("Top source IPs", top_sources(args.pcap), args.top)
        print_section("Protocols (innermost)", protocol_counts(args.pcap), args.top)
        print_section("DNS names queried", dns_names(args.pcap), args.top)
        print_section("TLS server names (SNI)", tls_server_names(args.pcap), args.top)
        print_section("TCP resets by source", reset_sources(args.pcap), args.top)
    except subprocess.CalledProcessError as err:
        sys.exit(f"tshark failed: {err.stderr.strip() or err}")


if __name__ == "__main__":
    main()
