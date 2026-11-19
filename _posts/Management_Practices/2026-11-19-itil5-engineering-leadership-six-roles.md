---
layout: post
title: "ITIL 5 through an engineering leader's eyes: the same practices, six very different jobs"
date: 2026-11-19
categories: [Engineering Leadership, ITIL]
tags: [ITIL-5, Engineering-Manager, Engineering-Operations, Iteration-Lead, Google, Financial-Services, Agile]
description: "My practical map of ITIL management practices to the capabilities and responsibilities of Iteration Leads, Engineering Managers and Engineering Operations Managers in product technology and financial services."
image: /assets/itil5/itil5-six-roles-overview.png
---
# ITIL 5 through an engineering leader’s eyes: six roles, not six job titles

*The same management practice can mean a completely different responsibility depending on the role you hold.*

![Animated guide to the six engineering leadership contexts](/assets/itil5/itil5-six-roles-website.gif)

Something clicked for me while studying ITIL Foundation (Version 5).

I had been thinking about career progression in terms of job titles: Iteration Lead, Engineering Manager, Engineering Operations Manager. But a title doesn't tell me what I need to learn. Even the same title can mean something different in a financial-services enterprise and a technology company.

The better question is: **Which management practices must I understand, what capability must I develop, and what should I actually be able to do with it?**

This matters to me because my background has moved across software engineering, Linux and systems integration, and then into delivery leadership in Australian superannuation and insurance technology. I've spent time where the sprint board, testing evidence, release governance and the people supporting production all meet. I enjoy delivery, but I also want to stay close to engineering. So this is more than an ITIL study note. It is a way for me to test where I am strong and where I still need to grow.

One lesson I keep coming back to: **a release can look green on a board and still be unready for the people who depend on it.** The real skill is making those gaps visible early and helping the right people make the decision.

## Two environments. Three roles. Six different expectations.

By **product technology**, I mean a Google-style environment: teams building software products and platforms at scale. Google is the example I keep in mind for engineering depth, product ownership, SRE and automation. I am *not* suggesting Google uses an “Iteration Lead” or “Engineering Operations Manager” title in exactly this form; they are comparison roles, not a Google organisation chart.

By **enterprise technology**, I specifically mean financial services: a bank, insurer or superannuation fund. Security and resilience matter in both worlds, but the shape of work can change: business rules, vendor platforms, privacy, regulatory obligations, older integrations, release windows and evidentiary controls may be especially prominent in financial services.

I use three simple verbs to remember the roles:

- **Iteration Lead — FLOW:** help the team make progress, surface dependencies and learn.
- **Engineering Manager — BUILD:** develop engineers and improve technical decisions and outcomes.
- **Engineering Operations Manager — RUN:** keep services healthy, recover them and improve how they operate.

Every role still needs to **focus on value, collaborate, think holistically and improve**. They just act on those principles differently.

## Quick comparison: what each role is accountable for

| Role / context | Primary capability | Example responsibility | Evidence I would look for |
| --- | --- | --- | --- |
| Iteration Lead — Google-style tech | FLOW + FEEDBACK | Make blocked work visible, not just report it. | A team that learns faster and delivers predictably. |
| Iteration Lead — Financial services | FLOW + ASSURANCE | Connect business requirements, vendors, testing and release teams. | A release that is genuinely ready, not just reported green. |
| Engineering Manager — Google-style tech | PEOPLE + BUILD | Hire, coach and grow technical judgement. | A stronger team and software that scales. |
| Engineering Manager — Financial services | PEOPLE + CONTROLS | Lead engineers across APIs, integrations and business-critical systems. | Engineering that is secure, maintainable and trusted. |
| Engineering Operations Manager — Google-style tech | RUN + AUTOMATE | Set service goals that reflect real customer experience. | Observable, resilient services with less manual toil. |
| Engineering Operations Manager — Financial services | RUN + RECOVER | Know which business services and members are affected. | Resilient services, safe recovery and accountable operations. |

