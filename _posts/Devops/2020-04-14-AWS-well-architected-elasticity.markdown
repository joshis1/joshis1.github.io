---
layout: post
title: "The AWS Well-Architected Framework and Elasticity"
description: "An overview of the original AWS Well-Architected Framework pillars and the concept of elasticity."
date:   2020-04-14 14:25:31 +1000
categories: DevOps
---
This article describes the original AWS Well-Architected Framework pillars as they were
presented when this post was written, and introduces elasticity. AWS has since updated
the framework; check the current documentation before applying its guidance.

The original framework described five pillars:

{% highlight text %}
 1. Security
 2. Reliability
 3. Performance efficiency
 4. Operational excellence
 5. Cost optimization
{% endhighlight %}

AWS later added sustainability as a sixth pillar. Refer to the current
[AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
for up-to-date principles.

## Security - Design Principles
The security pillar concerns protecting information, systems, and assets while delivering
business value through risk assessment and mitigation.

{% highlight text %}
1. Implement a strong identity foundation
2. Enable traceability
3. Apply security at all layers
4. Automate security best practices
5. Protect data in transit and at rest.
6. Prepare for security events.
{% endhighlight %}

## Reliability - Design Principles
Reliability pillar includes the ability of a system to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions, such as misconfigurations or transient network issues.

{% highlight text %}
1. Test recovery procedures
2. Automatically recover from failure
3. Scale horizontally to increase aggregate system availability
4. Stop guessing capacity
5. Manage change through automation
{% endhighlight %}

## Performance Efficiency - Design Principles
Performance efficiency pillar includes the ability to use
computing resources efficiently to meet system requirements and to maintain that efficiency as demand changes and technology evolve.
{% highlight text %}
1. Democratize advanced technologies
2. go global in minutes
3. use serverless architecture
4. experiment more often
5. mechanical sympathy
{% endhighlight %}

## Operational Excellence - Design Principles
The operational excellence pillar concerns running and monitoring systems to deliver
business value and continually improving supporting processes and procedures.
{% highlight text %}
1. Perform operations as code
2. Annotate documentation
3. Make frequent, small, reversible changes.
4. Refine operations procedures frequently
5. Anticipate failure
6. Learn from all operational events.
{% endhighlight %}

## Cost optimization - Design Principles
The cost optimization pillar concerns avoiding unnecessary costs while meeting
requirements.
{% highlight text %}
1. Adopt a consumption model.
2. Measure overall efficiency.
3. Stop spending money on data center operations.
4. Analyze and attribute expenditure.
5. Use managed services to reduce cost of ownership.
{% endhighlight %}

## Elasticity
Elasticity is the ability to acquire and release resources as demand changes. Automated
horizontal scaling is one way to implement it, but elasticity can involve other resource
types and scaling policies. A design should balance responsiveness, reliability, and cost.
