---
title: "Something isn't working — what do I do?"
app: srtstreamtester
category: help
order: 1
tags: "error, not working, can't connect, failed, rejected, wrong passphrase, busy, no reply, no video, black screen, camera permission, microphone permission, gray, support, contact, help"
quick: "Read the red line under the Connect button — it names the problem and what to change. Still stuck? Email support."
related:
  - watch-a-stream
  - send-my-camera
  - read-the-numbers
---

## The button is greyed out

- **Caller mode needs a host to dial.** Type the Host.
- **Port must be 1–65535.**
- **SRT passphrases must be 10–79 characters.**

## It won't connect

The app says why under the button and in the **Event Log**.

- **Wrong passphrase.** Check it with whoever runs the receiver.
- **Passphrase on one side only.** Set the same one on both, or clear both.
- **The receiver said no.** It may need a certain **Stream ID**, or it is full.
- **The receiver is busy.** Disconnect the other caller and try again.
- **Can't find** the host. Check the spelling, or use the IP address.
- **Nothing is listening on port …** Check the port, and that the receiver is started.
- **No reply at all.** The receiver is busy, a firewall blocks UDP, or the address is wrong.
- **This device's network failed.** Check Wi-Fi or cellular.

## Connected, but something is wrong

- **Peer disconnected** — the other end hung up. Connect again.
- **Packets arriving but not decrypting** — the passphrases do not match.
- **Nothing is arriving** — check the other end is actually sending.
- **Heavy packet loss** or **latency below 4×RTT** — raise **Latency**.

## Part of the picture is gray

- **The sender uses multi-slice H.264.** Only one slice shows.
- **Fix on the encoder:** turn off sliced threads (x264: `sliced-threads=0`).

## Sending: no camera or sound

- **Camera permission denied** — turn on Camera for SRT Tester in Settings.
- **Microphone permission denied** — turn on Microphone for SRT Tester in Settings.

## Contact support

- **Email** [{{ site.support_email }}](mailto:{{ site.support_email }}).
- **Include** the red message, and the **Event Log** lines if you can.
