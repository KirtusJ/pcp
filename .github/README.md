# Parrot Council Protocol and PCP OS | pre-publication build

This repository contains pre-publication build 19 of the [PCP 1.0 Enterprise Edition](../README.md), its two assistant plugins, and bootable PCP OS media.

## Boot PCP OS in a virtual machine

**The published `PCP-OS.iso` is for virtual machines only. Attach only the read-only CD. Leave hard disks, USB storage and network adapters disconnected from the guest.** On QEMU PC and Q35, the published ISO wrote 512 bytes to sector zero of an attached disposable disk before the launcher appeared. [Disk test results](https://github.com/KirtusJ/pcp-os/pull/276#issuecomment-7057938081)

For a first boot, use the [source-built BIOS tester and launch instructions](../audit/public-live-cd/candidates/source-bios/README.md). To reproduce the published 0.3.1 demo, follow the [published ISO checksum and CD-only boot command](../audit/public-live-cd/README.md). For a queue that survives shutdown, the [two-app VM workspace](../audit/vm-workspace/README.md) creates its own dedicated data disk.

## Use the Enterprise Edition

The [edition overview](../README.md) lists the specifications, reader guides, tools and license. The [edition guide](../EDITION_GUIDE.md) explains how to start a review.

## Verify the edition

In a Linux x86-64 Git checkout, run `python3 audit/enterprise-checkout/check.py HEAD` from the repository root. It checks the committed edition in three fresh checkouts and tests both plugin copies. In an extracted, standalone edition directory, run `python3 verify_edition.py` there. [Repository check](../audit/enterprise-checkout/check.py) · [Edition identity](../EDITION.json)
