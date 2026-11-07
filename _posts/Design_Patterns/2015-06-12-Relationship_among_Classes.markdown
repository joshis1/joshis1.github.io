---
layout: post
title:  "Relationships Between Classes: Inheritance, Association and Composition"
date:   2015-06-12 14:13:31 +1300
categories: Design_Patterns
description: An introduction to class relationships, inheritance, association, aggregation, composition, and C++ access modes.
---

Class relationships are a foundation of object-oriented design. Two useful questions are whether one type can substitute for another (“is-a”) and whether an object collaborates with or owns another object (“has-a”). Prefer modeling the behavior and lifecycle you need over choosing inheritance solely to reuse code.

## Inheritance: an “is-a” relationship
The easiest way to identify the candidate for inheritance is by asking yourself
a quest ion – “Is this new candidate “is a” / kind /sub-type of an old
candidate?.” If the answer is yes, then it is very much suitable for inherit ance.
Now, the new candidate is the derived class, and the old candidate is the
base class. In short , the inheritance depicts the relationship – “is a”. As you
can identify, this is a uni-directional relationship. It means that the derived
class is a type of base class. However, the base class is not a type of derived
class. In summary, you can create a specialised form from a generic form. On
the contrary, the generic form cannot be created from the specialized form. In
OOps, the generic form can be an abstract class or an interface class. Later,
we will see generalization and realization in inheritance.

Example – PVR Set top box is a type/kind of Settopbox(STB). Here, the STB
is the base class, and the PVR STB is a derived class.

## Association and composition: “has-a” relationships
The easiest way to identify the candidate for composition is by asking
yourself a question – “Is this new candidate has an old candidate?. If the
answer is yes, then it is very much suitable for composition. Here, the new
candidate “has a/an” old candidate. In short , the composition depicts
relationship – “has a”. As you can identify, this is a uni-directional
relationship. It means that the new candidate contains the old candidate.
However, the old candidate doesn’t contain the new candidate.

Example – Settop box has a tuner. Here, the STB class contains another
class object – tuner, as a member variable. Later, we will see the aggregation
and composition. Also, aggregation is called a weak composition. On the other
hand, composition is called a strong composition. Later, we will see why
they are called so.
## Association
These terms are not only useful in creating the logical diagrams i.e. class
diagrams, but also they are useful from design aspects.

Association - This term is used to describe the relationship/dependency
between classes.

General Association – This tells what other class/classes a class needs to
perform a particular service. Based on the number of dependencies, the
multiplicity is defined. The multiplicity can be one to one, one to many, many
to one, and many to many.


<img src="/assets/img/One_to_one_Association.png" alt="One_to_one_Association">


Directional Association – This association tells about what object is
contained by the other object . Here, the direction is essential to express the
relationship. For example, whether class A contains class B or class B contains
class A.

<img src="/assets/img/Directional_Association.png" alt="Directional_Association">

## Aggregation and composition
1. **Aggregation** – Also, this is called a weak composition. Here, the object
that is contained by the new object can exist independently. The life time of
the contained object is not controlled by the container object . Generally, the
contained object is passed to the constructor of the container object . There
is an advantage of aggregation – the coupling between classes are not
strong. The dependent objects are passed to the new object by the client . In
my opinion, this is a neat design. Personally, I prefer aggregation over
composition.
Example- In a STB, HDD has a fan. Both HDD and fan can exist independently.
Here, the coupling between them is not strong. Both the objects HDD and Fan
can exist independently. If HDD is killed, then FAN can exist . In short , the Fan can keep spinning even when the HDD is dead. This example is just to show
the concept of the aggregation in terms of the life time of contained and
container object . While programming/designing composition, we just think in
terms of loosely coupled or tightly coupled classes.

<img src="/assets/img/Aggregation.png" alt="Aggregation">

2. **Composition** - Also, this is called a strong composition. Here, the object
that is contained by the new object cannot exist independently. The life time
of the contained object is controlled by the container object . Many people
refer ‘composition’ as a special case of ‘aggregation’.
Example- Front Panel has a LED. Here, the LED cannot exist without a
Front Panel. If the Front Panel dies, the LED on the Front Panel dies. In such a
case, the LED life time is associated with the life time of Front Panel. Here,
the coupling between them is strong.

<img src="/assets/img/Composition.png" alt="Composition">

## Abstract classes and interfaces
Before we dive into inheritance, let’s understand the two types of classes.
a. **Abstract class** – This is a blue print – model of the object . However, it
cannot be instantiated. An abstract class has a few general methods implemented.
They generally have protected member variables that can be inherited by the
sub-class/derived class. However, there are a set of methods, which are not
implemented . It is expected that the derived class will extend the property of
abstract class. Also, the derived class will implement the not implemented
methods of the abstract class. In C++, we make the abstract class by putting
the keyword ‘virtual’ and equating the method to zero. For example, the
following is the syntax to make the class abstract in C++.

{% highlight cpp %}

/* a pure virtual function * /
virtual void unImplementedMethod(void) = 0;

{% endhighlight %}

b. **Interface class** – In C++, an interface is a design convention, not a special language construct. A class intended as an interface often exposes pure virtual operations and a virtual destructor. C++ does not prohibit it from having data members or implemented methods, but keeping an interface focused makes it easier to use.

**How an ‘Inheritance’ is synthesized ?**
1. **Generalization** – Here the derived class extends the abstract class.
Basically, the base class – Abstract class is a generalized class. Here, the
derived class is a specialized class.

<img src="/assets/img/Generalization.png" alt="Generalization">

2. **Realization** – Here the derived class implements the interface class.

<img src="/assets/img/Realization.png" alt="Realization">

## Private inheritance in C++

Private inheritance is not composition. It models implementation inheritance: the derived class is implemented in terms of a base class, but the public subtype relationship is hidden from callers. For ordinary object composition, store the collaborator as a data member instead. Private inheritance can be useful when the derived type needs access to a base implementation or when a specific library technique requires it, but it should be chosen deliberately.

**Property of Private inheritance -**
1. Base-class private members remain part of the base subobject but are inaccessible by name in the derived class.
2. Base-class public and protected members are accessible to the derived class as private members.

The following legacy example demonstrates access through private inheritance. It is not an example of composition; a member field would be the clearer design if the goal were simply to contain another object.

{% highlight cpp %}

#include <QtCore/QCoreApplication>
#include <QDebug>
class BaseClass
{
  private:
    QString baseClassName;
  public:
    void setBaseClassName(QString bName)
{
  baseClassName = bName;
}
QString getbaseClassName()
{
  return baseClassName;
}
virtual ~BaseClass()
{

}

};

class DerivedClass: private BaseClass
{
public:
  void printtheBaseClassName()
{
  qDebug()<<"The name of base Class is "<<getbaseClassName();
}

DerivedClass()
{
  qDebug()<<"The Derived class object is Constructed";
}
void settheBaseClassNameFromDerived(QString DerivedName)
{
  setBaseClassName(DerivedName);
}
};

int main(int argc, char * argv[])
{
  QCoreApplication a(argc, argv);
  DerivedClass * pDerived = new DerivedClass;
  pDerived->settheBaseClassNameFromDerived("COMPOSITION from Inheritance");
  pDerived->printtheBaseClassName();
  delete pDerived;
  return a.exec();
}

{% endhighlight %}

Here is the output –

<img src="/assets/img/Private_inheritance.png" alt="Private_inheritance">

These relationships are useful vocabulary for discussing class diagrams and making design trade-offs. Use them to communicate intent, then check that the resulting design supports the required behavior and object lifetimes.
