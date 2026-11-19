---
layout: post
title: "ITIL 5 Study Notes – Part 2: From Governance to Value Streams, Improvement and AI"
date: 2026-11-18 17:48:00 +1000
categories: Management_Practices
tags: [ITIL, Service-Management, Governance, Value-Streams, Continual-Improvement, DevOps, AI]
description: "Independent ITIL Foundation Version 5 learning notes covering governance, all 34 management practices, continual improvement, value stream mapping, complexity, the AI 6C model and the relationship with DevOps and PRINCE2."
---

> **Study status:** These are my personal learning notes while preparing for ITIL® Foundation (Version 5). I have not yet obtained the certification. The examples are fictional and are not descriptions of a particular employer or verified business outcomes. Use official training material for exact exam terminology.

*ITIL® Foundation (Version 5) — Part 2: How the Operating Model Actually Works*

*Governance, management practices, continual improvement, value streams, complexity, AI, DevOps and PRINCE2 — explained through enterprise technology delivery.*

In **Part 1**, I explored the foundation: opportunity and demand, value, products and services, the four dimensions, guiding principles, the eight lifecycle activities, and the difference between outputs and outcomes.

One question remained: **Who makes the decisions, who does the work, how does work flow, and how do we know it is getting better?**

That is the focus of Part 2. My goal is to connect the terms into a mental model I can actually use in a delivery or service leadership role, rather than memorising isolated definitions.

## The 60-second mental model

| Think about… | ITIL concept | The question it answers |
| --- | --- | --- |
| **Direction and accountability** | Governance | Who decides, on what basis, and who is accountable? |
| **Organisational capability** | Management practices | Which people, skills, processes, information and tools make the work possible? |
| **Building blocks of work** | Value chain / lifecycle activities | What types of activities do we combine? |
| **The actual journey of work** | Value stream | How does a particular need flow through the organisation? |
| **Learning and adaptation** | Continual improvement | Are the results improving, and what should change next? |

**My shorthand:** *governance provides direction; practices provide capability; a value stream connects the work; continual improvement tests whether it is producing better outcomes.* These are connected elements of the ITIL Value System, not rigid organisational layers.

![A practical mental model linking governance, management practices, value streams and continual improvement]({{ '/assets/img/itil5-part2-operating-model.svg' | relative_url }})

---

## 1. Governance: decisions, direction and accountability

Governance is the means by which an organisation is **directed and controlled**. It establishes how strategies, policies, decisions and accountability are handled. It is not the same as doing day-to-day delivery work, although governance decisions shape that work.

My notes use four interconnected activities:

| Governance activity | What happens | Example in a digital claims service |
| --- | --- | --- |
| **Engage stakeholders** | Understand needs, obligations and accountability. | Speak with claims operations, risk, technology and the platform supplier about a proposed change. |
| **Evaluate** | Assess options, performance, relationships, risks and alignment to strategy. | Compare the business impact, cost, security and dependency risks of two approaches. |
| **Direct** | Establish direction, policies, decisions and assigned responsibilities. | Approve an approach, define decision rights, and assign owners for delivery and controls. |
| **Monitor** | Assess performance and conformance against agreed direction. | Review service measures, outstanding risks, incidents, control evidence and expected benefits. |

The feedback loop matters. Monitoring may reveal evidence that changes the next evaluation and decision. **A governance meeting is not effective merely because it took place; it must lead to clear decisions, ownership and follow-through.**

![Governance cycle: engage, evaluate, direct and monitor, with monitoring informing the next evaluation]({{ '/assets/img/itil5-part2-governance-cycle.svg' | relative_url }})

### Governance versus management

Consider an external correspondence platform that has repeated failures:

- **Governance** determines risk appetite, approves material investment or exceptions, sets policies and ensures accountability.
- **Management** assesses the incidents, coordinates the vendor, makes authorised operational decisions, prioritises work and reports evidence.
- **The delivery and operations teams** analyse, design, build, test, deploy, operate and support the relevant changes within their delegated authority.

