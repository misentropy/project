# Lesson 3: Core protocols

**Goal:** recognise what normal looks like for the protocols you'll see in every capture. You can't spot abnormal until normal is familiar.

## ARP: "who has this IP?"

Maps an IP to a MAC on the local network.

- Request: broadcast `Who has 192.168.1.1? Tell 192.168.1.20`
- Reply: unicast `192.168.1.1 is at aa:bb:cc:...`
- Filter: `arp`
- Security note: ARP has no authentication. Many unsolicited replies, or two MACs claiming one IP, is how ARP spoofing looks (`arp.duplicate-address-detected`).

## DNS: names to addresses

Usually UDP port 53. One query, one response, matched by the **transaction ID**.

- Query types: `A` (IPv4), `AAAA` (IPv6), `MX`, `TXT`, `PTR`, `CNAME`
- Check the response code: `NOERROR` is fine, `NXDOMAIN` means the name doesn't exist
- Filter: `dns`, or `dns.flags.rcode != 0` for failures
- Security note: DNS is unencrypted by default, so anyone on-path sees every name you look up. Tunnelling malware abuses long, random-looking names and `TXT` queries.

## TCP: the three-way handshake

```
Client                    Server
  |-------- SYN ---------->|     seq = x
  |<------ SYN, ACK -------|     seq = y, ack = x+1
  |-------- ACK ---------->|     ack = y+1
          connected
```

Teardown uses `FIN` (polite) or `RST` (abrupt, or "nothing is listening here").

- New connections: `tcp.flags.syn == 1 && tcp.flags.ack == 0`
- Resets: `tcp.flags.reset == 1`
- Wireshark shows **relative** sequence numbers by default. The real ones are random starting values; turn this off in Preferences > Protocols > TCP if you want to see them.

## UDP

No handshake, no delivery guarantee. Just source port, destination port, length, checksum. DNS, DHCP, NTP and most voice/video use it.

## HTTP (cleartext)

If a site uses plain HTTP, everything is readable: method, path, headers, cookies, body.

- Filter: `http.request.method == "GET"`
- Look at: `Host`, `User-Agent`, `Cookie`, `Authorization`
- This is why passwords over HTTP are a vulnerability, and why Lab 03 exists.

## TLS (HTTPS)

You can't read the content, but the handshake still tells you a lot:

- **Client Hello** carries the **SNI**, the server name, in clear text (unless Encrypted Client Hello is in use)
- **Server Hello** picks the TLS version and cipher suite
- **Certificate** shows who the server claims to be (in TLS 1.2; TLS 1.3 encrypts it)
- Filter: `tls.handshake`

To decrypt your **own** browser traffic for study, set `SSLKEYLOGFILE` and point Wireshark at it (Preferences > Protocols > TLS > Pre-Master-Secret log filename). Treat that log like a password; it's in `.gitignore` for a reason.

```bash
SSLKEYLOGFILE=~/captures/sslkeys.log firefox
```

## DHCP

The four-step "DORA": **D**iscover, **O**ffer, **R**equest, **A**cknowledge. Broadcast on UDP 67/68. Filter: `dhcp` (or `bootp` in older versions). Renew your lease to see it live: `sudo dhcpcd -n` or reconnect Wi-Fi.

## Exercise

Capture while you: reconnect to Wi-Fi, open one HTTPS site, and run `dig archlinux.org`. Then find and note: the DHCP exchange, the ARP for your gateway, the DNS query/response, the TCP handshake and the TLS Client Hello with its SNI. Screenshot each (after checking for private data).

## Checkpoint

- [ ] I can draw the TCP handshake and point to it in a capture
- [ ] I can say what is visible in HTTPS traffic and what is not
- [ ] I know what NXDOMAIN means

Next: [Lesson 4: Streams and statistics](04-streams-and-statistics.md)
