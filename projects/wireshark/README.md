# Wireshark: Network Traffic Analysis

A hands-on learning project: learn to capture and read network traffic with Wireshark and `tshark`, then document what I find.

**Status:** in progress. Lessons are written; lab findings get filled in as I complete each lab on my own machine.

## Why this project

Reading packets is the foundation for incident response, threat analysis and network security work. It also ties into my radio background: a protocol is a protocol, whether it is on a wire or over the air.

## Environment

- Arch Linux
- Wireshark + tshark (from the `wireshark-qt` / `wireshark-cli` packages)
- Python 3 for automation
- Only my own network and traffic, or deliberately provided practice captures

## Learning path

| # | Lesson | Goal |
|---|--------|------|
| 0 | [Setup on Arch](lessons/00-setup-arch.md) | Install, run as a normal user, first capture |
| 1 | [Interface and first capture](lessons/01-interface-and-first-capture.md) | Know what every pane shows |
| 2 | [Capture vs display filters](lessons/02-filters.md) | Find the packets that matter |
| 3 | [Core protocols](lessons/03-core-protocols.md) | DNS, ARP, TCP handshake, HTTP, TLS |
| 4 | [Following streams and statistics](lessons/04-streams-and-statistics.md) | Rebuild conversations, spot patterns |
| 5 | [tshark and automation](lessons/05-tshark-and-automation.md) | Command line and Python |
| 6 | [Spotting suspicious traffic](lessons/06-spotting-suspicious-traffic.md) | Scans, beaconing, odd DNS |

## Labs

Each lab is a repeatable exercise with a write-up section for my own findings.

| Lab | Topic | Done |
|-----|-------|------|
| [Lab 01](labs/lab-01-dns.md) | Watching a DNS lookup | [ ] |
| [Lab 02](labs/lab-02-tcp-handshake.md) | The TCP three-way handshake | [ ] |
| [Lab 03](labs/lab-03-http-vs-https.md) | HTTP in cleartext vs HTTPS | [ ] |
| [Lab 04](labs/lab-04-port-scan.md) | Recognising a port scan (own lab only) | [ ] |
| [Lab 05](labs/lab-05-python-summary.md) | Summarising a capture with Python | [ ] |

Lab template: [labs/TEMPLATE.md](labs/TEMPLATE.md)

## Cheatsheets and scripts

- [Display filters](cheatsheets/display-filters.md)
- [tshark commands](cheatsheets/tshark.md)
- [`scripts/pcap_summary.py`](scripts/pcap_summary.py): summarise a capture (top talkers, protocols, DNS queries)

## Rules I follow

1. Capture only networks and devices I own or have explicit permission to test.
2. Never commit `.pcap` / `.pcapng` files or TLS key logs. The `.gitignore` blocks them, and screenshots get checked for IPs, MACs, cookies and names before committing.
3. Write down what I expected before I look at the packets, then compare.
