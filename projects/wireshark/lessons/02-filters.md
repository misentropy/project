# Lesson 2: Capture filters vs display filters

**Goal:** know which filter type to use and write the ten filters you'll use constantly.

## Two different filter languages

| | Capture filter | Display filter |
|--|----------------|----------------|
| Applied | **Before** packets are saved | **After**, on what's already captured |
| Syntax | BPF (same as `tcpdump`) | Wireshark's own |
| Effect | Packets are discarded for good | Packets are only hidden |
| Use for | Huge captures, saving disk | Nearly everything else |

Beginners mix these up and get errors. `host 1.2.3.4` is BPF (capture). `ip.addr == 1.2.3.4` is a display filter. The filter bar turns green when valid, red when not.

## Capture filter examples (BPF)

```
host 192.168.1.10
port 53
tcp port 443
not port 22
net 192.168.1.0/24
```

Use `not port 22` when capturing over SSH, or you capture your own SSH session in a loop.

## Display filter basics

Comparison: `==  !=  >  <  >=  <=`   Logic: `&&  ||  !`   Membership: `in {1 2 3}`   Text: `contains`, `matches`

## The ten to memorise

| Filter | Shows |
|--------|-------|
| `ip.addr == 192.168.1.10` | Traffic to or from a host |
| `ip.src == X && ip.dst == Y` | One direction between two hosts |
| `tcp.port == 443` | TCP traffic on a port |
| `dns` | All DNS |
| `dns.qry.name contains "example"` | Lookups for a name |
| `http.request` | HTTP requests only |
| `tls.handshake.type == 1` | TLS Client Hello (shows server name) |
| `tcp.flags.syn == 1 && tcp.flags.ack == 0` | New connection attempts |
| `tcp.analysis.flags` | Retransmissions, resets, other TCP problems |
| `!(arp \|\| dns \|\| icmp)` | Everything except background noise |

(Inside a markdown table `|` is escaped as `\|`; type a plain `||` in Wireshark.)

## Tips

- Right-click any field > **Apply as Filter > Selected**. Wireshark writes the syntax for you, which is the fastest way to learn field names.
- Start typing in the bar; it autocompletes field names.
- **Prepare as Filter** builds without applying, so you can combine with `&&`.
- Save good ones with the `+` button on the filter bar.

## Exercise

Capture 2-3 minutes of normal browsing, then write a display filter for each:

1. Only traffic to or from your own IP
2. Only DNS queries (not responses). Hint: `dns.flags.response == 0`
3. Only TLS Client Hellos, with a column showing the server name (`tls.handshake.extensions_server_name`)
4. Every TCP reset (`tcp.flags.reset == 1`)
5. Everything except your local broadcast noise

Record the filters that worked in your cheatsheet: [display-filters.md](../cheatsheets/display-filters.md).

## Checkpoint

- [ ] I can explain why a capture filter can't be changed after the fact
- [ ] I can write a display filter from a field I clicked

Next: [Lesson 3: Core protocols](03-core-protocols.md)
