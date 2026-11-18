---
layout: post
title: "When an Operating Model Changes, What Actually Changes?"
date: 2026-11-18 09:00:00 +1000
categories: Management_Practices
description: "The difference between a value chain, an organisational operating model, management capabilities and the role titles that carry them."
---

"We're changing the operating model" sounds like a technology statement. Often, it is also a statement about **who makes decisions, how work is coordinated and where accountability sits**.

I used to connect the phrase immediately to the ITIL value chain. That is part of the story, but not the whole story.

<img src="{{ '/assets/img/operating-model-layers.png' | relative_url }}" alt="Operating model layers showing strategy and governance, decision rights, teams and vendors, and value delivery workflows" loading="lazy">

## ITIL's value chain and the wider business operating model

In ITIL, the **value chain** is the operating model of interconnected activities used to create value. It becomes real through specific value streams, supported by practices and viewed through the four dimensions.

In organisational transformation, however, **operating model** is often used more broadly. It can cover strategy, governance, process design, service ownership, team topology, vendor sourcing, technology and decision rights.

So an organisation can change its operating model without removing the need to **discover, build, transition, operate or support** a product. It might instead change **who performs those activities and how they are coordinated**.

## Capability, role and person are three different things

This distinction is especially important in technology delivery:

- **Capability:** The organisation's ability to perform an outcome — for example, manage project risks or suppliers.
- **Role:** A bundle of duties and decision rights allocated to a position — for example, Iteration Lead or Engineering Manager.
- **Person:** The individual currently performing that role, with their own skills and experience.

A management practice is closer to the *capability* level than to the person or position title.

If a project coordination role disappears, the Project Management practice may remain. Its activities might move to product leads, analysts, engineering managers or a central delivery function.

That doesn't prove the old role was ineffective, and it doesn't prove the new design is better. Those are separate questions that require evidence.

## The four questions I would ask during a redesign

**1. Who owns the outcome?** Not just the Jira board, but the real-world benefit, quality and service readiness.

**2. Who has the decision rights?** Can the delivery lead change scope, negotiate priorities or approve risk? Or must every trade-off go elsewhere?

**3. Where does integrated visibility come from?** Individual specialists can see their work clearly while cross-team dependencies remain invisible.

**4. What capability would become weaker if a role were removed?** If the answer is 'none', perhaps the work was duplicated. If the answer is 'risk visibility and cross-team coordination', that gap needs an explicit owner.

## A practical example

A vendor-led platform team has knowledgeable analysts, experienced testers, a supplier manager and a capable Product Owner. The squad can run its own stand-up and track work in Jira.

A dedicated Iteration Lead is useful **only if there is distinct work to own**: an integrated delivery forecast, cross-team risks, dependency resolution, release readiness, flow improvement or decision support.

Otherwise, the position may add a handoff rather than remove one.

The same analysis applies to new titles. Calling a position 'Engineering Manager' does not make it accountable for engineering quality if technical standards, people decisions and production ownership all live elsewhere.

## A better way to examine role design

I find a simple accountability map more useful than a role-title chart:

| Work | Responsible for evidence | Accountable decision owner |
| --- | --- | --- |
| Requirements are understood | Product / BA | Product Owner or delegated business authority |
| Technical solution is sound | Engineering / vendor | Delegated technical authority |
| Quality evidence is complete | QA / engineering | Agreed quality or release authority |
| Delivery risks are visible | Delivery coordination | Delivery sponsor / risk owner |
| Production change proceeds | Release/change participants | Designated change authority |

Exact accountabilities differ by organisation. The point is to make them **explicit**.

## The leadership lesson

> **An organisation doesn't create value because it has the right job titles. It creates value because essential capabilities, decisions and workflows fit together.**

That is the relationship I now see between ITIL, operating model design and engineering leadership.

*This is an independent reflection on operating models, not a claim about any specific employer or restructuring decision.*
