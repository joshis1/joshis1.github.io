---
layout: post
title: "Managing Docker Versions and Logging Drivers"
description: "Historical Ubuntu examples for Docker package versions and configuring container logging drivers."
date:   2020-04-11 17:23:31 +1300
categories: DevOps
---
This historical Ubuntu walkthrough covers Docker package versions and logging drivers.
Package versions, repository configuration, and supported drivers depend on the Docker
Engine and Ubuntu releases in use.

## Downgrade docker
1. First stop the docker
2. Remove the Docker packages without purging data directories.
3. Install the old docker version.
{% highlight bash %}
 $sudo systemctl stop docker
 $sudo apt-get remove -y docker-ce docker-ce-cli
 $sudo apt-get update
 $sudo apt-get install -y docker-ce=5:18.09.4~3-0~ubuntu-bionic docker-ce-cli=5:18.09.4~3-0~ubuntu-bionic
docker version
{% endhighlight %}

## Upgrade docker
Here there is no need to remove the package or stop the docker.
{% highlight bash %}
$sudo apt-get install -y docker-ce=5:18.09.5~3-0~ubuntu-bionic docker-ce-cli=5:18.09.5~3-0~ubuntu-bionic
$docker version
{% endhighlight %}

## Configuring logging drivers - splunk journald, etc
Docker logging drivers route container logs to a selected destination. Driver capabilities
and options vary by Docker Engine version.

reference - (https://docs.docker.com/config/containers/logging/configure/)

Check the current default driver, then edit `/etc/docker/daemon.json`. This example uses
the `json-file` driver:

{% highlight bash %}
 $docker info --format '{{.LoggingDriver}}'
 $sudo vi /etc/docker/daemon.json

{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "15m"
  }
}
{% endhighlight %}
Next, restart docker after editing daemon.json

{% highlight bash %}
 $sudo systemctl restart docker
{% endhighlight %}

If you run a docker container, overwrite the system default logging driver
settings for individual container.

{% highlight bash %}
 $docker run --log-driver json-file --log-opt max-size=50m nginx
{% endhighlight %}

or syslog
{% highlight bash %}
  $docker run --log-driver syslog nginx
{% endhighlight %}

Restarting Docker can affect running containers; plan a maintenance window and consult
the documentation for the installed version.
