---
layout: post
title:  "Bringing Up Avnet MicroZed Linux with Yocto"
date:   2020-02-02 14:13:31 +1300
categories: Embedded_Linux
description: A historical Yocto Warrior walkthrough for building and booting Linux on an Avnet MicroZed Zynq board.
---

This historical walkthrough records the steps I used to build U-Boot, a Linux kernel, a device tree, and a root filesystem for an Avnet MicroZed Zynq-7010 board using Yocto Warrior.
Also, I will touch on how to create the fpga bit stream to program the Programming logic(PL). I have no experience in fpga but I would like to touch the fpga bit stream topic for the sake of completeness. Basically, a fully functional system where we can do tweaks later on. This is all about setting up the foundation to load the operating environment on the Avnet microZed using sd card/mmc. The model name is  Z7MB-7z0x0-ASY.  

<img src="/assets/img/AVNET_Zedboard.png" alt="MicroZed Zynq AVNET">

**Motivation to do this?**

I don't want to use Petalinux which abstracts a lot of details from the user. Instead, I would like to use Yocto build system. 
Here, in this blog, I am using warrior release of yocto.

**Setup** - I am using Ubuntu 18.04 on Windows 10 host machine.
I had a little bit of trouble finding what version of virtual box works with Ubuntu 18.04. I found that the version Virtual box 6.1.2 running guest OS - Ubuntu 18.04 works well on Windows 10 host machine.
Here is the link - [virtualboxForum](https://forums.virtualbox.org/viewtopic.php?f=6&t=97052)  Make sure you install the guest additions too for 6.1.2. Before you run the Guest Addition program, ensure you have installed the build-essential linux-headers-generic. Also, you might have to install build-essential gcc make perl dkms. I have given 50Gb to create Ubuntu virtual machine that should be sufficient to build the entire operating environment for microZed board.

**Pre-requisite**

Install the essentials in order to use Yocto.

[Yocto](https://www.yoctoproject.org/docs/1.8/yocto-project-qs/yocto-project-qs.html)

**Ubuntu and Debian**
The essential and graphical support packages you need for a supported Ubuntu or Debian distribution are shown in the following command:

{% highlight text %}

	 $sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib \
     build-essential chrpath socat cpio python python3 python3-pip python3-pexpect \
     xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev \
     pylint3 xterm

{% endhighlight %}

**Create your workspace.**
{% highlight text %}

$ mkdir -p microzed
$cd microzed

git clone -b <branch> <remote_repo>

{% endhighlight %}

The branch I am going to use here is Warrior. Checkout Poky - Warrior.

{% highlight text %}

git clone -b warrior git://git.yoctoproject.org/poky   

cd poky <Get inside the poky folder

{% endhighlight %}

**Layers we are using**

{% highlight text %}

a) meta-openembedded  and what it provides - read README -  [meta-openembedded](https://github.com/openembedded/meta-openembedded/blob/master/README)
b) meta-sourcery  and what it provides - read README - [meta-sourcery](https://github.com/MentorEmbedded/meta-sourcery/blob/master/README.md)
c) u-boot-xlnx  and it provides u-boot - read README - [u-boot-xlnx](https://github.com/Xilinx/u-boot-xlnx/blob/master/README)
d) meta-ezynq and it provides - read README - [meta-ezynq](https://github.com/Elphel/meta-ezynq/blob/master/README.md)
d) meta-external-toolchain and it is needed by meta-sourcery. 
e) meta-xilinx and it provides the definition for the machine microzed-zynq7 - read README - [meta-xilinx](https://github.com/Xilinx/meta-xilinx/blob/master/README.md)

{% endhighlight %}

Inside the poky folder, checkout these layers.

{% highlight text %}

1)git clone -b warrior https://github.com/openembedded/meta-openembedded.git
2)git clone -b warrior https://github.com/MentorEmbedded/meta-sourcery.git
3)git clone -b master https://github.com/Xilinx/u-boot-xlnx.git  
4)git clone -b warrior https://github.com/Elphel/meta-ezynq.git
5)git clone -b warrior git://git.yoctoproject.org/meta-external-toolchain
6)git clone -b warrior https://github.com/Xilinx/meta-xilinx.git

