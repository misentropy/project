# Lab 03: HTTP in cleartext vs HTTPS

**Status:** not yet done
**Skills:** HTTP and TLS analysis, TLS key logging
**Authorisation:** own machine, and a **test login with a throwaway password** only

## Objective

See concretely what an observer on the network can and cannot read in HTTP versus HTTPS.

## Prediction

> For an HTTPS site, which pieces of information will still be visible to someone capturing on my network?

## Method

### Part A: cleartext HTTP

1. Run a throwaway local web server with a fake login form, for example:
   ```bash
   mkdir -p ~/labweb && cd ~/labweb
   echo '<form method=POST action=/login><input name=user><input name=pw></form>' > index.html
   python -m http.server 8000
   ```
2. Capture on `lo` with filter `tcp port 8000`.
3. Request the page with `curl`, and send a POST with a **fake** password:
   ```bash
   curl http://127.0.0.1:8000/
   curl -d "user=test&pw=not-a-real-password" http://127.0.0.1:8000/login
   ```
   (the simple server will reject the POST with an error; the request is still in the capture)
4. In Wireshark: filter `http`, then Follow > HTTP Stream.

### Part B: HTTPS

1. Capture on your main interface, then load an HTTPS site.
2. Filter `tls.handshake.type == 1` and read the SNI.
3. Look at an `Application Data` packet: what can you read?

### Part C: decrypting your own browser traffic

1. Start your browser with a key log:
   ```bash
   SSLKEYLOGFILE=~/captures/sslkeys.log firefox
   ```
2. Wireshark: Preferences > Protocols > TLS > (Pre)-Master-Secret log filename.
3. Reload the capture; HTTP requests inside TLS should now be readable.
4. **Delete the key log and capture afterwards.** Neither goes in git.

## Things to find

- [ ] The POST body in cleartext in Part A
- [ ] The SNI (server name) in Part B
- [ ] The TLS version and cipher suite chosen
- [ ] What Part C revealed that Part B did not

## Observations

> Fill in after running.

## Analysis

> What does SNI leak even when the content is encrypted? What would Encrypted Client Hello change?

## What I learned

-