The boundaries depend on the organisation. A manager can hold delegated decisions; a governance body should not micromanage every ticket. Equally, a delivery lead should not silently accept risks that exceed their authority.

**A useful leadership question:** *Is this a decision I can make, a recommendation I must bring, or a risk I must escalate?*

---

## 2. Management practices: the capability behind the work

A **management practice** is a set of organisational resources designed for performing work or accomplishing an objective. It is broader than a process. A practice can bring together people, roles, skills, procedures, policies, partners, information and technology.

ITIL Version 5 retains **34 management practices**, grouped into **12 general management practices** and **22 product and service management practices**. This is a useful change in how the practices are organised compared with the three-group presentation in ITIL 4.

### 2.1 General management practices (12)

| Practice | My practical memory cue |
| --- | --- |
| Architecture management | Architectural direction, standards and trade-offs. |
| Continual improvement | Improve products, services, practices and results. |
| Knowledge management | Make dependable knowledge available and reusable. |
| Measurement and reporting | Turn evidence into decisions, not just dashboards. |
| Organisational change management | Help people adopt and sustain change. |
| Portfolio management | Balance investments, priorities and capacity. |
| Project management | Deliver defined change within agreed controls. |
| Relationship management | Build and maintain useful stakeholder relationships. |
| Risk management | Understand uncertainty and manage exposure. |
| Strategy management | Set direction in line with organisational objectives. |
| Supplier management | Manage third-party capability and obligations. |
| Workforce and talent management | Develop and sustain the right skills and capacity. |

### 2.2 Product and service management practices (22)

| Practice | My practical memory cue |
| --- | --- |
| Availability management | Is the service available as agreed? |
| Business analysis | What need are we solving, and what must change? |
| Capacity and performance management | Can the service handle the expected demand? |
| Change enablement | Are changes assessed and authorised appropriately? |
| Deployment management | How do changed components enter an environment? |
| Incident management | Restore disrupted service as quickly as appropriate. |
| Information security management | Protect information and manage security risk. |
| Infrastructure and platform management | Maintain the underlying technology platforms. |
| IT asset management | Manage technology assets through their lifecycle. |
| Monitoring and event management | Detect and interpret significant changes of state. |
| Problem management | Reduce causes and impacts of actual or potential incidents. |
| Release management | Make new or changed capabilities available for use. |
| Service catalogue management | Make agreed service offerings understandable. |
| Service configuration management | Maintain reliable information on service configurations. |
| Service continuity management | Prepare for severe disruption and recovery. |
| Service design | Shape services to meet needs and constraints. |
| Service desk | Provide a point of contact for users and requests. |
| Service financial management | Understand service costs, budgets and financial decisions. |
| Service level management | Agree, review and improve service levels. |
| Service request management | Fulfil predefined, normal service requests. |
| Service validation and testing | Check whether solutions meet defined requirements. |
| Software development and management | Build, change and maintain software effectively. |

The list can look like 34 departments. **It is not an organisational chart.** An organisation might have one team performing several practices, or several teams contributing to one practice. Nor must every practice be implemented with identical depth for every product or service.

### 2.3 Enabling versus supporting a lifecycle activity

My notes distinguish two ways a practice contributes to a value-chain activity:

- **Enabling (E):** its work participates directly in the activity.
- **Supporting (S):** it provides information, methods or other assistance without directly performing that activity.

For example, during **Transition**, deployment management might directly enable deployment, while knowledge management supports it with runbooks and handover information. The classification can vary across activities and the operating model; it is not a permanent ranking of practices.

**Important distinction:** a *process* is a coordinated set of activities; a *practice* is the broader capability required to perform work; a *value stream* is the end-to-end journey for a particular need. One practice can use several processes and contribute to several value streams.

---

## 3. Continual improvement: not the same as delivering more features

An improvement should be connected to a need and verified through evidence. Finishing an action does not automatically mean the underlying result improved.

