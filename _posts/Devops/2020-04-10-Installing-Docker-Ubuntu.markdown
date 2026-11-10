---
layout: post
title: "Installing Docker Engine on Ubuntu"
description: "A historical Ubuntu walkthrough for installing Docker Engine and exploring storage drivers and containers."
date:   2020-04-10 16:23:31 +1300
categories: DevOps
---

This historical guide records an installation of Docker Engine on Ubuntu Bionic. The
commands, repository-key instructions, and package versions below are obsolete; follow
the current Docker documentation for a supported Ubuntu release instead.

## What is Docker Community Edition
The docker community edition is free and open source docker engine.It has pretty rich features. However,
Docker Enterprise edition has some additional features.
The Docker Enterprise edition is a paid one.

## Some of the features of Docker Engine
{% highlight text %}
1. Docker Swarm
2. Orchestration
3. Networking
4. Security
{% endhighlight %}

## How to install docker in ubuntu?
First update the repository.

{% highlight bash %}

$sudo apt-get update

{% endhighlight %}

Next install the required packages by Docker Community
Edition/Docker CE.

{% highlight bash %}
  $sudo apt-get -y install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common
{% endhighlight %}

The following legacy repository-key commands are retained only to document the original
setup. Do not copy them into a current installation; use Docker's current signed
repository instructions.
{% highlight bash %}
 $curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

$sudo apt-key fingerprint 0EBFCD88

{% endhighlight %}

Now, add docker CE into repository.
{% highlight bash %}
$sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

{% endhighlight %}

Now, let's update the repository. Also, let's install
the docker-ce, docker-ce cli and containerd.io.
This example pins Docker Engine 18.09.5 for Ubuntu Bionic, a release that is no longer
supported. Do not use this version for a new deployment.

{% highlight bash %}

$sudo apt-get install -y docker-ce=5:18.09.5~3-0~ubuntu-bionic docker-ce-cli=5:18.09.5~3-0~ubuntu-bionic containerd.io

{% endhighlight %}

Adding a user to the `docker` group avoids typing `sudo`, but grants privileges
equivalent to root on the host. Only add trusted users, and follow your organization's
container security policy.


{% highlight bash %}

$sudo usermod -a -G docker $(whoami)

{% endhighlight %}

Here -a stands for add and -G stands for group.
The group name is docker.

Now, you need to log out and log in so that affect of
usermod will take place.

Let's test the docker.

{% highlight bash %}

$docker run hello-world
{% endhighlight %}

Here is the reference

(https://docs.docker.com/install/linux/docker-ce/ubuntu/)

## Storage driver
When docker is not using mounted volume, it is using
the internal storage to read/write the file inside docker container. Docker supports storage driver framework. The storage driver framework provides a plugable framework for managing the temporary internal
storage of a container's writable layer.

## Types of Storage driver
{% highlight text %}
 1. Overlay2 - file based storage - default to ubuntu and debian
 2. devicemapper - block storage - default for Centos
{% endhighlight %}

Storage-driver performance depends on workload and configuration. Do not assume that
Device Mapper is faster; use a driver supported by the installed Docker Engine and
operating system.

## How to see what storage driver is used by docker engine
In order to check this, we need to run the following command.
{% highlight bash %}
 $docker info
{% endhighlight %}

Reference:
(https://docs.docker.com/storage/storagedriver/select-storage-driver/)

## How to overwrite the default storage driver?
There are two options to change the default storage
driver.

1. Using docker system unit file

{% highlight bash %}
 $sudo vi /usr/lib/systemd/system/docker.service

ExecStart=/usr/bin/dockerd --storage-driver devicemapper ...
{% endhighlight %}

Afterwards, reload the service.
{% highlight bash %}
sudo systemctl daemon-reload
sudo systemctl restart docker
{% endhighlight %}

2. Create a file daemon.json

Daemon configuration is generally preferable to editing a packaged systemd unit, but
the `devicemapper` example below is legacy and may not be supported by current
installations.
{% highlight bash %}
sudo vi /etc/docker/daemon.json

{
  "storage-driver": "devicemapper"
}
{% endhighlight %}

Now, restart the docker.

{% highlight bash %}
 $sudo systemctl restart docker
 $sudo systemctl status docker
{% endhighlight %}

## How to run a container?
reference - (https://docs.docker.com/engine/reference/run/)

{% highlight bash %}

docker run [options] IMAGE[:TAG] [COMMAND] [ARGS..]

IMAGE: The container image to run.

TAG: A specific image tag.

COMMAND - command to run inside the container.

ARG: Arguments to pass when running the command.

 This brings an end to this article.

{% endhighlight %}

Example of command and parameter.

{% highlight bash %}
$docker run busybox echo hello world!
echo is a command
hello world! is a parameter
{% endhighlight %}

Example, run a daemon nginx i.e. a webserver.
This webserver by default uses the port 80.
In this exaple, we will run the nginx version 1.15.11.

{% highlight bash %}
$docker run nginx:1.15.11
{% endhighlight %}

## How to run nginx in background?
In order to run nginx in background, we can use
detached mode i.e. run -d.

{% highlight bash %}
docker run -d nginx
{% endhighlight %}

## How to see all the containers running?
In order to see all the containers running, we can use
the following command.

{% highlight bash %}
 $docker ps
{% endhighlight %}

## How to stop the container?
{% highlight bash %}
$docker container stop <container id>
{% endhighlight %}

## Docker options - restart
We don't want some applications like webserver to die
forever when something bad happens. In fact, we would like such applications to restart. Here are some of the
restart options supported by docker.

{% highlight text %}
no
on-failure
always
unless-stopped
{% endhighlight %}

Here is one of the example,

{% highlight bash %}
 $docker run -d --name nginx --restart on-failure nginx
{% endhighlight %}

## How to expose container port to host?
Docker provides the option -p i.e. publish for this purpose. The syntax is

{% highlight text %}
 -p <host port>:<container port>
{% endhighlight %}

For example, port mapping for nginx -p 8080:80.
We can test this using the command.

{% highlight bash %}
curl localhost:8080
{% endhighlight %}

## How to automatically remove the container when it exits?
--rm is the option provided by docker for this purpose.
Note, --rm option cannot be used when restart option is used.

## How to hard limit the memory usage of docker?
--memory is the option. For e.g. we can hard limit the
docker memory option to 500Mb using the option.

--memory 500M.

## How to give an extra memory when the docker exhaust all the given memory?
--memory-reservation is used in that case. For e.g.,
we can say --memory-reservation 256M. This reserved memory will only be used when the docker consumes all of its allocated memory.

## How to see all the containers status i.e. even those who have stopped?
{% highlight bash %}
 $docker ps -a
{% endhighlight %}

## How to give name to the container?
--name option is used to give name to the container.

{% highlight bash %}
 $docker run -d --name nginx --restart on-failure nginx
{% endhighlight %}

## How to start and stop the container?
{% highlight bash %}
$docker container start nginx
$docker container stop nginx
$docker container rm nginx
{% endhighlight %}

This brings an end to this article.
