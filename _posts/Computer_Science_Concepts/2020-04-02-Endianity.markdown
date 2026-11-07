---
layout: post
title:  "Byte Order (Endianness): Big-Endian vs Little-Endian"
date:   2020-04-02 14:13:31 +1300
categories: Computer_Science_Concepts
description: A practical explanation of byte order, how it affects multi-byte values, and why network protocols specify an encoding.
---

Endianness describes the order in which the bytes of a multi-byte value are stored in memory. It does not change the value itself; it describes how that value is represented across byte addresses.

## Big-endian and little-endian

Consider the 32-bit value `0x12345678`. If its first byte is stored at the lowest address:

| Byte address order | Bytes stored |
| --- | --- |
| Big-endian | `12 34 56 78` |
| Little-endian | `78 56 34 12` |

Big-endian stores the most significant byte at the lowest address. Little-endian stores the least significant byte there. Endianness applies to values made of multiple bytes; a single byte has no byte order.

Neither format is inherently more natural or universally faster. Processor architecture, instruction set, and workload determine performance. The byte order used to store an integer is separate from the way arithmetic is performed on that integer.

## Why byte order matters

Programs that exchange binary data need an agreed representation. If a sender and receiver interpret the same bytes using different byte orders, a multi-byte value can be decoded incorrectly. Text formats and protocols that define individual bytes avoid some ambiguity, but binary formats must specify field width, byte order, and often signedness as well.

Internet protocols commonly use **network byte order**, which is big-endian for multi-byte integer fields. In C, `htons` and `htonl` convert 16-bit and 32-bit values from host byte order to network byte order; `ntohs` and `ntohl` convert them back. These functions convert representation when needed and are effectively no-ops on hosts that already use network byte order. They do not convert an IP address string into an address; use the appropriate address-parsing API for that.

For portable file formats and network messages, prefer documented serialization APIs over copying a native integer's in-memory bytes. That makes the representation explicit and avoids assumptions about the machine running the code.

