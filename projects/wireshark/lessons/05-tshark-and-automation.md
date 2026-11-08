# Lesson 5: tshark and automation

**Goal:** do the same analysis from the terminal so it can be scripted. This connects directly to the Python automation goal in the main README.

## Why tshark

- Works over SSH on servers with no GUI
- Output can be piped into `sort`, `uniq`, `awk`, or Python
- Repeatable: the same command on the same capture gives the same answer, so results are easy to document

## Core flags

| Flag | Meaning |
|------|---------|
| `-i IFACE` | Capture on interface |
| `-r FILE` | Read a saved capture |
| `-w FILE` | Write a capture |
| `-c N` | Stop after N packets |
| `-a duration:60` | Stop after 60 seconds |
| `-f "port 53"` | Capture filter (BPF) |
| `-Y "dns"` | Display filter |
| `-T fields -e FIELD` | Print chosen fields only |
| `-E separator=,` | Field separator (CSV-style) |
| `-q -z STAT` | Quiet, print a statistic |

## Examples

Every DNS name queried, ranked:

```bash
tshark -r cap.pcapng -Y "dns.flags.response==0" -T fields -e dns.qry.name \
  | sort | uniq -c | sort -rn | head
```

Top source IPs:

```bash
tshark -r cap.pcapng -T fields -e ip.src | sort | uniq -c | sort -rn | head
```

Built-in statistics:

```bash
tshark -r cap.pcapng -q -z io,phs      # protocol hierarchy
tshark -r cap.pcapng -q -z conv,ip     # IP conversations
tshark -r cap.pcapng -q -z endpoints,ip
```

SNI of every TLS connection:

```bash
tshark -r cap.pcapng -Y "tls.handshake.type==1" \
  -T fields -e ip.dst -e tls.handshake.extensions_server_name
```

Find field names: `tshark -G fields | grep -i "dns.qry"`

## Calling tshark from Python

`subprocess` is enough. Ask tshark for tab-separated fields and parse them:

```python
import subprocess

def tshark_fields(pcap, display_filter, fields):
    cmd = ["tshark", "-r", pcap, "-Y", display_filter, "-T", "fields"]
    for f in fields:
        cmd += ["-e", f]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    return [line.split("\t") for line in out.splitlines()]
```

Pass arguments as a list (never `shell=True` with filenames or filters you didn't write yourself). Packet data is attacker-controlled, so treat anything you read from a capture as untrusted input.

This repo has a complete version: [`scripts/pcap_summary.py`](../scripts/pcap_summary.py).

## Exercise

1. Re-do the Lesson 4 questions using only tshark.
2. Run `scripts/pcap_summary.py` on your capture and compare its answers to the GUI.
3. Extend the script with one new feature (for example, count TCP resets per host) and commit it with a clear message.

## Checkpoint

- [ ] I can get top talkers and top DNS names from the command line
- [ ] I ran the Python helper and understand each function in it

Next: [Lesson 6: Spotting suspicious traffic](06-spotting-suspicious-traffic.md)