## The practice-to-capability map

Here is the difference between *knowing the practice name* and *being ready for the role*. I chose five practices for each role to keep the main article useful. There is a complete 34-practice learning matrix further below.

### 1. Iteration Lead — Google-style product engineering

**Help a product team move, learn and improve.**

| ITIL management practice | Capability to build | What it means on the job | What good looks like |
| --- | --- | --- | --- |
| Continual improvement | See and fix friction | Ask why work waits between design, code and test; run a small experiment. | Cycle time and blocked work trend in the right direction. |
| Measurement and reporting | Read the delivery system | Use ageing work, work in progress and customer results—not velocity as a performance target. | The team spots trouble before a deadline slips. |
| Relationship management | Build shared decisions | Get product, design, engineering and operations talking about trade-offs. | Fewer surprises and cleaner hand-offs. |
| Project management | Manage dependencies | Keep one visible decision and dependency list; name decision owners. | Cross-team commitments are explicit. |
| Knowledge management | Spread learning | Turn reviews and retrospectives into decisions teams can reuse. | Fewer repeated conversations and avoidable mistakes. |

**My shortcut:** FLOW + FEEDBACK → A team that learns faster and delivers predictably.

### 2. Iteration Lead — Bank, insurer or superannuation fund

**Make complex delivery ready for production.**

| ITIL management practice | Capability to build | What it means on the job | What good looks like |
| --- | --- | --- | --- |
| Project management | Integrated delivery planning | Bring internal and vendor dependencies, decisions and constrained capacity into one plan. | A forecast the team and business can trust. |
| Change enablement | Readiness and risk coordination | Track testing evidence, change windows and approvals; leave authorisation to its owners. | Fewer late surprises during governance checks. |
| Release management | Make hand-offs real | Align the release plan, run sheet, support team and sign-offs. | People know what happens before, during and after go-live. |
| Supplier management | Unblock external dependencies | Escalate vendor issues with business impact, action owner and decision date. | Vendor uncertainty stops being a hidden blocker. |
| Service validation and testing | Know what good means | Make business acceptance, regression coverage and control evidence visible. | Readiness is based on evidence, not optimism. |

**My shortcut:** FLOW + ASSURANCE → A release that is genuinely ready, not just reported green.

### 3. Engineering Manager — Google-style engineering team

**Grow engineers who can build and run great systems.**

| ITIL management practice | Capability to build | What it means on the job | What good looks like |
| --- | --- | --- | --- |
| Workforce and talent management | Grow people and ownership | Coach, hire and create room for engineers and tech leads to make decisions. | Engineers grow into independent technical leaders. |
| Architecture management | Make sound trade-offs | Guide service boundaries, interfaces, performance and maintainability decisions. | Design decisions are written down and revisited. |
| Software development and management | Strengthen engineering craft | Improve code review, automated tests and development workflows. | Safer, more frequent delivery and fewer defects. |
| Capacity and performance management | Plan for scale | Help teams think about traffic spikes, latency, scaling and cost. | The service stays responsive as usage grows. |
| Service level management | Keep promises to users | Agree reliability targets with product and SRE, then build toward them. | Reliability is an engineering choice, not a surprise. |

**My shortcut:** PEOPLE + BUILD → A stronger team and software that scales.

### 4. Engineering Manager — Bank, insurer or superannuation fund

**Build securely and make the controls part of the design.**

