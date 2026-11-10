---
layout: post
title: "Docker Swarm, Backups, and Container Isolation"
description: "An introductory historical walkthrough of Docker Swarm, manager and worker nodes, backup concepts, namespaces, and cgroups."
date:   2020-04-12 18:20:31 +1300
categories: DevOps
---
This historical walkthrough introduces Docker Swarm and Linux container isolation.
Commands and recovery procedures are version- and environment-specific; verify them in a
test environment before using them operationally.

## Introduction to docker swarm
Docker Swarm is Docker Engine's clustering and orchestration mode. A swarm coordinates
services across manager and worker nodes.

## What is orchestrating?
Orchestration coordinates services and tasks to achieve a desired state.

## What kind of nodes are there in swarm?
Manager nodes maintain swarm state and schedule tasks; worker nodes run assigned tasks.
A production swarm requires an appropriate manager quorum and careful handling of join
tokens.

## How to setup Manager node in Docker Swarm?
{% highlight bash %}
docker swarm init --advertise-addr MANAGER_IP
{% endhighlight %}

## How to check whether the container is manager or not?
{% highlight bash %}
docker info
docker node ls
{% endhighlight %}

## How to setup docker worker?
In order to setup docker worker, first we need to
run the following command on the manager node.
Here is the process of adding worker nodes to the swarm.

On the Docker manager node:
{% highlight bash %}
docker swarm join-token worker
{% endhighlight %}

The manager prints a join command containing a secret token. Never publish a real token.
If a token may have been exposed, rotate it on an authorized manager:

{% highlight bash %}
docker swarm join-token --rotate worker
{% endhighlight %}

Run the generated command on the worker, substituting the actual token and manager
address securely. It has this form:
{% highlight bash %}
docker swarm join --token WORKER_JOIN_TOKEN MANAGER_IP:2377
{% endhighlight %}

Since we ran this command, this node will join a swarm as a worker.

On worker run this command and you could Is Manager is
false.

{% highlight bash %}
docker info | more
Swarm: active
 NodeID: 7ar25kulzn220rxebh6t5go56
 Is Manager: false
 Node Address: WORKER_IP
 Manager Addresses:
  MANAGER_IP:2377
{% endhighlight %}

Note you can run the below command only on the
docker manager node and not on docker worker node.

{% highlight text %}
cloud@manager:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS      ENGINE VERSION
qgwdh5n4ovqfq9i8xof6q3lbx *   manager             Ready               Active              Leader              18.09.5
gca4t9bfionwdgl63dc5trbgn     worker1             Ready               Active                                  18.09.5
7ar25kulzn220rxebh6t5go56     worker2             Ready               Active
{% endhighlight %}

See the [Docker Swarm tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/add-nodes/).

## Backing up and restoring swarm state
Swarm manager state is sensitive and can contain security-critical information. Backups
must be access-controlled, encrypted, stored separately from the manager, and tested.
Use the procedure documented for the exact Docker Engine version and deployment. Plan
maintenance carefully: stopping a manager can affect quorum and service availability.

Restoration is not simply extracting an archive over the live state directory. It can
require stopping managers, restoring state to the correct location, and starting a
recovered cluster with version-specific options. Never delete or overwrite
`/var/lib/docker/swarm` based on a generic snippet. Follow the
[Docker Swarm backup and restore documentation](https://docs.docker.com/engine/swarm/admin_guide/#back-up-the-swarm)
for the deployed version, and rehearse recovery before relying on a backup.

## Docker internals - namespace and cgroups
Namespaces and cgroups are Linux kernel features used by container runtimes to isolate
processes and limit or account for resource usage. See the
[Docker Engine security documentation](https://docs.docker.com/engine/security/).

Namespaces provide views of system resources that can be isolated for processes:

{% highlight text %}
1. pid - Process isolation
2. net -  network interfaces isolation
3. ipc - inter-process communication identifiers
4. mnt - filesystem mount points
5. uts - hostname and domain-name identifiers
{% endhighlight %}

## Control groups or cgroups
Control groups (cgroups) account for and apply limits to resources such as CPU and memory.
Container isolation uses multiple kernel mechanisms; namespaces and cgroups alone are
not a complete security boundary.
