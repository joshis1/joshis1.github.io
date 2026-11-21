---
layout: post
title: "ITIL Clicked When I Saw the Value System as a Noun and the Value Stream as a Verb"
date: 2026-11-18 08:00:00 +1000
categories: Management_Practices
description: "A practical mental model connecting the ITIL Value System, value streams, value chain, four dimensions and the product and service lifecycle."
---

I spent a surprising amount of time trying to memorise ITIL terminology: value system, value chain, value stream, management practices, four dimensions. I knew the definitions, but the relationships were not sticking.

Then I tried a programmer's mental model:

> **The Value System is a noun. A value stream is an action.**

That isn't the formal ITIL definition. It is the analogy that finally made the architecture of the framework click for me.

<img src="{{ '/assets/img/itil-noun-verb.png' | relative_url }}" alt="ITIL Value System as the organisational system, with value streams connecting demand to value and four dimensions crossing the entire system" loading="lazy">

## The noun: an organisation's value system

Think of a value system like a living body or a well-designed software system. It has connected parts that make meaningful outcomes possible. In **ITIL Foundation (Version 5)**, the ITIL Value System brings together five components:

| Component | The question I ask |
| --- | --- |
| **Guiding principles** | What principles should shape how we think and act? |
| **Governance** | Who evaluates, directs and monitors? |
| **Value chain** | What interconnected activities make up our operating model? |
| **Management practices** | Which capabilities and resources enable the work? |
| **Continual improvement** | How do we keep making the whole system more effective? |

These are **not five steps that execute in sequence**. They are interdependent parts of one system. Governance can influence delivery decisions while guiding principles shape the team's behaviour and continual improvement changes how work is done.

An example of a guiding principle is **focus on value**. "Prioritise platform stability this quarter" is different: that is a strategic choice or policy. The principle helps us make good choices *within* that direction.

## The verb: a value stream

Now imagine a business request: a customer needs a booking confirmed, or an internal employee needs a system outage resolved.

A **value stream** is the particular end-to-end flow of activities through which the organisation responds to demand or opportunity and creates value. In shorthand:

**Demand or opportunity → coordinated work → value.**

The verb analogy helps: the system is capable of doing things; the value stream is how value-creating work actually happens.

It also exposes a trap: completing tasks is not necessarily the same as creating value. A team can close every delivery ticket yet leave users struggling with the released service.

## The operating model: the value chain

The **value chain** describes interconnected activities that can be combined into different value streams. In ITIL Version 5, the product and service lifecycle makes eight activity areas explicit:

**Discover · Design · Acquire · Build · Transition · Operate · Deliver · Support**

A software engineer may recognise a familiar lifecycle, but this is **not a compulsory waterfall sequence**. Different value streams use activities in different combinations. One product may be operating while the next version is being designed and built. An incident may start with support and lead back to design.

A practical distinction is:

- **Value chain:** the reusable operating model of activities.
- **Value stream:** one real flow of work through activities and practices to create an outcome.
- **Process:** a defined set of interrelated activities, often more specific than the end-to-end value stream.

## Where do the four dimensions sit?

My next question was: *Do the four dimensions apply only to build and operate, or to governance and management practices too?*

The useful answer is to treat them as **four lenses across the entire system**:

1. **Organisations and people:** roles, skills, culture and accountability.
2. **Information and technology:** data, tools, platforms, knowledge and security.
3. **Partners and suppliers:** external capabilities, contracts, interfaces and dependencies.
4. **Value streams and processes:** how work flows, handoffs occur and outcomes are produced.

For example, take **governance**. There are people who make decisions, information that informs those decisions, suppliers whose performance matters, and processes for approval and escalation. The same four lenses can help assess project management, supplier management and continual improvement.

**PESTLE** adds a view of the *external environment*: political, economic, social, technological, legal and environmental influences. It is **not a sixth component of the Value System**.

## One example that connects everything

Consider a fictional appointment-booking service. The product team wants to release a new reminder capability.

The **value stream** runs from the need, through analysis, engineering, testing, transition, operation and support, towards a usable service.

The **Value System** provides governance, principles, practices, operating activities and improvement mechanisms.

The **four dimensions** force a wider view: do Operations know the process? Is the technology resilient? Are vendor commitments clear? Are the handoffs workable?

The result we want is not merely "release completed". It is a service that helps the business and the people relying on it.

## The mental model I now use

> **Value System = the whole system. Value chain = the operating model. Value stream = the actual flow from demand to value. Four dimensions = the lenses used to see the whole system.**

This is the point where ITIL stopped feeling like a vocabulary test and started resembling systems thinking.

**Further reading:** [PeopleCert — ITIL Foundation (Version 5)](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-5-foundation-version-50-4154).

*This article is an independent learning interpretation, not an official ITIL training guide.*

*All service examples are invented for learning and do not refer to a specific organisation, client, supplier or incident.*