| ITIL management practice | Capability to build | What it means on the job | What good looks like |
| --- | --- | --- | --- |
| Architecture management | Design across complexity | Own trade-offs across legacy platforms, payments, claims, APIs and data flows. | Documented, tested designs across boundaries. |
| Risk management | Engineer control effectiveness | Understand regulatory and member impact; define mitigations with risk owners. | Risks become controls and verifiable tests. |
| Information security management | Protect sensitive data | Design access, encryption, privacy and safe handling into systems from the start. | Less rework and fewer security exceptions. |
| Workforce and talent management | Build sustainable expertise | Develop integration and domain skills, give engineers ownership and plan succession. | No critical capability depends on one person. |
| Service validation and testing | Prove it is safe to use | Lead non-functional testing, failure scenarios and credible technical sign-off. | Go-live evidence covers more than the happy path. |

**My shortcut:** PEOPLE + CONTROLS → Engineering that is secure, maintainable and trusted.

### 5. Engineering Operations Manager — Google-style SRE / platform engineering

**Turn reliability into an engineering discipline.**

| ITIL management practice | Capability to build | What it means on the job | What good looks like |
| --- | --- | --- | --- |
| Service level management | Set practical reliability targets | Define service indicators, objectives and sensible trade-offs with product teams. | SLOs guide release and investment decisions. |
| Monitoring and event management | Detect before users complain | Make alerts actionable and connect metrics to customer journeys. | Early signals and less alert noise. |
| Incident and problem management | Restore, learn, prevent | Coordinate response, hold blame-free reviews and remove recurring causes. | Fewer repeat incidents and faster recovery. |
| Infrastructure and platform management | Make good operations repeatable | Build self-service deployment paths, cloud standards and useful platform tools. | Less manual toil and safer service changes. |
| Capacity and performance management | Keep scale economical | Anticipate peak loads and tune performance without uncontrolled costs. | Healthy latency, headroom and unit cost. |

**My shortcut:** RUN + AUTOMATE → Observable, resilient services with less manual toil.

### 6. Engineering Operations Manager — Bank, insurer or superannuation fund

**Keep critical services running and recover them safely.**

| ITIL management practice | Capability to build | What it means on the job | What good looks like |
| --- | --- | --- | --- |
| Incident management | Restore service and communicate | Coordinate impact assessment, response, escalation and business updates. | People know what is broken and when it is restored. |
| Service continuity management | Be able to recover | Prove backup, failover, recovery objectives and exercise outcomes. | Recovery is tested, not only documented. |
| Change enablement | Control production risk | Apply proportionate risk reviews, approvals, emergency paths and rollback readiness. | Changes are auditable and safer to execute. |
| Supplier management | Close the ownership gaps | Hold external providers to operational obligations and escalation arrangements. | Vendor response works under pressure. |
| Problem management | Prevent recurrence | Prioritise repeat failures and track effective permanent fixes. | Known problems do not linger indefinitely. |

**My shortcut:** RUN + RECOVER → Resilient services, safe recovery and accountable operations.

## One practice, six different responsibilities: Change Enablement

This was the clearest way for me to connect the dots. “Change Enablement” is not just a meeting or an approval form; it is about making changes safe enough to deliver value.

| Context | A practical responsibility |
| --- | --- |
| Google-style Iteration Lead | Help teams see which dependencies, approvals or technical decisions are holding up a release; make the issue visible without trying to become the change approver. |
| Financial-services Iteration Lead | Coordinate business and testing sign-offs, vendor prerequisites, release windows and the people needed at go-live. |
| Google-style Engineering Manager | Guide engineers to use automated checks, gradual rollouts to a small group first, clear monitoring and a reliable way to reverse a change. |
| Financial-services Engineering Manager | Make sure the proposed design, test evidence and controls justify production readiness. |
| Google-style Engineering Operations Manager | Build the tools and operating safeguards that make gradual rollouts, monitoring and quick rollback routine. |
| Financial-services Engineering Operations Manager | Ensure emergency and planned changes have appropriate decision-makers, impact assessment, communication and recovery readiness. |

I prefer saying **“roll it out to a small group first, check that it works, then expand it”** rather than dropping specialist deployment jargon into every conversation. The engineering behind it matters, but the explanation should work for business stakeholders too.

