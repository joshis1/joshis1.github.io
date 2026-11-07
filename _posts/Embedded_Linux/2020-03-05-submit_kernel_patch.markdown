---
layout: post
title:  "Submitting My First Linux Kernel Patch"
date:   2020-03-05 15:23:31 +1300
categories: Embedded_Linux
description: Notes from preparing, revising, and emailing a first Linux kernel patch, including historical workflow caveats.
---

This is all about my journey to submit my first kernel patch. Here I have discussed all the important things you must know before you submit your kernel patch and also respond to the feedbacks.

**How to check code style before submitting the patch?**

Kernel community uses a very different coding style and is a bit different. But, what they have done is that they have created a script to check the coding style before we send the code for review.

For e.g, if you have changed the file - da9062-core.c

{% highlight text %}
perl scripts/checkpatch.pl  -f drivers/mfd/da9062-core.c
{% endhighlight %}

In order to run checkpatch.pl, you need to install a few python modules.

{% highlight text %}
$sudo apt-get install python-pip
$pip install gitpython
{% endhighlight %}

Sometimes, I get an error that my pip version is older and I need to upgrade it. The best way to upgrade pip version is to not use sudo command but the following command.

{% highlight text %}
 $pip install --upgrade --user pip
{% endhighlight %}
 
Since python packages are used by Operating system too. If we use sudo then it will interfere with the OS python packages and it might overwrite them. This will lead to system not working. Instead of installing for system we should install for the user. 

Another way of installing pip package is 

**using virtual environment.**

{% highlight text %}
$sudo apt install virtualenv

$virtualenv venv

$source venv/bin/activate

$virtualenv -p /usr/bin/python2.7 venv

{% endhighlight %}

**How to commit your changes?**

One need to sign-off using git commit -s.
By signing, you agree with the kernel policies.

{% highlight text %}

$git commit -s 

{% endhighlight %}

**How to give git commit message?**

{% highlight text %}

 mfd: da9062: add support for interrupt polarity defined in device tree
    
 The da9062 interrupt handler cannot necessarily be low active.
 Add a helper function to read the polarity defined in the device tree.
 Based on the user defined polarity in device tree, the interrupt is set active.
 
{% endhighlight %}
 
Here mfd:da9062 is the file showing drivers/mfd/da9062-core.c

In case, you are not happy about your commit, you can again commit the code using.

{% highlight text %}

$git commit --amend <files update>

{% endhighlight %}

**How to generate a patch file?**

{% highlight text %}

$git format-patch HEAD~<number of commits to convert to patches>

{% endhighlight %}

**How to add revision history?**

Generally the maintainers are quite keen to see the revision history as it helps them to review. It is best to hand modify the file generated from ‘git format-patch” to add the version history to the patch. It is not part of the commit message and should go below the ‘---’ line and above the information regarding the files touched by the patch and the number of changes, so in my case:

{% highlight text %}

The da9062 interrupt handler cannot necessarily be low active.

Add a function to configure the interrupt type based on what is defined in the device tree.
The allowable interrupt type is either low or high level trigger.

Signed-off-by: XX <xx@xx.com>

---

V3:

     Fixed issue with ….

V2:

     Updates relating to ……

drivers/mfd/da9062-core.c | 43 ++++++++++++++++++++++++++++++++++++---

1 file changed, 40 insertions(+), 3 deletions(-)

{% endhighlight %}

**How to see maintainers list for the changes you made?**

{% highlight text %}

$perl scripts/get_maintainer.pl  <patch file>

{% endhighlight %}

**How to apply the patch file?**

The patch file can be applied using the command.

{% highlight text %}

$git am <patchfile>

{% endhighlight %}

**How to use git send-email?**

Install git-email

{% highlight text %}
$sudo apt-get install git-email
{% endhighlight %}


**How to find the messageID of the email in order to reply.**

Please refer to this link.
(message id)[https://www.codetwo.com/kb/messageid/]

**How to setup the git email client**

Setting up an email client

{% highlight text %}
~/.gitconfig
[sendemail]
  ; setup for using git send-email; prompts for password
  smtpuser = myemailaddr@gmail.com
  smtpserver = smtp.googlemail.com
  smtpencryption = tls
  smtpserverport = 587
{% endhighlight %}


**Example to send the patch -**
{% highlight text %}
$git send-email  --cc linux-kernel@vger.kernel.org  C:\Users\xx\Documents\0001-mfd-da9062-Add-support-for-interrupt-polarity-def.patch
{% endhighlight %}


**Example to re-send the patch, basically replying on to the email using revised patch.**

{% highlight text %}
$git send-email  --cc linux-kernel@vger.kernel.org --in-reply-to AM6PR10MB22635CBCBF559AEB9A5C2BFF80120@AM6PR10MB2263.EURPRD10.PROD.OUTLOOK.COM C:\Users\xx\Documents\0001-mfd-da9062-Add-support-for-interrupt-polarity-def.patch
{% endhighlight %}


There is another email client called - mutt, but I won't suggest using mutt because it needs you to turn off the secure settings from your mail server like "allow less secure apps"

Here is the mutt.rc settings

{% highlight text %}
set ssl_starttls=yes
set ssl_force_tls=yes
set imap_user = 'email@gmail.com'
set imap_pass = 'XXXX' --> set Password here.
set from='email-address'
set realname='XXX'
set folder = imaps://imap.gmail.com/
set spoolfile = imaps://imap.gmail.com/INBOX
set postponed="imaps://imap.gmail.com/[Gmail]/Drafts"
set header_cache = "~/.mutt/cache/headers"
set message_cachedir = "~/.mutt/cache/bodies"
set certificate_file = "~/.mutt/certificates"
set smtp_url = 'smtp://<email-id>@smtp.gmail.com:587/'
set smtp_pass = $imap_pass
set move = no
set imap_keepalive = 900
{% endhighlight %}

**Setting up your local environment to show the git branch?**

This is pretty helpful and it will save your time. After this you don't have to run 'git branch' to know what branch you are working at. Add this line to your bash.rc in order to see what branch you are working in?

{% highlight text %}
PS1="\u@\h\[\033[00m\]:\[\033[01;36m\]\w\[\033[00m\]\[\033[01;34m\]\$(git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/')\[\033[00m\]\$"
{% endhighlight %}

Here is the output and you can see that I am onto the warrior branch.

<img src="/assets/img/git_warrior_branch.png" alt="git branch on the shell">

Useful links

[kernel patches](https://lore.kernel.org/patchwork/project/lkml/list/)

This brings an end to this article. It's a good idea to give back to the open source community like linux kernel.