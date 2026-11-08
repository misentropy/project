# Lab 04: Recognising a port scan

**Status:** not yet done
**Skills:** traffic pattern recognition, Conversations and I/O statistics
**Authorisation:** scan **only your own machine** (`127.0.0.1`) or a VM you own. Never scan anyone else's network or hosts, including your ISP's router and other people on shared Wi-Fi.

## Objective

Learn what a port scan looks like from the *defender's* side, so I can recognise one in real logs.

## Prediction

> What will the packet pattern look like for open ports versus closed ports? How many distinct destination ports will one source touch?

## Method

1. Install nmap if needed: `sudo pacman -S nmap`
2. Start a capture on the loopback interface:
   ```bash
   tshark -i lo -w ~/captures/lab04.pcapng
   ```
3. Optionally start something listening so there is an open port:
   ```bash
   python -m http.server 8000
   ```
4. Scan yourself (the TCP connect scan needs no root):
   ```bash
   nmap -sT -p 1-1000 127.0.0.1
   ```
5. Stop the capture. In Wireshark:
   - Filter: `tcp.flags.syn == 1 && tcp.flags.ack == 0`
   - **Statistics > Conversations > TCP**: how many conversations from one source?
   - Compare an open port (8000) with a closed one.

## Things to find

- [ ] The burst: how many SYNs, and in what time window?
- [ ] An open port's exchange: SYN, SYN-ACK, ACK, then close
- [ ] A closed port's exchange: SYN, then RST-ACK
- [ ] The I/O Graph shape of the scan
- [ ] The source port behaviour across probes

## Observations

> Fill in after running.

## Analysis

Write this as an analyst would:

1. **Observation:** what exactly appears (filter, packet range)
2. **Hypothesis:** a scan from one host
3. **Alternative explanations:** a misconfigured app retrying connections, a network monitoring tool, a load balancer health check
4. **Next step:** what log or detection rule would confirm it

## What I learned

-

## Next steps

- Write a detection rule idea: "one source sends SYNs to more than N distinct ports within T seconds". Can the Python helper count this?
