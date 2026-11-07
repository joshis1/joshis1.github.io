---
layout: post
title:  "Reading and Writing QSPI Flash with U-Boot on Zynq"
date:   2020-04-03 14:13:31 +1300
categories: Embedded_Linux
description: A historical Zynq U-Boot walkthrough for loading, writing, verifying, and booting kernel and device-tree images from QSPI.
---
This historical walkthrough records how I loaded a kernel and device tree from an SD card, wrote them to QSPI NOR flash with U-Boot, read them back for verification, and booted the kernel on a Zynq board. Confirm flash offsets, image sizes, and memory addresses for your hardware before running any write or erase command.

**What is the DRAM memory size?**
In order to find the DRAM memory size in uboot, we can run the following command.

{% highlight text %}

Zynq> bdinfo
arch_number = 0x00000000
boot_params = 0x00000000
DRAM bank   = 0x00000000
-> start    = 0x00000000
-> size     = 0x40000000
baudrate    = 115200 bps
TLB addr    = 0x3fff0000
relocaddr   = 0x3ff51000
reloc off   = 0x3bf51000
irq_sp      = 0x3eb2de10
sp start    = 0x3eb2de00
ARM frequency = 666 MHz
DSP frequency = 0 MHz
DDR frequency = 533 MHz
Early malloc usage: 5cc / 600
fdt_blob    = 0x3eb2de28

{% endhighlight %}

we can see that the size is 0x40000000 in hexadecimal.

**How do I convert the hexadecimal to memory size?**
Here given number is 0x4 0000000 i.e 0x4 and 7 zeroes.
So, hexadecimal is nothing but 4 bits representation or nibble you can say.
In our example, we have 7 zeroes or we can say it has 7*4 = 28 bits zero.
Now, 0x4 is nothing but 2^2. Thus, in total it is 2^2 * 2^28 = 2^30.
Now, 2^10 is kilobytes, 2^20 is Megabytes, 2^30 is 1 Gigabytes.
So, we have 1 Gigabytes RAM.

**List the directory contents of the SD card formatted in FAT**

{% highlight text %}

Zynq> fatls mmc 0
            System Volume Information/
    84104   boot.bin
  2083852   custom_ip.bit
   548898   u-boot.img
      957   uEnv.txt
  4162656   uImage
    11893   devicetree.dtb
            .Spotlight-V100/
            .fseventsd/

7 file(s), 3 dir(s)

{% endhighlight %}

**How to flash uImage to QSPI?**

The first thing here is to read the uImage from the FAT partition of sd card and load that image
into memory. In this example, we are loading the uImage i.e. kernel image from mmc 0 and storing the
uImage at memory address - 0x3000000 i.e 0x3 and 6 zeroes. 
The 6 zeroes is nothing but 6*4 = 24 bits or 2^24 and 0x3.
Next, we know that 2^20 is 1 Mb, so it is 2^4 * 0x3 = 48Mb. So, we are placing the UImage at the offset of 48Mbytes
in DRAM. 

{% highlight text %}
fatload mmc 0 0x3000000 ${kernel_image}
{% endhighlight %}

Now, flash the QSPI NOR 

Probe the SPI Nor.

{% highlight text %}
Zynq>  sf probe 0 0 0
SF: Detected s25fl128s_64k with page size 256 Bytes, erase size 64 KiB, total 16 MiB
{% endhighlight %}

We cannot directly onto QSPI Nor flash, first we need to erase the block and then only we can write the
data. So, let's first erase 8Mb for kernel image. I know this pretty big. In theory, my zedboard kernel image size is just a little over 4 Mb. So, 8 Mb is pretty safe. 

{% highlight text %}
sf erase 0 0x800000  //Erase 8MB from QSPI offset 0x0
{% endhighlight %}

Write the uImage i.e. kernel image to the QSPI.

{% highlight text %}
sf write 0x3000000 0 0x800000  //written to QSPI offset 0 and read from RAM memory 0x3000000
{% endhighlight %}

Now, let's readback the uImage from SPI NOR and store that uImage onto memory location - 
0x8000000 i.e. 0x8 and 6 zeroes. i.e. 2^3 and 6*4 = 24 or 2^24. This means 2^27 or 2^7 *2^20 = 128Mb.
So, now we are reading the uImage from QSPI and store at the memory location - 128Mb from the base address i.e 0x000. 

{% highlight text %}
sf read  0x8000000 0  0x800000  // read back into memory 0x8000000  -- kernel image read
{% endhighlight %}

Now, check wether the uImage is there in the memory address 0x8000000 or not.

{% highlight text %}