## An example I can relate to: claims correspondence stops working

Imagine a claims system sends letters through an external service. Some letters fail, and members do not receive important correspondence. At first, it might look like a straightforward integration defect. But this is exactly where role boundaries and the whole-system view matter.

| Role | First useful action | ITIL practice lens |
| --- | --- | --- |
| Google-style IL | Make dependencies and the next product-team decision visible. | Relationship Management; Measurement and Reporting |
| Financial-services IL | Bring BA, vendor, testers, release owners and business decision-makers into a single realistic recovery plan. | Project Management; Supplier Management; Change Enablement |
| Google-style EM | Help engineers choose between queueing, retries, de-duplication and better integration design. | Architecture Management; Software Development and Management |
| Financial-services EM | Ensure the technical fix protects correspondence integrity, personal data and auditability. | Risk Management; Information Security Management; Service Validation and Testing |
| Google-style Ops | Make the failures visible, respond quickly and automate recovery where safe. | Monitoring and Event Management; Incident Management; Problem Management |
| Financial-services Ops | Assess the affected members, restore service safely, reconcile failed items and verify the recovery process. | Incident Management; Service Continuity Management; Supplier Management |

A useful leadership sequence is: **Validate the problem → understand the customer impact → stop the immediate harm → name the decision owners → fix the root cause → prove the fix worked.**

That's the kind of situation where I find the ITIL guiding principles genuinely practical. “Think and work holistically” is not just an exam answer. It changes what questions I ask before anyone commits the team to a solution.

## How I use the seven guiding principles as a leader

| ITIL guiding principle | My plain-English leadership question |
| --- | --- |
| Focus on value | Who is better off when this work is finished? |
| Start where you are | What do the data, current architecture and team experience already tell us? |
| Progress iteratively with feedback | What is the smallest safe change that will teach us something? |
| Collaborate and promote visibility | Who needs to know, and who actually decides? |
| Think and work holistically | What breaks upstream or downstream if I only fix my team’s piece? |
| Keep it simple and practical | What can we remove without removing necessary safety? |
| Optimise and automate | Have we improved the process before automating it? |

## My skill-assessment method: explain it, apply it, prove it

I don't want to treat this as another checklist of certifications. For each practice relevant to the role I want, I ask myself three things:

1. **Can I explain it** to an engineer and to a business stakeholder without hiding behind terminology?
2. **Have I applied it** when a trade-off, dependency or incident really mattered?
3. **Can I prove the outcome** through a decision, measurement, document, demonstration or a story from my work?

For an Iteration Lead, proof might be a dependency board and a measurable reduction in delays. For an Engineering Manager, it should include engineering direction **and evidence of growing people**, not just delivery. For an Operations Manager, it might be a recovery exercise, a repeat-incident reduction or a useful set of reliability targets.

The transition I am working towards is not to “become more technical” in the abstract. It is to **combine my engineering foundation with delivery, people leadership and operational judgement**.

## The complete 34-practice learning matrix

This matrix is a *development guide*, not official PeopleCert role mapping and not a RACI for Google or any financial-services organisation.

**H = develop deep working capability; W = be able to apply and partner; A = understand the purpose and who owns it.** The role columns are illustrative learning priorities, not a ranking of the jobs.

### General management practices (12)

| ITIL practice | Google-style IL | Finance IL | Google-style EM | Finance EM | Google-style Ops | Finance Ops | Capability it develops |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Architecture management | A | A | H | H | W | W | Architecture standards and design trade-offs |
| Continual improvement | H | H | H | H | H | H | Hypothesis → measure → sustained change |
| Knowledge management | H | H | W | W | H | H | Reusable decisions, runbooks and learning |
| Measurement and reporting | H | H | H | H | H | H | Decisions from trusted evidence |
| Organizational change management | W | W | W | W | W | W | Adoption of changed ways of working |
| Portfolio management | A | W | W | W | W | W | Prioritise investment and capacity |
| Project management | H | H | W | W | W | W | Scope, dependencies and coordination |
| Relationship management | H | H | H | H | H | H | Influence, align, agree decision rights |
| Risk management | W | H | W | H | W | H | Make risks and mitigations explicit |
| Strategy management | A | W | H | H | W | W | Turn vision into coherent priorities |
| Supplier management | W | H | W | H | W | H | Vendor performance and interfaces |
| Workforce and talent management | A | A | H | H | H | H | Hire, develop, deploy and retain talent |
### Product/service management practices (22)

