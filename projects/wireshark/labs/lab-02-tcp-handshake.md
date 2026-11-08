# Lab 02: The TCP three-way handshake

**Status:** not yet done
**Skills:** TCP flags, sequence numbers, stream following
**Authorisation:** own machine only

## Objective

Capture a complete TCP connection, from handshake to close, and match each packet to the theory.

## Prediction

> Which three packets set up the connection, and which flags are set in each? What will the acknowledgement number in the second packet be, relative to the first sequence number?

## Method

1. Capture on your main interface:
   ```bash
   tshark -i wlan0 -f "tcp port 80" -w ~/captures/lab02.pcapng
   ```
2. In another terminal, make a plain-HTTP request:
   ```bash
   curl -v http://example.com/
   ```
3. Stop the capture, open it in Wireshark, filter `tcp`.
4. Right-click the first packet > **Follow > TCP Stream**.
5. Also try a connection to a closed port to compare:
   ```bash
   curl -v http://127.0.0.1:9/      # nothing listens on port 9
   ```
   (capture on `lo` for this one)

## Things to find

- [ ] SYN, SYN-ACK, ACK: packet numbers and flags
- [ ] Initial sequence numbers (turn off relative numbering to see the real ones)
- [ ] Window size and the MSS option in the SYN
- [ ] The HTTP request and response inside the stream
- [ ] The close: who sent FIN first? Was there a RST?
- [ ] For the closed port: what did the "server" send back instead of SYN-ACK?

## Observations

> Fill in after running.

## Analysis

> Why do both sides pick random initial sequence numbers? What does a RST in reply to a SYN tell a scanner?

## What I learned

-
