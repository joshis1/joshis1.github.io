---
layout: post
title: "ITIL Has 34 Management Practices. That Doesn't Mean You Need 34 Teams."
date: 2026-11-18 08:45:00 +1000
categories: Management_Practices
description: "A practical explanation of ITIL management practices as capabilities, with examples of enabling versus supporting contributions, CSFs and metrics."
---

When I first studied ITIL, I saw a list of **34 management practices** and imagined 34 neatly labelled departments. Architecture Management. Project Management. Supplier Management. Incident Management. And so on.

Real organisations rarely work that way.

<img src="{{ '/assets/img/34-practices-capabilities.png' | relative_url }}" alt="ITIL's 34 management practices as capabilities that can be provided by shared teams, vendors and individuals rather than separate departments" loading="lazy">

## A practice is a capability, not a job title

A management practice is a set of organisational resources designed to perform work or accomplish an objective. It may involve people, skills, tools, workflows, contracts, information and controls.

For example, **Supplier Management** does not necessarily require a standalone Supplier Management department. A manager, procurement team and delivery lead might together maintain vendor performance, commercial arrangements and escalation routes.

Similarly, **Project Management** does not require every delivery squad to have a full-time project manager. Some activities may sit with a delivery lead, program office, product leader or engineering manager.

That distinction is why an organisation can change its team structure without abandoning the underlying capability.

## How the 34 are grouped in Version 5

ITIL Version 5 retains 34 practices and groups them into two broad families:

- **12 General Management practices**, including Project Management, Risk Management, Measurement and Reporting, Relationship Management, Supplier Management and Continual Improvement.
- **22 Product and Service Management practices**, including Business Analysis, Software Development and Management, Service Validation and Testing, Release Management, Incident Management and Change Enablement.

The key point is not memorising a reporting chart. It is recognising **which organisational capability a value stream needs**.

## A vendor-led product team, seen through the practices

Consider a team delivering changes to a digital platform:

| Work being performed | ITIL capability involved |
| --- | --- |
| Product team clarifies needs | Business Analysis |
| External partner develops code | Software Development and Management; Supplier Management |
| QA validates scenarios | Service Validation and Testing |
| Delivery lead tracks dependencies | Project Management; Risk Management |
| Manager handles vendor commitments | Supplier Management; Relationship Management |
| Production support restores service | Incident Management |
| Team reduces rework after a release | Continual Improvement |

Several roles contribute to one practice, and one role can contribute to several practices. That is normal.

## Do you have to implement all 34?

**No.** ITIL is guidance to adopt and adapt, not a checklist of mandatory departments. An organisation should have the capabilities needed for its objectives, risks and obligations — delivered internally, shared or sourced externally.

But avoiding the label does not remove the need. If nobody is accountable for recurring incidents, an organisation may have a **Problem Management capability gap**, even if it has a help desk and a ticketing system.

The useful question is not "Where is the Problem Management department?" but "Who investigates recurring causes, and how do we know the work is effective?"

## Enabling and supporting are relationships, not seniority levels

A practice may be directly involved in carrying out a value chain activity (**enabling**) or provide information and methods that help another activity (**supporting**). Which label fits depends on the specific activity and context.

The same practice can be more direct in one situation and more indirect in another. It does not mean an 'enabling' person outranks a 'supporting' person.

## Success needs evidence, not only ownership

A useful way to manage a practice is to connect four ideas:

**Purpose → success condition → metric → decision or improvement.**

For a delivery-focused Project Management capability:

| Success condition | Example metric |
| --- | --- |
| Dependencies are surfaced early | Time to identify and resolve critical dependencies |
| Forecasts are credible | Difference between forecast and actual completion |
| Significant risks are understood | High-impact risks with a mitigation owner |
| Release readiness is visible | Unresolved readiness exceptions at authorisation |

These are **illustrative operational measures**, not a reproduction of the official ITIL practice success factors or measurement tables.

A warning: a practice's measures are not automatically one employee's KPIs. Risk management may be a shared capability while specific risk acceptance decisions remain with accountable leaders.

## The practical takeaway

> **A management practice describes a capability an organisation needs to perform. A job title describes one way the organisation chooses to allocate that work.**

Once I made this distinction, ITIL became a much better lens for understanding why teams and roles change — and how to tell whether important work still has a clear owner.

**Further reading:** [PeopleCert ITIL FAQ — management practices in Version 5](https://www.peoplecert.org/help-and-support/faq-itil).