The **six questions** in the Version 5 continual improvement model give me a practical sequence:

| Step | Question | What I would do in practice |
| --- | --- | --- |
| 1 | **What is the vision?** | Agree the problem and the business outcome. |
| 2 | **Where are we now?** | Collect a baseline: delay, error rates, experience, capability and constraints. |
| 3 | **Where do we want to be?** | Define a realistic target state and the critical conditions for success. |
| 4 | **How do we get there?** | Choose an iterative plan, owners, resources and controls. |
| 5 | **Take action.** | Try improvements, manage adoption and record results. |
| 6 | **Are we getting there?** | Compare evidence with the target, learn and adjust. |

![Six-step ITIL continual improvement loop, returning to vision after checking results]({{ '/assets/img/itil5-part2-continual-improvement.svg' | relative_url }})

For me, the key is what happens *after* step six. Continue the improvement, adjust the target, reprioritise, or stop an experiment if conditions have changed. Keep what works by updating the actual ways of working, knowledge, training and ownership. Transparent reporting includes **what did not work**.

### CSF, KPI and metric: related, but not identical

- **Critical success factor (CSF):** a condition needed to achieve the intended result. For example, claims staff must be able to trust the accuracy of outgoing correspondence.
- **Key performance indicator (KPI):** a selected measure used to judge performance against an important objective. For example, the percentage of correspondence delivered within the agreed service level.
- **Metric:** a measurement or calculation used to assess or monitor something. For example, queue depth, elapsed processing time or retry count.

Not every metric is a KPI, and not every improvement should be reduced to a single target.

### Goodhart's law: when the measure distorts the work

Suppose the service desk is measured only on **average call duration**. Agents may end calls quickly while leaving issues unresolved. The reported number improves while user experience deteriorates.

A more balanced set of indicators might look at resolution quality, repeat contacts, response and restoration time, and user feedback alongside throughput. The principle is not that targets are bad: it is that **the choice of target changes behaviour**.

**Question I want to ask before adopting a dashboard:** *If a team optimised only this number, what might become worse?*

---

## 4. Value-stream mapping versus value-stream management

Part 1 introduced the difference between **value chain**, **value stream**, and **process**. Here is what I needed to understand next:

- **Value-stream identification** chooses the journey worth studying and defines its start, end, consumer and boundaries.
- **Value-stream mapping** is an exercise to visualise and analyse how work and information actually flow — including handoffs, delays, rework and decisions.
- **Value-stream management** is ongoing oversight and optimisation of that flow, using evidence and periodically updating the map.

**Mapping gives us a picture. Management ensures we use the picture to improve the system.** A beautiful diagram in a workshop is not, by itself, value-stream management.

### The five-step mapping approach

1. **Identify the value stream.** Choose a specific consumer need and a meaningful boundary.
2. **Map the current state (“as is”).** Follow real work across people, teams, suppliers and systems. Include information and artefacts, not just boxes on a Jira board.
3. **Analyse the flow.** Examine bottlenecks, queues, waiting, rework, unnecessary approvals and missing ownership.
4. **Design the future state (“to be”).** Simplify flow, improve visibility, clarify decisions and address avoidable dependencies.
5. **Plan and implement improvements.** Agree accountable owners, try changes, collect feedback and revisit the map.

### Example: a correspondence-change request

Imagine a business team asks for a small change to a claims letter. The work travels through business triage, analysis, supplier estimation, prioritisation, build, testing, change approval and release.

The developer may need just a short change, while most elapsed time is spent waiting between steps. The central question becomes **“Where is the work waiting, and what creates that wait?”**, not simply “Why is the developer slow?”

![Example of an as-is and future-state correspondence value stream with handoffs made visible]({{ '/assets/img/itil5-part2-value-stream.svg' | relative_url }})

The future-state example reduces unnecessary rework through clearer intake, earlier cross-functional clarification and visible supplier dependencies. It does **not** mean removing necessary compliance, testing or change controls. Those controls may protect the value the service is meant to provide.

