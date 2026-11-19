---
layout: post
title: "If the Team Can Run Its Own Stand-up, What Is an Iteration Lead For?"
date: 2026-11-18 08:15:00 +1000
categories: Management_Practices
description: "A candid look at Iteration Lead value, delegated authority and the difference between coordination and delivery leadership in a vendor-led environment."
---

Here is an uncomfortable question for anyone in Agile delivery:

> **If the analysts clarify requirements, testers coordinate testing, a vendor builds the software, management handles the vendor, and the team can run its own ceremonies — what exactly does an Iteration Lead own?**

I have found this question more useful than debating whether a team should estimate in story points or days.

<img src="{{ '/assets/img/iteration-lead-value.png' | relative_url }}" alt="Specialist teams own analysis build and test while the delivery lead connects dependencies risks decisions and readiness" loading="lazy">

## First, separate the work from the coordination

Imagine an enterprise platform with a Product Owner, business analysts, testers, a third-party development vendor and an engineering or delivery manager.

The Product Owner owns business priorities and acceptance decisions. Analysts refine requirements and coordinate estimates. The vendor makes implementation commitments. Testers validate behaviours. A manager owns commercial vendor escalations. A Jira dashboard displays progress.

Where does that leave the Iteration Lead?

Potentially **nowhere useful**, if the only remaining activities are scheduling meetings and repeating status updates. There is no rule in ITIL or Agile that says a dedicated coordinator must exist in every squad.

But there *is* a valuable gap when nobody owns the **integrated delivery picture**.

## What the integrated delivery picture actually means

A delivery leader ought to join up facts that are individually correct but collectively worrying:

- The vendor expects a fix on Wednesday.
- Testers need three days of regression after that fix.
- The change window closes on Thursday evening.
- Operations still needs the support runbook and monitoring details.
- The Product Owner believes the release is green.

Every specialist can be competent, and the overall delivery can still be at risk.

The delivery leader's contribution is to connect these signals and frame the decision: **"Given the dependency, the current date is no longer credible. Here are the options, the impacts and the decision needed."**

That is different from asking, "Can everyone please update Jira?"

## ITIL: a role is not a management practice

ITIL Version 5 retains 34 management practices. They are **organisational capabilities**, not 34 departments or 34 job titles.

An Iteration Lead may contribute to multiple practices without owning any of them end to end:

| Practice | Practical contribution |
| --- | --- |
| Project management | Integrated planning and forecasting within delegated scope |
| Risk management | Expose delivery risks and arrange timely escalation |
| Measurement and reporting | Translate data into actionable decisions |
| Relationship management | Connect business, technology, testing and support |
| Supplier management | Track vendor dependencies, without necessarily owning the vendor contract |
| Continual improvement | Reduce waiting, rework and avoidable handoffs |
| Release management | Coordinate readiness information, not necessarily approve the release |

A meeting facilitator can contribute to these practices. But facilitation alone does not constitute full accountability for delivery.

## The authority test

I now think about delivery roles through four questions:

1. **Outcome:** Which result am I explicitly accountable for?
2. **Authority:** What can I decide, and what must go to someone else?
3. **Access:** Am I in the conversations where dependencies and trade-offs are discussed?
4. **Distinct value:** What would remain unresolved if I were not there?

If the role has accountability without access or authority, it becomes dependent on others for every meaningful action. If the role has access but no outcome, it risks turning into a reporting function.

Neither arrangement necessarily means an individual lacks ability. It may mean the **role design is weak**.

## You do not need to be the deepest product expert

A Delivery Lead working on an insurance platform should understand the main business journey, key integrations, release constraints and failure modes. They do **not** have to know the platform as deeply as the most experienced technical analyst or vendor engineer.

The required skill is to understand enough to ask the right integration question:

"If document generation fails, how is the claim notified, retried and reconciled — and who owns that failure?"

That is technical fluency in service of delivery, not pretending to be the solution architect.

## A practical daily operating loop

Instead of owning ceremonies, I would design a routine around **exceptions and decisions**:

- **Morning:** Review the delivery board and actual testing, deployment and vendor evidence. Identify changed risks.
- **During the day:** Unblock cross-team dependencies and reconcile inconsistent forecasts. Avoid duplicating the analysts' technical discussions.
- **When a decision is needed:** Present options and impacts to the decision owner. Track the decision and downstream effects.
- **Before release:** Ensure readiness evidence from QA, Operations, product and technology is visible to those who authorise the release.
- **Weekly:** Examine aging work, rework, escaped defects, forecast accuracy and recurring handoffs. Choose one improvement and check its effect.

Story points are optional. **Predictability and quality are not.** Day estimates, lead time and transparent forecasts can work if teams use them sensibly.

## What if the team genuinely needs no dedicated Iteration Lead?

That can be a positive outcome. A mature team might distribute delivery coordination among specialists, with one Delivery Manager covering several teams and cross-cutting risks.

The mature response is not to invent ceremonies to justify a position. It is to find where leadership really adds value — or recognise that the operating model no longer needs a separate role.

> **A leader's value is not how many meetings depend on them. It is how much better the system performs because of their contribution.**

That is the standard I would apply to any Delivery Lead or Engineering Manager role.

*Examples are deliberately generic composites. Responsibilities vary by organisation and delegated decision rights.*
