# Lesson 4: Following streams and using statistics

**Goal:** stop reading packet by packet. Rebuild whole conversations and get the big picture first.

## Follow a stream

Right-click a packet > **Follow > TCP Stream** (or `Ctrl+Alt+Shift+T`). Wireshark reassembles both directions into one readable view and applies a filter like `tcp.stream eq 5`.

- Red = client to server, blue = server to client
- Good for: HTTP, FTP, SMTP, Telnet and other readable protocols
- Also available: UDP, TLS (needs keys), HTTP/2, QUIC

Tip: after following, **clear the display filter** to go back to the full capture.

## The Statistics menu

| Menu item | Answers |
|-----------|---------|
| **Capture File Properties** | How long, how many packets, which interface |
| **Protocol Hierarchy** | What share of the capture is each protocol. Unexpected protocols stand out |
| **Conversations** | Every pair of hosts, with bytes and packets. Sort by bytes to find the heavy talker |
| **Endpoints** | Each host alone, with a geo-IP column if a database is configured |
| **I/O Graphs** | Traffic over time. Spikes and perfectly regular intervals are interesting |
| **Flow Graph** | Ladder diagram of a conversation |
| **DNS** (and HTTP) | Query counts, response codes, request tables |

## Workflow for an unknown capture

1. **Capture File Properties**: time span, size
2. **Protocol Hierarchy**: what protocols are present? Anything surprising?
3. **Conversations** (IPv4 tab): top talkers by bytes
4. **DNS** statistics: what names were looked up?
5. Only now pick a conversation and **Follow Stream**

Going from broad to narrow is what makes analysis fast. Starting at packet 1 is how you get lost in 200,000 rows.

## Expert Information

**Analyze > Expert Information** summarises problems Wireshark noticed: retransmissions, duplicate ACKs, zero windows, malformed packets. It's a good first look when something is slow or broken.

## Exercise

Capture 5 minutes of mixed normal use (browse, a video, a software update with `sudo pacman -Syu`, if you like). Without filtering first, answer:

1. What are the top three protocols by bytes?
2. Which remote host did you send or receive the most data with? Can you tell why?
3. What were the five most-queried DNS names?
4. Does the I/O Graph show any regular pattern? What causes it?

Write answers in a lab write-up using [TEMPLATE.md](../labs/TEMPLATE.md).

## Checkpoint

- [ ] I can follow a TCP stream and find it in the list again
- [ ] I run Protocol Hierarchy and Conversations before filtering

Next: [Lesson 5: tshark and automation](05-tshark-and-automation.md)
