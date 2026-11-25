---
layout: post
title: "An On-Time Release Is Not Always a Successful Outcome"
date: 2026-11-18 08:30:00 +1000
categories: Management_Practices
description: "A fictional release example explaining outputs, outcomes, value and Goodhart's Law."
---

**Fictional learning scenario:** Imagine a product team releasing an appointment-reminder feature on schedule. After release, users identify a few missed edge cases and support documentation that needs improvement. The circumstances are invented solely to explore how delivery success should be measured.

**Was that a successful delivery?**

<img src="{{ '/assets/img/delivery-vs-value.png' | relative_url }}" alt="On time release checked green but operational readiness and business value still require validation" loading="lazy">

## The difference between output, outcome and value

These three ideas sound similar, but they answer different questions:

| Lens | Question | Example |
| --- | --- | --- |
| **Output** | What did we deliver? | An appointment-reminder feature |
| **Outcome** | What changed for the people using it? | Customers receive accurate reminders |
| **Value** | What useful benefit was realised? | Fewer missed appointments and less manual follow-up |

"Delivered on time" is an important delivery measure. It is not, by itself, proof of the outcome.

## Is this Goodhart's Law?

A common modern paraphrase of Goodhart's Law is:

> "When a measure becomes a target, it ceases to be a good measure."

The precise historical formulations are more nuanced, but the practical management warning is clear: when people are rewarded for a proxy, they can optimise the proxy instead of the underlying objective.

There are **two different explanations** for the release scenario:

**Possibility 1 — a Goodhart effect.** Leadership emphasises hitting the date so strongly that unresolved operational-readiness issues are discounted, testing time shrinks, or a "green" report is valued more than honest uncertainty. The score improves while the real outcome deteriorates.

**Possibility 2 — ordinary delivery uncertainty.** The team made reasonable decisions, but requirements were incomplete, some edge cases were unknown, or defects emerged despite good controls. That is a delivery and quality problem, but it does not prove metric-driven distortion.

An on-time release followed by defects is **evidence of a gap between the milestone and the outcome**. It is not sufficient evidence, on its own, to diagnose Goodhart's Law.

## The measurement trap

Imagine an executive scorecard containing only:

- Release delivered by the committed date: **Yes**.

The team can satisfy that target while operational readiness remains uncertain. A stronger set of measures answers more than one question:

| Perspective | Illustrative indicator |
| --- | --- |
| Schedule | Forecast accuracy and release-date adherence |
| Quality | Critical scenarios passed, high-severity escaped defects |
| Readiness | Support training, runbooks, monitoring and ownership confirmed |
| Adoption | Successful use of the new capability in real workflows |
| Value | Rework avoided, user outcomes and business benefit indicators |

**More metrics are not automatically better.** A small number of balanced, decision-relevant indicators is often more useful than a large dashboard of vanity measures.

## Where CSFs and KPIs fit

This is where ITIL's management practice thinking becomes practical.

**Objective:** Introduce a reliable new capability into production.

**Critical success factor (CSF):** Critical business scenarios are validated and the service is operationally supportable.

**Metric:** Percentage of agreed critical scenarios passed before release.

**KPI:** A selected indicator with an agreed threshold and decision rule — for example, all agreed critical scenarios passed before authorisation, with any exception formally assessed.

A metric tells us something. A KPI elevates it as an important signal. A CSF tells us **what must be true for success**. The official ITIL practice guidance also uses *practice success factors (PSFs)* when discussing practice effectiveness.

## Who owns the problem?

Consider a fictional delivery involving analysts, testers, support staff, a Product Owner, engineers, a delivery lead and a designated release decision-maker.

The BA and Product Owner help ensure requirements and business acceptance are understood. Testers provide validation evidence. Engineers address technical defects. Operations assesses supportability. The delivery lead joins up the risks and dependencies. A designated authority makes the decision to proceed within governance.

No single person can replace all of those controls.

What the delivery leader **can** do is prevent an information problem becoming a decision problem. Before authorisation, they can make unresolved risks explicit, show their likely impact and identify who must decide.

## A better release conversation

Instead of asking only, "Are we on track for Thursday?", ask:

1. What evidence tells us this capability works for its most important real-world scenarios?
2. Which requirements and edge cases remain unverified?
3. Can Operations detect, support and recover from failures?
4. What risks are we accepting, and who has authorised them?
5. What will we measure after release to know whether value was realised?

This connects directly to ITIL's guiding principle **focus on value**. It also makes continual improvement meaningful: learn from the gaps, change the system, and observe whether the change actually helped.

## A useful question for any release review

> **Would we still call this delivery successful if the release date were removed from the dashboard?**

If the answer is unclear, the team needs a better definition of success — not necessarily another status report.

**Further reading:** [Cambridge discussion of Goodhart's Law](https://www.damtp.cam.ac.uk/user/mem2/papers/LHCE/goodhart.html) · [PeopleCert ITIL Foundation (Version 5)](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-5-foundation-version-50-4154).

*This independent educational article does not describe, assess or attribute outcomes to any current or former employer, colleague, client or supplier.*