A mapping workshop should involve the people doing the work. Compare the map with real tickets, communication threads and observed practice. Otherwise, we risk documenting the **official process** while missing the **actual flow**.

### Questions worth asking

- Where does the request begin, and when does the consumer receive the useful outcome?
- Which steps are active work, and which are waiting?
- Who is authorised to make each decision?
- Where is information passed around, lost or repeatedly clarified?
- Which dependencies are within our control, and which require supplier agreement?
- How do we know whether the new flow improves outcomes rather than only speed?

---

## 5. Complexity: why an operating model cannot be copied blindly

Enterprise delivery is not always a neat sequence of predictable tasks. There can be multiple vendors, legacy integrations, competing priorities, security obligations, uncertain demand and changing customer needs.

A **complicated** problem may have many parts but be analysable with sufficient expertise. A **complex** situation also involves interacting people and systems, feedback loops and outcomes that cannot be completely predicted in advance.

For complexity, my notes highlight these useful behaviours:

| Behaviour | Practical interpretation |
| --- | --- |
| **Iterative and adaptive** | Work in smaller increments and inspect actual results. |
| **Experimentation** | Test a hypothesis rather than assuming a design will work. |
| **Autonomy** | Delegate decisions within clear risk and policy boundaries. |
| **Loose coupling** | Reduce unnecessary dependencies and fragile handoffs. |
| **Transparency** | Make work, constraints, owners and risks visible. |
| **Continuous learning** | Incorporate evidence instead of defending the original plan. |
| **Flexibility** | Adapt the workflow to context without abandoning needed controls. |

**A single operating model is not universally right.** A low-risk internal enhancement may need different approval and assurance arrangements from a change to regulated financial-service payments. The goal is proportionate coordination and control, not ceremony for its own sake.

### What this means for an Iteration Lead or Delivery Lead

One idea became particularly clear for me: **facilitating every meeting is not the same as leading delivery**.

Business analysts can clarify requirements. Engineers can estimate. Testers can coordinate test evidence. A product owner can prioritise. A supplier lead can speak directly with the vendor. This can be a healthy operating model *if decision rights and accountabilities are clear*.

The delivery leader's contribution may instead be to connect the full picture:

- **Outcome:** What value is expected, and who owns the benefit after release?
- **Flow:** Where are the dependencies, blocked decisions and recurring wait states?
- **Trade-offs:** What changes when scope, capacity, risk or dates conflict?
- **Transparency:** Does everyone see the same plan, constraints, confidence and decisions?
- **Readiness:** Are release, support, operational ownership and recovery arrangements understood?
- **Improvement:** What is slowing the system, and what experiment should we run next?

If all meaningful decisions occur elsewhere and the role is limited to recording status, the issue may be **role design and delegation**, not a lack of ceremonies. That requires an explicit conversation about the operating model rather than an attempt to seize work from specialists.

**My leadership prompt:** *What decision, coordination or improvement would be missing if I were absent this week?*

---

## 6. ITIL and AI: the six Cs — and the governance question

AI is not only about generating text. The ITIL AI Capability Model groups functional capabilities into **six Cs**. My practical examples are shown below; many solutions combine several capabilities.

| Capability | What the AI does | Example in enterprise service management |
| --- | --- | --- |
| **Creation** | Produces new material. | Draft a knowledge article or a first version of release notes. |
| **Curation** | Improves existing information. | Flag duplicate or outdated support articles. |
| **Clarification** | Makes existing content easier to understand. | Summarise an incident history or explain a policy in plain language. |
| **Cognition** | Finds patterns and supports analysis. | Identify repeating incident clusters or forecast workload peaks. |
| **Communication** | Interacts with users or stakeholders. | Provide a service chatbot or tailored status updates. |
| **Coordination** | Initiates or orchestrates actions. | Route requests, request approvals or trigger a governed remediation workflow. |

