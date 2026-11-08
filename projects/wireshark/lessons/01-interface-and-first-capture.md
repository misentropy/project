# Lesson 1: The interface and your first capture

**Goal:** know what each pane shows and read a single packet from top to bottom.

## The three panes

| Pane | Shows | Use it to |
|------|-------|-----------|
| **Packet List** (top) | One row per packet: number, relative time, source, destination, protocol, length, info | Scan and pick a packet |
| **Packet Details** (middle) | The selected packet as a tree, one layer per protocol | Read fields layer by layer |
| **Packet Bytes** (bottom) | Raw hex and ASCII | See exactly what was on the wire |

Click a field in Details and the matching bytes highlight in Bytes. Do this a lot early on; it makes the layers real.

## The layers you will see

For a typical web request, top to bottom in the Details pane:

1. **Frame**: Wireshark's own metadata (capture time, length). Not on the wire.
2. **Ethernet II**: source and destination MAC addresses (local network only).
3. **Internet Protocol (IPv4/IPv6)**: source and destination IP, TTL, protocol number.
4. **TCP or UDP**: ports, sequence numbers, flags.
5. **Application**: DNS, HTTP, TLS, and so on.

This is the same stack as the OSI/TCP-IP model from networking fundamentals, only now you can see each header.

## Useful setup tweaks

- **View > Time Display Format > Time of Day** (or keep relative time, whichever helps).
- **Right-click a column header > Column Preferences**: add `tcp.dstport`, `ip.ttl` or `dns.qry.name` as columns.
- **View > Colouring Rules**: the colours are not decoration. Black rows with red text are TCP problems (resets, retransmissions); light blue is UDP/DNS.
- Save a **profile** (Edit > Configuration Profiles) called `learning` so your columns stick.

## Exercise

1. Start a capture on your main interface.
2. Run `ping -c 4 archlinux.org` in a terminal.
3. Stop the capture, apply the display filter `icmp`.
4. Click one echo request and write down, for each layer: the key fields and what they mean.
5. Match each request to its reply. What is the same? What differs? (Hint: look at the ICMP identifier, sequence number and the IP addresses.)

## Checkpoint

- [ ] I can name the five layers in the Details pane
- [ ] I can find a specific byte on the wire from a field name
- [ ] I made a `learning` profile

Next: [Lesson 2: Filters](02-filters.md)
