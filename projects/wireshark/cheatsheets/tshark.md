# tshark cheatsheet

## Capture

```bash
tshark -D                                  # list interfaces
tshark -i wlan0                            # live capture, print to screen
tshark -i wlan0 -w ~/captures/x.pcapng     # save to file
tshark -i wlan0 -a duration:60 -w x.pcapng # stop after 60 s
tshark -i wlan0 -c 100 -w x.pcapng         # stop after 100 packets
tshark -i wlan0 -f "port 53" -w dns.pcapng # capture filter
```

## Read and filter

```bash
tshark -r x.pcapng                         # print everything
tshark -r x.pcapng -Y "dns"                # display filter
tshark -r x.pcapng -c 20                   # first 20 packets
tshark -r x.pcapng -V -Y "frame.number==5" # full detail of one packet
```

## Extract fields

```bash
tshark -r x.pcapng -T fields -e frame.time -e ip.src -e ip.dst
tshark -r x.pcapng -T fields -E header=y -E separator=, -e ip.src -e ip.dst
tshark -G fields | grep -i "tls.handshake"      # find field names
```

## Statistics

```bash
tshark -r x.pcapng -q -z io,phs            # protocol hierarchy
tshark -r x.pcapng -q -z conv,tcp          # TCP conversations
tshark -r x.pcapng -q -z endpoints,ip      # endpoints
tshark -r x.pcapng -q -z io,stat,10        # packets per 10 s
tshark -r x.pcapng -q -z dns,tree          # DNS summary
```

## One-liners

```bash
# Top talkers
tshark -r x.pcapng -T fields -e ip.src | sort | uniq -c | sort -rn | head

# Top DNS names asked
tshark -r x.pcapng -Y "dns.flags.response==0" -T fields -e dns.qry.name \
  | sort | uniq -c | sort -rn | head

# Server names in TLS handshakes
tshark -r x.pcapng -Y "tls.handshake.type==1" \
  -T fields -e ip.dst -e tls.handshake.extensions_server_name
```

## Other tools in the same package

| Tool | Use |
|------|-----|
| `capinfos x.pcapng` | Summary: duration, packet count, hashes |
| `editcap -c 1000 x.pcapng part.pcapng` | Split into 1000-packet files |
| `mergecap -w all.pcapng a.pcapng b.pcapng` | Merge captures |
| `dumpcap -i wlan0 -w x.pcapng` | The lean capture engine tshark uses |