| ITIL practice | Google-style IL | Finance IL | Google-style EM | Finance EM | Google-style Ops | Finance Ops | Capability it develops |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Availability management | A | W | W | W | H | H | Architect and verify resilience |
| Business analysis | W | H | H | H | W | W | Define business needs and outcomes |
| Capacity and performance management | A | W | H | H | H | H | Predict performance, scale and cost |
| Change enablement | W | H | W | H | H | H | Make change risk-aware and safe |
| Deployment management | W | W | H | H | H | H | Ship into runtime safely |
| Incident management | A | W | W | W | H | H | Restore service and communicate |
| Information security management | W | H | H | H | H | H | Safeguard data and systems |
| IT asset management | A | A | A | W | W | H | Know/manage valuable IT assets |
| Infrastructure and platform management | A | W | W | W | H | H | Build and run platform infrastructure |
| Monitoring and event management | W | W | H | W | H | H | Observe, detect and act |
| Problem management | A | W | W | W | H | H | Prevent repeat failures |
| Release management | W | H | H | H | H | H | Release readiness and coordination |
| Service catalogue management | A | A | A | W | W | H | Offerings, consumers and ownership |
| Service configuration management | A | W | W | W | H | H | Track components and dependencies |
| Service continuity management | A | W | W | H | H | H | Recovery and continuity under disruption |
| Service design | W | W | H | H | H | H | Design service experience and operability |
| Service desk | A | A | A | A | W | H | User-facing support and routing |
| Service financial management | A | W | W | W | H | H | Understand cost and value of service |
| Service level management | W | W | H | W | H | H | Service expectations, SLA/SLO |
| Service request management | A | A | A | A | W | H | Fulfil standard user requests |
| Service validation and testing | W | H | H | H | W | W | Prove readiness and fitness for use |
| Software development and management | W | W | H | H | H | W | Build sustainable and secure software |

## My practical next step

I will pick one role, highlight its **H** practices and build a short example for each one: What was happening? Who had the authority? What did we decide? What trade-off did we make? What improved?

Because I have worked in both engineering and enterprise delivery, my immediate challenge is not learning every management acronym. It is demonstrating broader **engineering accountability, people development and system-level decisions** with the same confidence I bring to delivery coordination.

That feels like a much clearer career plan than collecting another title.

---

### Sources and important distinction

The ITIL practice names and seven guiding principles come from the framework. The role-to-practice connections above are my own learning interpretation. Google is an *illustrative* product-technology benchmark, not a claim about its official internal reporting lines. Financial-services examples reflect the kinds of responsibilities encountered in banking, insurance and superannuation technology.

- [PeopleCert — ITIL (Version 5) and 34 practices](https://www.peoplecert.org/help-and-support/faq-itil)
- [PeopleCert — ITIL Foundation (Version 5)](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-5-foundation-version-50-4154)
- [Google — Site Reliability Engineering: an introduction](https://sre.google/sre-book/introduction/)
- [Google SRE — incident management and reliability signals](https://sre.google/resources/practices-and-processes/incident-management-guide/)
- [Google Careers — Engineering Manager example](https://www.google.com/about/careers/applications/jobs/results/130322727708828358-engineering-manager-people-ops-engineering)

*Written as a personal professional reflection, not a statement of employer policy or a substitute for reviewing a real job description.*