{% endhighlight %}

**Initialize the build**

This source command will create a build directory and will cd into build directory. The build directory will have the template for local.conf and bblayers.conf.
Here is the command.

{% highlight text %}

a) cd poky 
b) source oe-init-build-env 

{% endhighlight %}

Let's edit bblayers.conf to add layers to the recipe.

{% highlight text %}

$kate conf/bblayers.conf 
# POKY_BBLAYERS_CONF_VERSION is increased each time build/conf/bblayers.conf
# changes incompatibly
POKY_BBLAYERS_CONF_VERSION = "2"

BBPATH = "${TOPDIR}"
BBFILES ?= ""

BBLAYERS ?= " \
  ${TOPDIR}/../meta \
  ${TOPDIR}/../meta-poky \
  ${TOPDIR}/../meta-yocto-bsp \
  ${TOPDIR}/../meta-openembedded/meta-oe \
  ${TOPDIR}/../meta-external-toolchain \
  ${TOPDIR}/../meta-sourcery\
  ${TOPDIR}/../meta-ezynq\
  ${TOPDIR}/../meta-xilinx/meta-xilinx-bsp \
  "
{% endhighlight %}

Now, edit local.conf to tell what machine architecture we are building for.

{% highlight text %}

$kate conf/local.conf 
MACHINE ?= "microzed-zynq7"
{% endhighlight %}

Now, you are good to go. Let's build the Secondary Program Loader (SPL) u-boot image. The SPL image replaces the need for first stage boot loader i.e. fsbl.

**Build U-Boot**
This will create boot.bin, u-boot.img.

{% highlight text %}

$ bitbake virtual/bootloader
{% endhighlight %}

**Build minimal working uImage, dtb and rootfile system**
{% highlight text %}
$bitbake core-image-minimal
{% endhighlight %}

This is how it looks on the terminal.

<img src="/assets/img/bitbake.png" alt="bitbake">

**Generating fpga bit stream for microZed.**

In order to build fpga bit stream, we will use Vivado. I have installed 
Vivado on my Windows 10 machine. 

By default, Vivado doesn't have board files for microzed zynq 7010 from AVNET. So, we need to download the board files of microzed zynq7. Here is the link to download the board files. If the link doesn't exist then you can also do a google search for microzed-zynq7 board files. 

