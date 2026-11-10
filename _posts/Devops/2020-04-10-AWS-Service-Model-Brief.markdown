---
layout: post
title: "An Introduction to AWS Service Models"
description: "A concise introduction to IaaS, PaaS, SaaS, FaaS, and the AWS shared responsibility model."
date:   2020-04-10 16:23:31 +1300
categories: DevOps
---
This article introduces cloud service models and the AWS shared responsibility model.

## Account security
Enable multi-factor authentication (MFA), especially for privileged identities. Use
individual identities with least-privilege access for routine work, and protect account
recovery methods. Console steps and available MFA options change over time.

## Billing alerts
Configure billing and Free Tier notifications in AWS Billing and Cost Management. A
CloudWatch billing alarm can send notifications through an Amazon SNS topic. Metrics and
console steps may vary. Choose a threshold that fits the account and remember that an
alert is not a spending limit; charges may already have accrued when it arrives.

## Identity and access management
A **principal** is a person or workload that can make a request. **Authentication**
establishes who or what is making the request; **authorization** determines which actions
it may perform on which resources. An identity can be authenticated and still be denied
access by policy. Do not treat anonymous access as an identity that has been authenticated.

## Shared responsibility
AWS is responsible for security *of* the cloud infrastructure. Customers are responsible
for security *in* the cloud, with the exact division depending on the service. Customers
remain responsible for their data, identities, access policies, and configuration.
Responsibility for operating systems and infrastructure varies between services; it is
not accurate to say that AWS never manages anything inside a customer's cloud environment.

## Cloud service models
{% highlight text %}
IaaS - Infrastructure as a service
PaaS - Platform as a service
SaaS - Software as a service
FaaS - Function as a service
{% endhighlight %}

These are useful general categories, not strict AWS product classifications. Amazon EC2
is commonly described as IaaS; AWS Lambda is a serverless compute service. In general,
managed services shift more infrastructure operations to the provider, but customers
remain responsible for their code, data, and configuration.

## A simplified service stack
{% highlight text %}
Application data
Application and runtime
Operating system
Virtualization
Servers
Network and storage
Data center
{% endhighlight %}

Service choice affects control, operational responsibility, and cost. Serverless billing
is service-specific and may include requests, duration, and other resources—not only
whether a function was invoked. Review current AWS documentation before applying these
generalizations to a particular service.
