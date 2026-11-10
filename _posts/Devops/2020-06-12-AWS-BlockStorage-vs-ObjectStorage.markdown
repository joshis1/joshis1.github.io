---
layout: post
title: "AWS Block Storage vs. Object Storage"
description: "Compare block storage such as Amazon EBS with object storage such as Amazon S3."
date:   2020-06-12 16:23:31 +1300
categories: DevOps
---

This article compares block storage and object storage at a high level. The examples are
historical; check current service documentation before making an architectural decision.

## Block Storage vs. Object Storage
Amazon S3 is object storage; Amazon EBS provides block storage volumes commonly used with
Amazon EC2.

## EBS block storage
Block storage exposes a volume as addressable blocks. A filesystem or application on the
attached host organizes those blocks and may maintain file metadata. It is often used for
workloads that need a mounted volume and random reads and writes, but suitability depends
on the workload and service configuration. Block storage is not limited to EC2 in general;
access depends on the product and attachment options.

Amazon EBS volumes can be attached to compatible EC2 instances and formatted or used by
applications as required.

## Object Storage
Object storage manages data as objects, usually consisting of data, metadata, and an
identifier within a storage namespace. The service abstracts the physical storage
location. It is typically accessed through an API rather than mounted as a conventional
block device. Amazon S3 is an example of object storage.
