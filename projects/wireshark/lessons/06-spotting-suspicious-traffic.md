# Lesson 6: Spotting suspicious traffic

**Goal:** turn "what is normal" into "what looks wrong", and learn to describe it carefully. This is the bridge to incident response.

> **Important:** a pattern here is a *lead*, not a verdict. Every item below also has innocent explanations. Analysts note the evidence, state their confidence, and look for a second source before concluding anything.

## Patterns and how they look

### Port scan

One source touching many ports (or many hosts) in a short time.

- Many `SYN` packets from one IP to different `tcp.dstport` values
- Closed ports answer `RST, ACK`; open ones answer `SYN, ACK`
- Filter: `tcp.flags.syn==1 && tcp.flags.ack==0`, then **Statistics > Conversations** sorted by packets
- Only ever test this against your **own** lab (see Lab 04)

### Beaconing

Malware checking in with a controller at regular intervals.

- Same destination, near-constant interval (every 60s, say) and similar packet sizes
- Look in **I/O Graphs** for evenly spaced spikes, or compare `frame.time_delta_displayed` after filtering to one conversation
- Innocent look-alikes: NTP, software update checks, chat apps, calendar sync. Compare against a baseline capture of a clean machine

### Suspicious DNS

- Very long or high-entropy subdomains (`a8f3kq0z9xj2....example.com`): possible tunnelling or DGA domains
- Large numbers of `NXDOMAIN` responses: domain-generation algorithms or typos
- Lots of `TXT` queries to one domain
- Filters: `dns.qry.name.len > 50`, `dns.flags.rcode == 3`, `dns.qry.type == 16`

### ARP spoofing

- Two different MACs claiming the same IP
- Gratuitous ARP replies nobody asked for
- Filter: `arp.duplicate-address-detected` or `arp.opcode == 2`

### Cleartext credentials

- `http.authbasic`, `ftp.request.command == "PASS"`, `telnet`
- The fix is not hiding it better; it's using an encrypted protocol

### Data exfiltration (large outbound transfer)

- A host with far more bytes **out** than in, to an unusual destination, often at odd hours
- **Statistics > Conversations**, sort by bytes, compare direction

## How to write it up

For each finding, record:

1. **Observation:** what exactly appears in the capture (filter used, packet numbers, timestamps)
2. **Hypothesis:** what might explain it
3. **Alternative explanations:** what else could be true
4. **Next step:** what would confirm or rule it out (logs, process list, threat-intel lookup)

This structure is what separates analysis from guessing, and it's what I want my write-ups to show.

## Practice material

Practise on captures made for training rather than real victims' data:

- Your own lab captures (Lab 04)
- Wireshark's sample captures: `https://wiki.wireshark.org/SampleCaptures`
- Malware-Traffic-Analysis.net exercises (password-protected archives, handle in a VM)

Treat any malware-related capture as hostile: open it in a VM, never on your daily machine.

## Checkpoint

- [ ] I can describe the signature of a scan, a beacon and DNS tunnelling
- [ ] I can state an alternative innocent explanation for each
- [ ] I use the observation / hypothesis / alternatives / next-step format
