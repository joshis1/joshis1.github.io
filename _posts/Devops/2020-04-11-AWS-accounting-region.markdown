---
layout: post
title: "Understanding AWS Accounts and Regions"
description: "An introduction to AWS account boundaries, Regions, Availability Zones, VPCs, and edge locations."
date:   2020-04-12 19:01:31 +1300
categories: DevOps
---
This article introduces AWS accounts, Regions, Availability Zones, and edge locations.

## AWS accounts
AWS accounts are security and resource boundaries as well as a way to access AWS services.
They can help separate workloads, environments, and billing, but the benefits depend on
how identities, policies, and cross-account access are configured.

Authentication establishes who or what is making a request. Authorization determines
which actions that identity may perform on which resources. The account root user has
broad privileges and should be protected with MFA and used only when required. Use
individual identities with least-privilege access for routine work. An account boundary
alone does not guarantee that an incident or cost impact is contained.

Accounts have separate billing views, and organizations can be configured for consolidated
billing. Billing arrangements and account features depend on current AWS configuration.

## AWS Regions
A Region is a geographic area containing AWS infrastructure. Select Regions based on
latency, service availability, cost, resilience, and applicable data-residency obligations.
Data does not automatically stay in one Region: its location and replication depend on the
services and settings you choose. Amazon S3 is a regional service, although some S3
features and control-plane functions are global.

## Availability Zones
Each Region contains multiple Availability Zones (AZs), designed as separate failure
domains and connected by low-latency, high-bandwidth networks. Deploying across AZs can
improve resilience, but does not by itself guarantee fault tolerance; the application
must be designed and tested for failover.

## Virtual Private Cloud
A Virtual Private Cloud (VPC) is a logically isolated network in an AWS Region. Its
subnets are associated with Availability Zones.

## Edge locations and points of presence
AWS points of presence place selected networking and content-delivery services closer to
users. They are not smaller Regions or general-purpose substitutes for regional compute.
Choose a Region and architecture based on the services and requirements involved.

References:

- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [AWS service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/rande.html)
