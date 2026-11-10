---
layout: post
title: "Docker Images and Dockerfiles: An Introduction"
description: "Learn how Docker image layers work and how a Dockerfile builds and runs a simple Nginx image."
date:   2020-04-13 14:56:31 +1000
categories: DevOps
---
This historical introduction explains Docker image layers and a simple Nginx image. The
Ubuntu and Nginx versions shown are obsolete; use maintained base images and current
package versions for new projects.

## What is a docker image
Images package the filesystem and metadata used to create containers. Image layers are
read-only and can be shared; a running container adds a writable layer.

See the [Docker image documentation](https://docs.docker.com/build/concepts/).

For example, the following command pulls an image from Docker Hub:

{% highlight bash %}
 $docker image pull nginx
{% endhighlight %}

## Structure of image
An image consists of one or more read-only layers.

## Structure of a container
A container adds a writable layer. Data that must persist beyond the container's
lifetime should be stored in a volume or another external data service.

Example
{% highlight text %}
 Writeable container layer #Only container creates this layer
 Web-application - image  #read only layer
 Python - image  #read only layer
 Base Ubuntu OS image #read only layer
{% endhighlight %}

See the [Docker image documentation](https://docs.docker.com/build/concepts/).

## Advantages of layered file system
Layers can be shared between images and containers, reducing repeated storage and transfer.
Build caches can also avoid repeating unchanged steps.

{% highlight text %}
1. Smaller repeated storage footprint
2. Less data to transfer when layers are already cached
3. Faster rebuilds when cached steps remain valid
{% endhighlight %}

For example, containers created from the same image can share its read-only layers while
maintaining separate writable layers.

## How to find what layers an image comprises of?
{% highlight bash %}
 $docker image history <image name>
{% endhighlight %}

This will list the layers used to build an image.

## Build a simple Docker image
Docker Hub provides public images. Anyone running software in Docker should understand
how a Dockerfile builds an image.

See the [Dockerfile reference](https://docs.docker.com/reference/dockerfile/).

{% highlight bash %}
mkdir ~/custom-nginx
cd ~/custom-nginx
printf '%s\n' 'Hello, World!' > index.html
{% endhighlight %}

## What are directives in docker?
It is a set of instructions which are used to construct a docker image.
These instructions are called directives.

## Common Directives
{% highlight text %}
1) FROM - it starts a new build stage and sets the base image. It is usually must be the first directives in the Dockerfile(except ARG can be placed before FROM)

2) ENV - sets environment variables. These can be referenced in the Dockerfile itself and are visible to the container at run time.

3) RUN - it creates a new layer on top of the previous layer by running a command inside that new layer and committing the changes.

4) CMD - specifically a default command used to run a container at execution time.
{% endhighlight %}

Create a file named `Dockerfile` with the following contents:

{% highlight dockerfile %}
# Historical example; use a supported base image and package version in new builds.
FROM ubuntu:bionic
ENV NGINX_VERSION 1.14.0-0ubuntu1.7
RUN apt-get update && apt-get install -y curl
RUN apt-get update && apt-get install -y nginx=$NGINX_VERSION
COPY index.html /var/www/html/index.html
CMD ["nginx", "-g", "daemon off;"]
{% endhighlight %}

## Build and test the image
In order to build and test the image, we need to run the following.
{% highlight bash %}
 $docker build -t custom-nginx .
 $docker run --name custom-nginx -d -p 8080:80 custom-nginx
curl localhost:8080
{% endhighlight %}

## More directives
Dockerfiles offer many different directives which we can use to build and customize our images.

{% highlight text %}
1) EXPOSE - documents which port(s) are intended to published when running a container.

2) WORKDIR - sets the current working directory for subsequent directives such as
ADD, COPY, CMD, ENTRYPOINT, etc. We can use relative path here too.

3) COPY - copy files from the local machine to the image.

4) ADD - it is similar to COPY, but can also pull files using a URL and extract an archive into loose files in the image.

5) STOPSIGNAL - specify the signal that will be used to stop the container.

6) HEALTHCHECK - specify a command to run in order to perform a custom health check to verify that the container is working properly.

{% endhighlight %}

Here is an example.
{% highlight dockerfile %}
# Historical example; use a supported base image and package version in new builds.
FROM ubuntu:bionic
ENV NGINX_VERSION 1.14.0-0ubuntu1.7
RUN apt-get update && apt-get install -y curl
RUN apt-get update && apt-get install -y nginx=$NGINX_VERSION
WORKDIR /var/www/html/
COPY index.html ./index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
STOPSIGNAL SIGTERM
HEALTHCHECK CMD curl --fail --silent --show-error localhost:80
{% endhighlight %}

Now, rebuild the image and test it.
{% highlight bash %}
 $docker build -t custom-nginx .
 $docker run -d -p 8080:80 custom-nginx
 $curl localhost:8080
{% endhighlight %}

Now, locate our running container with docker ps, then remove it to clean up the environment.
{% highlight bash %}
 $docker ps
 $docker container rm -f <container id>
{% endhighlight %}

Here is a simple project that build docker image and runs the docker image.
[custom_docker_project](https://github.com/joshis1/docker_custom_build)

This brings an end to this article.
