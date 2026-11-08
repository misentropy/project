# Lab 01: Watching a DNS lookup

**Status:** not yet done
**Skills:** capture, display filters, DNS fields
**Authorisation:** own machine only

## Objective

Follow one DNS lookup from the query to the answer and identify every field that matters.

## Prediction

Write this before capturing: how many packets will a lookup of `archlinux.org` produce? Which protocol and port? Will the response contain one address or several?

> My prediction:

## Method

1. Flush any local cache if you use one (for `systemd-resolved`: `resolvectl flush-caches`).
2. Start a capture on your main interface with the capture filter `port 53`:
   ```bash
   tshark -i wlan0 -f "port 53" -w ~/captures/lab01.pcapng
   ```
3. In another terminal:
   ```bash
   dig archlinux.org A
   dig archlinux.org AAAA
   dig doesnotexist-12345.example A
   ```
4. Stop the capture and open it in Wireshark. Filter: `dns`.

## Things to find

- [ ] The query packet: transaction ID, query type, name
- [ ] The matching response: same transaction ID, answer count, TTL, addresses
- [ ] Which server answered (is it your router or a public resolver?)
- [ ] The `NXDOMAIN` response for the fake name: what rcode, and is there an answer section?
- [ ] The response time (`dns.time`)
- [ ] The transport: UDP or TCP, and the source port (random or fixed?)

## Observations

> Fill in after running.

## Analysis

> Questions to answer: Why is the source port random? What does the TTL tell a resolver to do? Who can see these queries on a typical home network?

## What I learned

-

## Next steps

- Repeat with DNS over HTTPS/TLS enabled in the browser and see what changes in the capture
