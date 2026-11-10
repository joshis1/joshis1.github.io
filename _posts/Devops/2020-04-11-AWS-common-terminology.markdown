---
layout: post
title: "AWS Architecture Terminology"
description: "A glossary of availability, disaster recovery, scaling, encryption, and architecture concepts."
date:   2020-04-11 16:23:31 +1300
categories: DevOps
---
This glossary introduces common concepts used when discussing cloud architecture and
disaster recovery.

## High availability
A highly available system is designed to reduce the likelihood and duration of service
interruptions. It may recover from failures automatically, but some interruption can
still occur.

## Fault tolerance
A fault-tolerant system is designed to continue providing its intended service despite
specified component failures, ideally without user-visible interruption. The achievable
level depends on the failure being considered; fault tolerance does not guarantee zero
outages and usually adds cost and complexity. A load balancer can route around an
unhealthy instance, provided the application and its dependencies can also tolerate the
failure.

Discuss the required recovery behavior, acceptable interruption, and cost with
stakeholders rather than treating availability and fault tolerance as interchangeable.

## Disaster recovery

### Recovery point objective (RPO)
The RPO is the maximum acceptable amount of data loss, expressed as a period of time.
Replication and recovery design affect the actual recoverable point; it is not simply the
time since the last backup.

### Recovery time objective (RTO)
The RTO is the target maximum time to restore a service after an outage. Test recovery
plans against both RTO and RPO targets.

Lower targets often require more frequent replication, additional capacity, automation,
and testing, which can increase cost. Choose targets based on business impact.

## Scaling
Vertical scaling increases the resources of a machine. Horizontal scaling adds instances
or nodes. Both approaches have trade-offs. Horizontal scaling usually requires an
application designed to distribute work and manage shared state.

### Three-tier architecture
{% highlight text %}
1. Presentation
2. Application logic
3. Data
{% endhighlight %}

Separating these concerns can make independent scaling easier, but a monolithic
application can also be horizontally scaled if it is designed for it.

## Encryption
Symmetric encryption uses the same secret key to encrypt and decrypt. Asymmetric
cryptography uses a related public/private key pair. Keep private keys secret and protect
them with appropriate access controls.

Example of symmetric encryption with GnuPG:

{% highlight bash %}
printf '%s\n' "Example message" > message.txt
gpg --symmetric message.txt
gpg --output decrypted.txt --decrypt message.txt.gpg
{% endhighlight %}

Public-key encryption requires the recipient's verified public key:

{% highlight bash %}
gpg --encrypt --recipient recipient@example.com message.txt
gpg --output decrypted.txt --decrypt message.txt.gpg
{% endhighlight %}

## General architecture concepts
1. **Cost efficiency:** Meet requirements while managing initial and ongoing costs.
2. **Security:** Protect data and operations using controls appropriate to the risks.
3. **Application session state:** Data about a user's activity, such as a shopping cart.
   Storing state outside an application instance can make it easier to replace or scale
   that instance; it does not by itself make a system stateless.
4. **Undifferentiated heavy lifting:** Operational work that does not directly
   differentiate a product. Managed services can reduce some of this work, but do not
   remove the customer's responsibility for configuration and data.
