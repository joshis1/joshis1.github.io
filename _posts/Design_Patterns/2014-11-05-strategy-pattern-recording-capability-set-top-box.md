---
layout: post
title: "Strategy Pattern in C++: When a Set-Top Box Gains Recording Capability"
date: 2014-11-05 13:11:55
categories: Design_Patterns
description: "An original Tune2Wizard set-top-box use case for the Strategy Pattern, with runtime recordable and non-recordable policies and a modernised C++ example."
---

**How can the same set-top box behave like a PVR when a hard disk is attached, and like a simple zapper when no disk is available?**

That is the practical problem I used when I first wrote about the **Strategy Pattern**, also called the *Policy Pattern*. The important detail is that the disk's presence is known at **runtime**. I do not want to compile two entirely different versions of the playback logic just to handle a change in recording capability.

The solution is to **separate the behaviour that changes from the product that uses it**.

*Archive note: Originally published on Tune2Wizard on 5 November 2014. The original article used the names `ISTB`, `Irecords`, `pvr`, `zapper`, `recordable` and `nonRecordable`, and showed a UML model created in Umbrello. The C++17 code below is a newly written, memory-safe teaching adaptation of that original example, not a verbatim copy of the archived implementation.*

<img src="{{ '/assets/img/tune2wizard-strategy-pvr.svg' | relative_url }}" alt="Set-top box owns a recording strategy interface with Recordable and NotRecordable implementations selected at runtime" loading="lazy">

## First, define the problem

Imagine a generic set-top box that can play audio/video and change channels in either mode.

- **External hard disk present:** Recording and playback of stored content can be enabled (PVR capability).
- **External hard disk absent:** Live viewing and channel changing still work, but recording is unavailable (zapper behaviour).

The low-level driver detects the disk when the device boots. The application can then select its recording policy. The key is that **the hardware condition changes the policy, not the identity of the whole product**.

## The Strategy Pattern in one view

| Part | Responsibility in this example |
| --- | --- |
| Context | `SetTopBox` — exposes stable device operations and delegates recording behaviour |
| Strategy interface | `RecordingPolicy` — defines the recording operation |
| Concrete strategy | `Recordable` — recording is available |
| Concrete strategy | `NotRecordable` — recording is unavailable |
| Runtime decision | Hardware check or configuration selects the appropriate strategy |

My 2014 UML diagram represented a similar idea: `ISTB` had a relationship to an `Irecords` interface, with separate implementations of recording behaviour. The useful insight was **composition** — one object *has a* policy — rather than repeatedly copying the policy code into multiple device classes.

## A modern C++ version of that experiment

Here is the same idea written with C++17 and `std::unique_ptr`. It avoids the raw-pointer ownership ambiguity in my original code.

```cpp
#include <iostream>
#include <memory>
#include <utility>

class RecordingPolicy {
public:
    virtual ~RecordingPolicy() = default;
    virtual void record() const = 0;
};

class Recordable final : public RecordingPolicy {
public:
    void record() const override {
        std::cout << "Recording started\n";
    }
};

class NotRecordable final : public RecordingPolicy {
public:
    void record() const override {
        std::cout << "Recording unavailable: no disk attached\n";
    }
};

class SetTopBox {
    std::unique_ptr<RecordingPolicy> recordingPolicy;

public:
    explicit SetTopBox(std::unique_ptr<RecordingPolicy> policy)
        : recordingPolicy(std::move(policy)) {}

    void setRecordingPolicy(std::unique_ptr<RecordingPolicy> policy) {
        recordingPolicy = std::move(policy);
    }

    void playLiveTV() const {
        std::cout << "Playing live television\n";
    }

    void record() const {
        recordingPolicy->record();
    }
};

int main() {
    bool diskAttached = false; // Illustrative runtime hardware result
    SetTopBox box(std::make_unique<NotRecordable>());

    box.playLiveTV();
    box.record();

    diskAttached = true;       // Simulate connecting a hard disk
    if (diskAttached) {
        box.setRecordingPolicy(std::make_unique<Recordable>());
    }
    box.record();
}
```

Compile the independent teaching example with:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic strategy-set-top-box.cpp -o strategy-set-top-box
./strategy-set-top-box
```

Expected output:

```text
Playing live television
Recording unavailable: no disk attached
Recording started
```

The output is illustrative. This is a standalone teaching program; the original PDF's implementation was based on Qt classes and used `qDebug()` for its messages.

## Why composition helps

Without a policy interface, it is tempting to put every disk-detection `if` statement in the main set-top-box code or to create different products with duplicated playback and channel-changing logic. That can make new behaviours expensive to add.

With composition, I can introduce another policy — perhaps `RecordingDisabledByParentalControl` — without rewriting the main playback class. But this is not a rule that every simple `if` should become a design pattern. Strategy makes sense when the **behaviour varies independently and is meaningful enough to encapsulate**.

The original example used two concrete products, a PVR and a zapper. The revised version makes the runtime switch particularly clear by changing the strategy of one existing box. That is an intentional teaching improvement, not a claim about what the original code did at runtime.

## A useful distinction: interface versus abstract class

In C++, an abstract class has at least one pure virtual function. It may also include data and implemented methods. What we informally call an *interface* is commonly an abstract base with pure virtual operations and a virtual destructor; C++ does not have a separate `interface` keyword in the language.

That matters because the policy type represents a **contract**. The set-top box depends on the contract, not on the concrete recording implementation.

## The takeaway

In this experiment, the physical set-top box did not need to become a different object simply because its recording capability changed. What changed was the behaviour selected for that capability.

> **When something varies at runtime, isolate the varying policy and let the stable part of the system depend on an interface. That is the real value of Strategy.**

*Shreyas Joshi — originally published on Tune2Wizard, 5 November 2014. Source: personal archived PDF, `StrategyPatternArticle.pdf`. Original STB/PVR/zapper framing preserved; sample code intentionally modernised and distinguished from the original.*
