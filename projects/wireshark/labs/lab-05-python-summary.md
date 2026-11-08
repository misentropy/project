# Lab 05: Summarising a capture with Python

**Status:** not yet done
**Skills:** tshark, Python, subprocess, automation
**Authorisation:** own captures only

## Objective

Use [`scripts/pcap_summary.py`](../scripts/pcap_summary.py) to answer the Lesson 4 questions automatically, then extend it.

## Prediction

> Before running the script, which host do I think is my top talker, and which DNS name will be asked most?

## Method

1. Make a 5 minute capture of normal use:
   ```bash
   tshark -i wlan0 -a duration:300 -w ~/captures/lab05.pcapng
   ```
2. Run the script:
   ```bash
   python projects/wireshark/scripts/pcap_summary.py ~/captures/lab05.pcapng
   ```
3. Compare each section with what Wireshark shows (Protocol Hierarchy, Conversations, DNS statistics).
4. Run the script's tests to make sure my changes don't break parsing:
   ```bash
   python -m unittest discover projects/wireshark/scripts
   ```

## Extension tasks (pick one, commit it with a clear message)

- [ ] Count TCP resets per source IP
- [ ] Flag any source that sends SYNs to more than 50 distinct destination ports
- [ ] Flag DNS names longer than 50 characters
- [ ] Output JSON with `--json` for use in other tools
- [ ] Write a Markdown report to a file

## Observations

> Did the script and the GUI agree? Where did they differ and why?

## What I learned

-
