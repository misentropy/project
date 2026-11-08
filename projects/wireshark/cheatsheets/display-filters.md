# Display filter cheatsheet

Display filters are typed in the bar above the packet list. Green = valid, red = error.

## Operators

| Operator | Meaning |
|----------|---------|
| `==` `!=` | equal, not equal |
| `>` `<` `>=` `<=` | comparison |
| `&&` `\|\|` `!` | and, or, not |
| `contains` | substring match |
| `matches` | regular expression |
| `in {a b c}` | one of a set |

## Hosts and ports

```
ip.addr == 192.168.1.10
ip.src == 192.168.1.10
ip.dst == 192.168.1.10
ip.addr == 192.168.1.0/24
tcp.port == 443
udp.port == 53
tcp.dstport in {80 443 8080}
eth.addr == aa:bb:cc:dd:ee:ff
```

## Protocols

```
dns
http
tls
arp
icmp
dhcp
tcp
udp
```

## DNS

```
dns.flags.response == 0         # queries only
dns.flags.response == 1         # responses only
dns.qry.name contains "arch"
dns.qry.type == 1               # A records
dns.qry.type == 28              # AAAA records
dns.qry.type == 16              # TXT records
dns.flags.rcode == 3            # NXDOMAIN
dns.qry.name.len > 50           # suspiciously long names
```

## TCP

```
tcp.flags.syn == 1 && tcp.flags.ack == 0    # connection attempts
tcp.flags.syn == 1 && tcp.flags.ack == 1    # SYN-ACK replies
tcp.flags.reset == 1                        # resets
tcp.flags.fin == 1                          # closes
tcp.analysis.retransmission
tcp.analysis.flags                          # all TCP problems
tcp.stream eq 4                             # one specific conversation
```

## HTTP and TLS

```
http.request
http.request.method == "POST"
http.host contains "example"
http.response.code >= 400
tls.handshake.type == 1                     # Client Hello
tls.handshake.type == 2                     # Server Hello
tls.handshake.extensions_server_name        # SNI field
```

## Time

```
frame.time_delta > 1                        # gaps longer than 1 second
frame.number >= 100 && frame.number <= 200
```

## Combining

```
ip.addr == 192.168.1.10 && !(dns || arp)
(tcp.port == 80 || tcp.port == 443) && ip.dst == 93.184.216.34
```

## Filters I worked out myself

(Add yours here as you go.)

| Filter | What it finds | Date |
|--------|---------------|------|
|  |  |  |
