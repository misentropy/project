# Lesson 0: Setup on Arch Linux

**Goal:** Wireshark and tshark installed, capturing as a normal user (not root), first capture saved.

## 1. Install

```bash
sudo pacman -S wireshark-qt
```

`wireshark-qt` is the GUI and pulls in `wireshark-cli`, which provides `tshark`, `dumpcap`, `capinfos` and `editcap`. If you only want the command line, install `wireshark-cli` alone.

## 2. Capture without running as root

Never run the Wireshark GUI as root. The dissectors parse untrusted data from the network, so a bug in one would run with full privileges. Only the small `dumpcap` helper needs special rights, and the Arch package already gives it the needed capabilities. You just need to be in the `wireshark` group:

```bash
sudo usermod -aG wireshark $USER
```

Then log out and back in (a new group only applies to new sessions). Verify:

```bash
groups                      # should list "wireshark"
getcap /usr/bin/dumpcap     # should show cap_net_admin,cap_net_raw
```

If `getcap` shows nothing, reinstall the package: `sudo pacman -S wireshark-cli`.

## 3. List your interfaces

```bash
tshark -D
```

Typical names on Arch:

| Name | What it is |
|------|------------|
| `lo` | Loopback, traffic from your machine to itself |
| `enp...` / `eth0` | Wired ethernet |
| `wlp...` / `wlan0` | Wi-Fi |
| `any` | Every interface at once |

Find which one carries your traffic with `ip -br link` and `ip route`.

## 4. First capture

GUI: run `wireshark`, double-click your interface, open a website in a browser, then press the red square to stop.

Command line:

```bash
tshark -i wlan0 -c 50 -w ~/captures/first.pcapng
```

(`-c 50` stops after 50 packets. Create `~/captures` first, and keep it **outside** this repo.)

Read it back:

```bash
tshark -r ~/captures/first.pcapng | head
capinfos ~/captures/first.pcapng
```

## 5. Keep captures out of git

This repo's `.gitignore` blocks `*.pcap` and `*.pcapng`. A capture of your own traffic can contain cookies, usernames, DNS history and device names. Store captures in `~/captures`, and only publish deliberately sanitised screenshots or text excerpts.

## 6. Troubleshooting

| Symptom | Fix |
|---------|-----|
| "You don't have permission to capture" | Not in the `wireshark` group yet, or you haven't logged out and back in |
| No interfaces listed | Same cause; check `groups` and `getcap` |
| Only broadcast/own traffic on Wi-Fi | Normal. A switch or access point only sends you your own traffic. Monitor mode is a separate topic |
| GUI looks wrong on Wayland | Try `QT_QPA_PLATFORM=xcb wireshark` |

## Checkpoint

- [ ] `tshark -D` lists interfaces without sudo
- [ ] I saved a capture and re-opened it
- [ ] I know where my captures live and that they're not in git

Next: [Lesson 1: Interface and first capture](01-interface-and-first-capture.md)
