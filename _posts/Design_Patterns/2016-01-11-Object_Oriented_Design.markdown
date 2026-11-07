---
layout: post
title:  "SOLID Principles: A Practical Guide to Object-Oriented Design"
date:   2016-01-11 14:13:31 +1300
categories: Design_Patterns
description: An introduction to the SOLID principles and the trade-offs behind loosely coupled object-oriented software.
---
This article introduces the SOLID design principles and some of the trade-offs behind applying them.

**Why do we need Software Design Principles?**

These are the principles that should be used to avoid a bad software design.

**Properties of Object Oriented language**

1. Encapsulation – It refers to packing of data and functions into a single
component . This is done in the class.
2. **Information hiding** limits which implementation details callers can access. Getters and setters are optional; they are not a requirement for encapsulation.
3. **Abstraction** presents relevant behavior while hiding unnecessary implementation detail. Interfaces are one way to create an abstraction.
4. **Dynamic dispatch** selects an overridden method at runtime. A vtable is a common implementation technique, not a language requirement.
5. **Inheritance** expresses a subtype relationship when the derived type can safely stand in for the base type.
6. **Polymorphism** lets code work with multiple implementations through a common operation.
Common forms include method overloading and operator overloading. Programming to a useful abstraction can reduce coupling, but an interface is not automatically beneficial for every class.
Drawbacks of a tightly coupled code?
a. Rigidity – Basically, it means tightly coupled. When you change one piece
of code, everything needs to be changed.
b. Fragility – Since a code is tightly coupled, one change can lead to break of
the entire system. So, code is very fragile and is succumbed to the break
down of entire system.
c. Immobility – Since it is tightly coupled, it cannot be re-used by other
application.

Object-oriented design principles are often summarized by the acronym SOLID.

**SOLID stands for –**

a. S – Single Responsibility. <br>
b. O – Open Closed. <br>
c. L – LISKOV Substitution. <br>
d. I – Interface Segregation. <br>
e. D – Dependency Inversion. <br>

**Single Responsibility Principle (SRP)** – A module should have one coherent responsibility, or one primary reason to change. Separating unrelated responsibilities can improve testing and maintenance, but splitting every small operation into its own class can add needless complexity.

**Open/Closed Principle (OCP)** – Software should be open to the extensions a system needs while minimizing changes to stable behavior. Interfaces and composition can help, but inheritance is not the only technique. This is a design goal, not a reason to avoid all changes to existing code.

**Liskov Substitution Principle (LSP)** – A subtype should be usable wherever its base type is expected without breaking the base type's behavioral promises. Check preconditions, postconditions, and invariants, not just whether the subtype shares fields with the base type. The square/rectangle example illustrates the problem when a mutable rectangle promises independently settable width and height; the lesson is about the contract, not a blanket rule against that inheritance relationship.

**Interface Segregation Principle (ISP)** – It states that a client should not
depend on the methods that they don’t use. Again, this is related to
inheritance, we should not have a polluted or fat interfaces, which means that
the interface shouldn’t have methods that are unrelated or not required. We
shouldn’t clutter the interface class with the methods, which are not
related to the interface/class responsibility. Otherwise the class, which will implement the interface, has to unnecessary implement the un-related methods.
The methods, which are not related should be in the other interface. Thus, it is all about interface segregation.

[Example] – Here is a short program – ” the method get DttInfo() is not related
to contentMgr”. Thus, we have a separate interface for getting DttInfo(). This
program shows that the interface is segregated. There are two separate
interfaces – IcontentMgr and IdttInfo rather than combining the functionality
into one interface. Here the interface is segregated as the methods are
unrelated. The two interface classes are IdttInfo and IcontentMgr. The IdttInfo
is all about the dtt information. The IcontentMgr is all about content . They
are both unrelated, and they should have a separate interface.

{% highlight cpp %}

#include<iostream>
#include<string>
class IdttInfo
{
 public:
  virtual ~IdttInfo() = default;
    virtual bool isDttSupported() = 0;
};

class serviceMgrDttInfo:public IdttInfo
{
  public:
      virtual bool isDttSupported()
{
  return true;
}

};

class IcontentMgr
{
  public:
  virtual ~IcontentMgr() = default;
      virtual std::string getClassName() = 0;
};

class serviceContentMgr: public IcontentMgr
{
  private:
      IdttInfo * p_mDttInfo;
      serviceContentMgr();
  public:
      virtual std::string getClassName()
{
  return "serviceContentMgr";
}
serviceContentMgr(IdttInfo * pDttInfo):p_mDttInfo(pDttInfo)
{

}
};

int main()
{
  IdttInfo * pDttInfo = new serviceMgrDttInfo;
  IcontentMgr * pContentMgr = new serviceContentMgr(pDttInfo);
  std::cout<<pContentMgr->getClassName()<<std::endl;
  std::cout<<pDttInfo->isDttSupported();
  return 0;
}

{% endhighlight %}

**Dependency Inversion Principle ( DIP)** - This principle states that the high
level module shouldn’t depend on the low level modules directly. Instead, a
high level class should use interface class of a low level class in order to
abstract the direct call to a low level class. With the aid of this principle,
we decouple the software modules. When you decouple the modules, the
maintenance becomes easier. This principle should only be applied when you
think that the code can change in future. However, when you know that the
code may not change in future, there is no point of creating an extra class i.e.
Interface class for every class.

High Level Classes -> Abstraction via. Interface class of a Low Level Class -> Low Level Classes

This brings an end to the topic of Design Principles/Concepts in OOPs.
