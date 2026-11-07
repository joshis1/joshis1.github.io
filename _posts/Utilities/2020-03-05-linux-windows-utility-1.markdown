---
layout: post
title:  "Linux and Windows Utilities: Practical Notes, Part 1"
date:   2020-03-05 14:23:31 +1300
categories: Utilities
description: Practical notes on Linux and Windows utilities, with safer file-encryption guidance and command examples.
---

This article collects short answers to common Linux and Windows questions. The examples reflect the tools available when these notes were written; check local versions and options before using them.

## Encrypting a file

For new workflows, consider a maintained file-encryption tool such as `age`. If you use OpenSSL, use a current version and a strong passphrase. Avoid putting a passphrase directly on the command line, where it may be exposed in shell history or process listings. OpenSSL versions that support PBKDF2 can prompt for the passphrase:

{% highlight text %}
openssl enc -aes-256-cbc -salt -pbkdf2 -iter 600000 -in password.txt -out password.enc
{% endhighlight %}

Decrypt with the same options:

{% highlight text %}
openssl enc -d -aes-256-cbc -pbkdf2 -iter 600000 -in password.enc -out password.txt
{% endhighlight %}

AES is a symmetric cipher: the same secret is used to encrypt and decrypt. CBC mode does not authenticate the file, so successful decryption alone does not prove that the file has not been modified. Prefer an authenticated encryption format or a tool designed for file encryption when choosing a new workflow.

## Removing a directory with an unusual name

For file deletions, one trick is to wildcard as much of the name as you can, and use the -i (interactive) option to decide what subset of the matches to delete, one by one. The rmdir command does not have that, but the recursive file removal will deal with directories. E.g.

{% highlight text %}
rm -r -i -- AB*20191217-163059*
{% endhighlight %}

Review every prompt before confirming deletion. If the directory name begins with `-`, use `--` before it so it is not interpreted as an option.

## Using `-exec` with `find`

`-exec` is a `find` action that runs another command on each matching path.

**Example**

{% highlight text %}
find . -type f \( -iname '*.c' -o -iname '*.h' -o -iname '*.l' \) -exec grep -in 'test1' /dev/null {} \;
{% endhighlight %}

For C and header files only:

{% highlight text %}
find . -type f -iname '*.[ch]' -exec grep -in 'test1' /dev/null {} \;
{% endhighlight %}

`{}` is replaced with each matched path. The escaped semicolon closes the `-exec` action for `find` rather than the shell.

## Running a DHCP server on Windows

Here is the utility that I use in Windows10 to run my DHCP server.

[dhcp server](https://www.dhcpserver.de/cms/)

## Discovering active hosts on your own network

Nmap can help inventory hosts on a network you own or are authorized to administer. Keep the target range within that scope.

{% highlight text %}

sudo nmap -sn 11.11.11.1-254

Starting Nmap 7.40 ( https://nmap.org ) at 2020-03-29 22:59 PDT
Nmap scan report for 11.11.11.1
Host is up (-0.099s latency).
MAC Address: 00:1B:21:A7:62:44 (Intel Corporate)
Nmap scan report for 11.11.11.4
Host is up (0.00069s latency).
MAC Address: 78:45:01:05:98:40 (Unknown)
Nmap scan report for 11.11.11.3
Host is up.
Nmap done: 254 IP addresses (3 hosts up) scanned in 15.42 seconds 
{% endhighlight %}

## Searching files without recursing into directories
Here -d skip means skip looking into the directory.
Next -H means print the file names.
Generally, the '-d skip' is used with the find and exec.

{% highlight text %}
find ./ -exec grep -d skip -H 'asf' {} \;
{% endhighlight %}

## Increasing a virtual machine's disk size
Many times, you will realise that your virtual machine box needs more space then you have allocated previously.
I faced this issue while using yocto in my virtual machine running Ubuntu. Here is what I referred to increase
the size of my virtual machine box - 

[Enlarge Virtual Machine disk space](https://drive.google.com/open?id=1ZLMDLuKJZ9nKfB_6DXYVlBid0gCLYsS9)


This brings an end to this article. This article was just to touch some
common commands and utilities to address common problems or tasks.