![The ITIL six-Cs AI capability model with an enterprise service management example for each capability]({{ '/assets/img/itil5-part2-ai-six-c.svg' | relative_url }})

### The distinction I care about: advice versus action

An AI tool that **drafts** a suggested incident update creates a different risk from an agent that **sends** that update, changes production configuration or closes a ticket without review. The more autonomy and system access involved, the greater the need for proportionate assurance.

Before using AI in a financial-services workflow, I would ask:

1. **Purpose:** Which outcome does this improve, and what evidence supports the use case?
2. **Data:** Is the information accurate, current, authorised and appropriately protected?
3. **Authority:** Can AI only suggest, or can it take action? Who approves or can override it?
4. **Controls:** What testing, audit trail, access limits and rollback or recovery arrangements exist?
5. **Accountability:** Who owns model performance, incidents, errors and ongoing monitoring?
6. **Learning:** How will we detect unintended effects and change or suspend the use case?

### AI maturity is more than having an AI pilot

An organisation becomes more capable when it can repeat useful AI outcomes with reliable information, skilled people, defined controls, monitoring and a way to respond to errors. A demonstration that produces a convincing draft is not the same as a governed production service. This is a practical interpretation of maturity, not a claim that every organisation must follow a fixed sequence of maturity levels.

**AI should strengthen judgement, not become an excuse to remove accountability.** In regulated contexts, privacy, security, reliability, compliance and human oversight are design requirements rather than post-release extras. AI outputs can be wrong even when they sound confident; the quality of data, model behaviour and surrounding controls all matter.

---

## 7. ITIL, DevOps and PRINCE2: different lenses on the same enterprise

These approaches are often discussed as competitors. My learning is that they answer different questions and can be used together.

| Approach | Primary lens | Useful question |
| --- | --- | --- |
| **ITIL** | Managing and improving digital products and services across their lifecycle. | How are useful, reliable services created, delivered, supported and improved? |
| **DevOps** | Collaboration, automation, feedback and operational practices across software delivery and operations. | How can teams build, release, operate and learn safely and frequently? |
| **PRINCE2 Project Management** | Structured governance, organisation and control of a project. | How do we justify, direct, manage and close this defined change initiative? |

For example, an organisation replacing a legacy correspondence integration could use **PRINCE2** to manage a time-bound replacement project, **DevOps** practices for build pipelines, automated tests, deployment and operational feedback, and **ITIL** practices for service design, supplier management, change enablement, incident response and continual improvement.

This is a useful simplification, **not** a claim that ITIL only specifies *what* and DevOps only specifies *how*. Each contains principles and practical guidance, and the organisation must make the combined operating model coherent.

The test is whether the combination improves outcomes with appropriate risk management — not how many framework names appear on a slide.

---

## 8. Putting it together: one fictional service scenario

**Scenario:** Claims operations reports that some digital correspondence is not reaching members. A supplier owns the external correspondence platform; an internal team owns the integration and claims workflow. It is initially unclear where the failure occurs.

| Lens | What I would ask or do |
| --- | --- |
| **Value and outcome** | Who is affected? What member or business harm occurs when communication is delayed? |
| **Governance** | Which decisions can the response team make, and which need risk, product or executive approval? |
| **Incident management** | Confirm scope, severity and restoration options; communicate known impact and uncertainty. |
| **Problem management** | Investigate recurrence, technical causes, known errors and longer-term prevention. |
| **Supplier management** | Clarify ownership, evidence, escalation, contractual obligations and joint next steps. |
| **Value-stream mapping** | Trace the correspondence from triggering event through integration, supplier, delivery and status feedback. |
| **Change / release / deployment** | Introduce the fix with appropriate testing, authorisation, readiness and rollback controls. |
| **Continual improvement** | Compare post-change evidence with the original baseline, update runbooks and track residual risks. |
| **AI, if used** | Assist with summarisation or pattern detection without allowing uncontrolled customer communication or production actions. |