Some people use Xilinx Vitis IDE to generate FPGA program. The most popular language for 
FPGA is VHDL. [Vitis](https://www.xilinx.com/products/design-tools/vitis.html)


[zynq-microzed-7010x-board-definition](http://zedboard.org/content/board-definition-files-0)

Copy the board definition files at the location - 

{% highlight text %}
C:\Xilinx\Vivado\2018.1\data\boards\board_files
{% endhighlight %}

or if you are not a regular Windows OS user, then you can use this link for reference [Vivado_Board_File_Installation](https://www.youtube.com/watch?v=n7A0_twGPlI)

Now, you should be able to select the board for Zynq-7010x.
I have followed this tutorial to generate the bitstream 

[creating basic fpga program](http://www.fpgadeveloper.com/2014/07/creating-a-base-system-for-the-zynq-in-vivado.html)

Here is my fpga project. 

[My FPGA project](https://github.com/joshis1/avnet_microzed_fpga.git)

Once you run it, Vivado generates the bit file in runs\impl_1 folder in the project directory.

**Prepare hardware system**

{% highlight text %}

1) Setup the Jumper settings accurately to do sdboot 

Follow this - [AVNET Getting Started](http://zedboard.org/sites/default/files/documentations/MicroZed_GettingStarted_v1_0.pdf )

see Page 11.

2) Prepare sd card.

a) Partition the sd card into two partition.

i) FAT 32 - maximum 800 MB is good enough.
ii) EXT4 -  Rest of the sd card space.

{% endhighlight %}

I use gpart application to do the partitiion. You need to enable USB in the virtual box. You might need to restart the virtual box after enabling the usb device.

Now copy, boot.bin, devicetree.dtb, u-boot.img uEnv.txt and uImage in the FAT partitiion. Also, if you have created the fpga bit stream then you could copy the fpga bit stream here.

boot.bin is the SPL image and it will look for u-boot.img. 
u-boot.img will look for devicetree.dtb to set parameters for the kernel. For e.g, what clock rate, i2c devices the board needs is all defined in the devicetree. uImage i.e Kernel will refer to the device tree in order to configure and probe the required drivers. When the kernel starts, it reads this file (called dtb for Device Tree Binary) to know the devices on the board, and initialize useful drivers. Basically, SPL image uses PS7 i.e. processor system 
ps7_init.c and ps7_init.h from the xilinix board. In case you are not using microzed zynq, then you might need to 
generate ps7_init.c and ps7_init.h using xilinix tool. Next, you need to copy these files to uboot-xilinx.
The PS7_init.c does a lot of things like - resetting the SLCR - System level control registers and rom boot loader.
It starts by resetting the processor. 

**Copy Root File System**

Mount EXT4 to some <mountpoint>
unpack the rootfs.tar.gz

{% highlight text %}

tar -C <mountpoint> -xzpf rootfs.tar.gz

{% endhighlight %}

**Poking with u-boot environment.**

By default, my system had the following sdboot value.

{% highlight text %}

sdboot=echo Copying Linux from SD to RAM... && mmcinfo && run mmc_loadbit_fat && fatload mmc 0 0x3000000 ${kernel_image} 
&& fatload mmc 0 0x2A00000 ${devicetree_image} && fatload mmc 0 0x2000000 ${ramdisk_image} && bootm 0x3000000 0x2000000 0x2A00000

{% endhighlight %}

ramdisk_image=uramdisk.image.gz

Here you can see, it is trying to boot the ramdisk image i.e. rather than mounting the root file system, it's going to load the root file system on the RAM.

By the way, when you build, you must be wondering where is uramdisk.image.gz. Basically uramdisk.image.gz is nothing but 

{% highlight text %}

"uramdisk.image.gz" is just another name for "*.cpio.gz.u-boot"

{% endhighlight %}

So, if you don't want to mount ext4 partitiion, you can use ramdisk_image. Otherwise, you can change the sdboot to

{% highlight text %}
setenv sdboot 'echo Copying Linux from SD to RAM...  && mmcinfo && run mmc_loadbit_fat && fatload mmc 0 0x3000000 ${kernel_image}  && fatload mmc 0 0x2A00000 ${devicetree_image} && bootm 0x3000000 - 0x2A00000'
{% endhighlight %}

**Loading the fpga bit stream**

I have given a name to the fpga bit stream as custom_ip.bit here.
{% highlight text %}
fatload mmc 0 ${loadbit_addr} custom_ip.bit
fpga loadb 0 ${loadbit_addr} $filesize
{% endhighlight %}

**Setting the u-boot environment**
{% highlight text %}
setenv mmc_loadbit_fat 'echo Loading bitstream from SD/MMC/eMMC to RAM.. && mmcinfo && fatload mmc 0 ${loadbit_addr} ${bitstream_image} && fpga loadb 0 ${loadbit_addr} ${filesize}'
{% endhighlight %}

Please note that I am using fpga loadb in order to load the bitstream.
There is no translation required in order to load the fpga bitstream generated from Vivado.

**EXT4 Root File System**

**Telling uboot to mount the rootfile system from where?**

This is to identify from where kernel should mount the root file system.

In my case, I did the following in my u-boot.

{% highlight text %}

Zynq> mmc part

Partition Map for MMC device 0  --   Partition Type: DOS

Part    Start Sector    Num Sectors     UUID            Type
  1     2048            1433600         f2ccc02a-01     0b Boot
  2     1435648         6133760         f2ccc02a-02     83

{% endhighlight %}


In this example, the partition table identifies the EXT4 root filesystem as `/dev/mmcblk0p2`. `mmcblk0` is the first MMC device and `p2` is its second partition. Confirm the partition number on your own card; it must match the partition table.

Now, set the u-boot environment variable bootargs, which eventually is passed to the kernel.
Kernel uses this environment variable to set the console, root file system and other parameters.

{% highlight text %}
set bootargs earlyprintk console=ttyPS0,115200 root=/dev/mmcblk0p2 rw rootwait devtmpfs.mount=1
{% endhighlight %}

There are many commands supported by the u-boot. Here is the help.

{% highlight text %}

Zynq> help
?       - alias for 'help'
base    - print or set address offset
bdinfo  - print Board Info structure
blkcache- block cache diagnostics and control
boot    - boot default, i.e., run 'bootcmd'
bootd   - boot default, i.e., run 'bootcmd'
bootefi - Boots an EFI payload from memory
bootelf - Boot from an ELF image in memory
bootm   - boot application image from memory
bootp   - boot image via network using BOOTP/TFTP protocol
bootvx  - Boot vxWorks from an ELF image
bootz   - boot Linux zImage image from memory
clk     - CLK sub-system
cmp     - memory compare
coninfo - print console devices and information
cp      - memory copy
crc32   - checksum calculation
dcache  - enable or disable data cache
dfu     - Device Firmware Upgrade
dhcp    - boot image via network using DHCP/TFTP protocol
dm      - Driver model low level access
echo    - echo args to console
editenv - edit environment variable
env     - environment handling commands
exit    - exit script
ext2load- load binary file from a Ext2 filesystem
ext2ls  - list files in a directory (default /)

{% endhighlight %}

You can view the current environment variables using the following command.

{% highlight text %}

Zynq> printenv
baudrate=115200
bitstream_image=custom_ip.bit
bitstream_size=0x3DBAFC
bootargs=earlyprintk console=ttyPS0,115200 root=/dev/mmcblk0p2 rw rootwait devtmpfs.mount=1
bootcmd=run $modeboot
bootdelay=3
devicetree_image=devicetree.dtb
devicetree_size=0x20000
ethact=Gem.e000b000
ethaddr=00:0a:35:00:01:22
fdt_high=0x20000000
fdtcontroladdr=3eb2de28
fileaddr=100000
filesize=1fcc0c
initrd_high=0x20000000
ipaddr=11.11.11.103
jtagboot=echo TFTPing Linux to RAM... && tftp 0x3000000 ${kernel_image} && tftp 0x2A00000 ${devicetree_image} && tftp 0x2000000 ${ramdisk_image} && bootm 0x3000000 0x2000000 0x2A00000
kernel_image=uImage
kernel_size=0x500000
loadbit_addr=0x100000
mmc_loadbit_fat=echo Loading bitstream from SD/MMC/eMMC to RAM.. && mmcinfo && fatload mmc 0 ${loadbit_addr} ${bitstream_image} && fpga loadb 0 ${loadbit_addr} ${filesize}
modeboot=sdboot
nandboot=echo Copying Linux from NAND flash to RAM... && nand read 0x3000000 0x100000 ${kernel_size} && nand read 0x2A00000 0x600000 ${devicetree_size} && echo Copying ramdisk... && nand read 0x2000000 0x620000 ${ramdisk_size} && bootm 0
x3000000 0x2000000 0x2A00000
nfsdir=/home/shreyas/zynq
norboot=echo Copying Linux from NOR flash to RAM... && cp 0xE2100000 0x3000000 ${kernel_size} && cp 0xE2600000 0x2A00000 ${devicetree_size} && echo Copying ramdisk... && cp 0xE2620000 0x2000000 ${ramdisk_size} && bootm 0x3000000 0x200000
0 0x2A00000
othbootargs=init=/bin/bash
qspiboot=echo Copying Linux from QSPI flash to RAM... && sf probe 0 0 0 && sf read ${loadbit_addr} 0xC00000 ${bitstream_size} && mw 0xF8007080 0x30800100 0x4 && fpga load 0 ${loadbit_addr} ${bitstream_size} && sf read 0x3000000 0x100000 
${kernel_size} && sf read 0x2A00000 0x600000 ${devicetree_size} && echo Copying ramdisk... && sf read 0x2000000 0x620000 ${ramdisk_size} && bootm 0x3000000 0x2000000 0x2A00000
ramdisk_image=uramdisk.image.gz
ramdisk_size=0x5E0000
sdboot=echo Copying Linux from SD to RAM...  && mmcinfo && run mmc_loadbit_fat && fatload mmc 0 0x3000000 ${kernel_image}  && fatload mmc 0 0x2A00000 ${devicetree_image} && bootm 0x3000000 - 0x2A00000
serverip=11.11.11.3
silent=n
stderr=serial@e0001000
stdin=serial@e0001000
stdout=serial@e0001000

{% endhighlight %}

<img src="/assets/img/uboot_putty.png" alt="Uboot - SPL">

U-Boot runs code placed in (processor's) RAM,  although it can also read data from other media. The boot process normally takes place in two steps:

{% highlight text %}

1) Reading the OS image from media (Ethernet, flash, USB, MMC) into RAM
2) Jumping to the first instruction of the image in RAM