Zynq> md 0x8000000
00010000: 56190527 a7f99ceb 64ad585e 20843f00    '..V....^X.d.?.
00010010: 00800000 00800000 d52ee395 00020205    ................
00010020: 756e694c 2e342d78 302e3931 6c69782d    Linux-4.19.0-xil
00010030: 2d786e69 31303276 00312e39 00000000    inx-v2019.1.....
00010040: e1a00000 e1a00000 e1a00000 e1a00000    ................
00010050: e1a00000 e1a00000 e1a00000 e1a00000    ................
00010060: ea000005 016f2818 00000000 003f8420    .....(o..... .?.
00010070: 04030201 45454545 00003460 e10f9000    ....EEEE`4......
00010080: eb000bf6 e1a07001 e1a08002 e10f2000    .....p....... ..
00010090: e3120003 1a000001 e3a00017 ef123456    ............V4..
000100a0: e10f0000 e220001a e310001f e3c0001f    ...... .........
000100b0: e38000d3 1a000004 e3800c01 e28fe00c    ................
000100c0: e16ff000 e12ef30e e160006e e121f000    ..o.....n.`...!.
000100d0: e16ff009 00000000 00000000 00000000    ..o.............
000100e0: e1a0400f e204433e e2844902 e1a0000f    .@..>C...I......
000100f0: e1500004 359f01b0 3080000f 31540000    ..P....5...0..T1

{% endhighlight %}

Similarly, read the device tree.

**Load device tree from FAT**

{% highlight text %}

fatload mmc 0 0x2A00000 ${devicetree_image}

{% endhighlight %}

**Flash device tree into QSPI**

Since, we have already consumed first 8Mb from QSPI for uImage purpose, we should write the
device tree after 8Mb in QSPI. Thus, the offset should be 8Mb.

**Erase 4Mb for device tree into QSPI**
{% highlight text %}
sf erase 0x800000  0x400000 //erase 4MB for Device Tree
{% endhighlight %}

**Flash/write device tree into QSPI**
{% highlight text %}
sf write 0x2A00000 0x800000  0x400000  //written to QSPI from RAM memory 0x2A00000
{% endhighlight %}

**Readback device tree from QSPI into different memory location**

Previously, we have read uImage into memory space - 128Mb and as I know my kernel size is not more than 5Mb.
Thus, any memory address 128Mb + 5Mb = 133Mb should be fine. Here, I have taken the memory address - 
140Mb. Thus, 140 Mb is nothing 0x8C and 5 zeroes. The 0x8C equals to 140 in decimal. 

**Flash/write device tree into QSPI**
{% highlight text %}
sf read  0x8C00000 0x800000 0x400000 //device tree read from QSPI offset 0x800000 and how much to read i.e. 0x400000 ~ 4Mb read.
{% endhighlight %}

**Verify the device tree image using memory dump**
{% highlight text %}

Zynq> md 0x8C00000
00180000: edfe0dd0 752e0000 38000000 302a0000    .......u...8..*0
00180010: 28000000 11000000 10000000 00000000    ...(............
00180020: 45040000 f8290000 00000000 00000000    ...E..).........
00180030: 00000000 00000000 01000000 00000000    ................
00180040: 03000000 04000000 00000000 01000000    ................
00180050: 03000000 04000000 0f000000 01000000    ................
00180060: 03000000 36000000 1b000000 656e7661    .......6....avne
00180070: 797a2c74 6d2d716e 6f726369 0064657a    t,zynq-microzed.
00180080: 786e6c78 6e797a2c 696d2d71 7a6f7263    xlnx,zynq-microz
00180090: 78006465 2c786e6c 716e797a 3030372d    ed.xlnx,zynq-700
001800a0: 00000030 03000000 15000000 26000000    0..............&
001800b0: 656e7641 694d2074 5a6f7263 62206465    Avnet MicroZed b
001800c0: 6472616f 00000000 01000000 73757063    oard........cpus
001800d0: 00000000 03000000 04000000 00000000    ................
001800e0: 01000000 03000000 04000000 0f000000    ................
001800f0: 00000000 01000000 40757063 00000030    ........cpu@0...

{% endhighlight %}

**Boot kernel image**
The command here is bootm "uImage address"  "rootfs address if you have otherwise put -"  "device tree address".
In my case, I don't have rootfs address. Thus, I am putting '-'.

{% highlight text %}
bootm 0x8000000 - 0x8C00000
{% endhighlight %}

**How to run elf image using uboot**
Similar to bootm, you can use bootelf to run an elf executable.
Suppose an elf is stored at the memory address 0x1000000.

{% highlight text %}
 bootelf 0x1000000
{% endhighlight %}

This brings an end to this article.