The important point is not to personally perform every activity. **Leadership means making sure the right responsibilities, decisions and feedback loops connect across the service.**

---

## 9. The language I want to use in real meetings

| When I hear… | I want to ask… | Connection |
| --- | --- | --- |
| “We have a governance meeting.” | What decision will be made? Who owns it? What evidence is required? | Governance |
| “We have a process.” | Does it reflect how work really happens, including waiting and handoffs? | Process and value-stream mapping |
| “The sprint was completed.” | What was made available, and what changed for the consumer? | Output versus outcome |
| “The vendor is handling it.” | Who owns the end-to-end service risk, decision and communication? | Supplier and relationship management |
| “Our KPI is green.” | Could the metric be hiding poor experience or rework? | Measurement and Goodhart's law |
| “We are improving.” | Compared with what baseline, and what has been learned? | Continual improvement |
| “AI can automate this.” | What level of autonomy is appropriate and who remains accountable? | AI governance |

Framework vocabulary is useful only when it creates shared understanding. I would rather ask one clear question that exposes an important decision than deliver a perfect definition nobody can act on.

---

## 10. Quick self-test

1. A supplier performs deployments and a delivery lead coordinates releases. Does that automatically determine who owns change authorisation?
2. What is the difference between a management practice, a process and a value stream?
3. A team shortens average ticket handling time, but repeat contacts increase. Is that enough evidence of improvement?
4. Why does the continual improvement model need a current-state baseline?
5. What is the difference between mapping a value stream once and managing that value stream over time?
6. A proposed AI agent can reset production configuration without a person reviewing it. What governance questions come first?
7. Can an organisation use ITIL, DevOps and PRINCE2 together without making every activity bureaucratic?

<details markdown="1">
<summary><strong>Suggested answers — expand after trying the questions</strong></summary>

1. No. Deployment, release and change-authorisation accountabilities must be explicitly defined in the operating model and applicable policies.
2. A practice is organisational capability; a process coordinates inputs and activities into outputs; a value stream follows end-to-end work for a particular need.
3. No. Examine repeat incidents, resolution quality, user experience and overall outcomes; a target can distort behaviour.
4. Without a baseline, claims of improvement are weak and may confuse correlation with an effect of the change.
5. Mapping visualises and analyses a flow; management monitors, adapts and improves it continually.
6. Define purpose, authorisation, access, safeguards, auditability, failure behaviour, human oversight and accountability before permitting action.
7. Yes. Apply each where it adds value, align decision rights and use proportionate controls.

</details>

## Final takeaway

The insight I am taking from ITIL Version 5 is that **good delivery is not the efficient movement of tickets through a team**. It is the coordination of capabilities, decisions, relationships and feedback so a service actually produces value.

Governance should make responsible decisions possible. Practices should enable work. Value streams should expose how work really moves. Improvement should be measured against outcomes. AI and automation should extend capability without erasing accountability.

**The question to carry into my next delivery role: “Are we managing the work — or are we improving the system that produces the outcome?”**

---

## Sources and attribution

- [PeopleCert — ITIL Foundation (Version 5)](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-5-foundation-version-50-4154)
- [PeopleCert — ITIL frequently asked questions](https://www.peoplecert.org/help-and-support/faq-itil)
- [ITIL — What is new in Version 5](https://www.itil.com/Itil-News-and-Announcements/itil-version-5-explained)
- [ITIL — AI Governance white paper and the six-capability model](https://itil.com/Itil-News-and-Announcements/ai-governance-white-paper)
- [ITIL — Where do you start with ITIL? Continual improvement](https://www.itil.com/Itil-News-and-Announcements/where-do-you-start-with-ITIL)

*These are independently written study notes, not an official ITIL training publication. ITIL® is a registered trademark of the PeopleCert group. Diagrams are original explanatory illustrations, not reproductions of official framework figures. Verify precise exam definitions against your licensed course material.*