{% endhighlight %}

In order to read an image from an MMC card formatted in FAT, 
the command is:

{% highlight text %}
fatload mmc <dev>[:partition] <loadAddress> <bootfilename>
{% endhighlight %}

**bootm**
This command starts a kernel image running.
{% highlight text %}
bootm <address of kernel> <address of ramdisk> <address of dtb>
{% endhighlight %}

In our case, we are not using ramdisk so '-' in the middle.

{% highlight text %}
bootm <address of kernel> - <address of dtb>
{% endhighlight %}

Here is the entire system.

<img src="/assets/img/Kernel_booting.png" alt="Kernel_booting">

Here is the root file system mounted.

<img src="/assets/img/root_file_system.png" alt="Root file System Mounted">

**FSBL based**

Instead of SPL image, you can use FSBL too. In order to generate 
FSBL, you need to use Xilinx SDK. Also, I will suggest that it is a better idea to enable FSBL_DEBUG_INFO in order to see whether FSBL is working or not. Here is how you enable the FSBL_DEBUG_INFO in order to troubleshoot the FSBL based image. I haven't tried building up the entire system using FSBL. However, I was able to load the FSBL image successfully. Personally, I recommend to use SPL rather than FSBL.

<img src="/assets/img/fsbl_build_settings.png" alt="FSBL Build Settings">

<img src="/assets/img/fsbl_debug_info.png" alt="FSBL Debug Info">

Here is the link to download the tutorial for FSBL based AVNET ZYNQ-7010.

[FSBL_Tutorial](https://drive.google.com/open?id=1RjMOyBuzkphg4NjYy28krqLvtYS29rfD)


I strongly suggest to use SPL image rather than FSBL since if you get
stuck with something then you have no support but to use peta-linux
only.

Here is the link to download the [ZedboardImage](https://drive.google.com/open?id=10LsddxTvGmLnEsdgI-SYKYGNvOzIK-zc).

Here are the jumper settings to change the boot mode to JTAG, QSPI or SD Card.

<img src="/assets/img/ZEDBOARD_JUMPER_SETTINGS.png" alt="Zedboard Jumper Settings">

Also, you can read the entire guide on setting.

[Zedboard reference guide](https://drive.google.com/open?id=1UcFAOTKosQ9m8bufOg3s5oGMPxCNyaVF)


This brings an end to this article. Here is the entire embedded system running.

