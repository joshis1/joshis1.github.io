---
layout: post
title:  "Adding Packages to a Yocto Image"
date:   2020-04-03 18:13:31 +1300
categories: Embedded_Linux
description: A short, version-specific note on finding recipes and adding packages to a Yocto image.
---

This short, historical note shows how I added packages to a Yocto image. Recipe names and override syntax vary by Yocto release; this example is from the Warrior-era setup.
For e.g, I would like to add curl and node js package in Yocto.

**Check whether those packages are already available or not**
The best thing is to check whether those packages already exist or not.
For e.g. run the command bitbake-layers show-recipes and redirect its output to a file.
Next, open your favourite editor and find the package. There is a good chance it is already
available and its the matter of compiling and installing that package to your root file system.

{% highlight text %}

$bitbake-layers show-recipes  > recipes.txt

{% endhighlight %}

Also, you can check using the following link -

[packages](http://layers.openembedded.org/layerindex/branch/warrior/layers/?)

**How to add those packages to your root file system**

First define in local.conf file what packages you would like to install.

{% highlight text %}
 
 WEB_PACKAGES = " \
  curl \
  nodejs \
"
{% endhighlight %}

Next append those packages.

{% highlight text %}
IMAGE_INSTALL_append = " ${WEB_PACKAGES}"
{% endhighlight %}


Now, build your image again.

{% highlight text %}
$bitbake core-image-minimal
{% endhighlight %}

Now, your root file system should have those packages - nodejs and curl.

This brings an end to this article.