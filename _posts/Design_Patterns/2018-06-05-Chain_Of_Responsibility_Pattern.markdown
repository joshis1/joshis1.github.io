---
layout: post
title:  "The Chain of Responsibility Pattern in C++"
date:   2018-06-05 10:13:31 +1300
categories: Design_Patterns
description: A C++ command-dispatch example that explains handlers, delegation, and trade-offs in a chain of responsibility.
---
The Chain of Responsibility pattern lets a request pass through a sequence of handlers. A handler can process the request or pass it to the next handler, reducing the sender's dependency on a specific receiver.

The C++ example below dispatches an enum value in one process. It is not an XMPP parser, transport, or security implementation.

**Difference between Structural and Behavioural Pattern**
1. Structural Pattern talks about the relationship between entities. For
example, Façade Pattern and Adapter Pattern.

2. Behavioural Pattern talks about how these entities communicate with each
other. For example, Strategy Pattern and Observer Pattern.
In the “Chain of Responsibility Principle”, we talk about how the command from
the client is delegated from one object to another. This talks about how the
message is delegated ( communicated) from one object to another. A chain
of responsibility decouples the sender and receiver. A sender will just post the
command on the pipeline. The objects which are connected to the pipeline will
either process the desired command or will just delegate to their next object.

**Task:**
A STB will receive the XMPP commands, the commands are for various
sub-modules. For example, reboot the box – by Power Manager of the box,
HDD health – by Storage Manager of the box, and code download – by the
Software Upgrade Manager of the box. Adding a handler can avoid changes to
existing handlers, but new command types and registrations still require
updates to the system.

**Solution/Discussion:**
These entities are totally disconnected. For example,
Power Manager and Storage Manager have entirely different purpose. We
don’t want sender to be coupled with the receiver. The sender can just
dispatch the message/command to the pipeline and forget. The object that is
connected to the pipeline will either process or delegate the command to the
next object. In order to synthesis this kind of behavior, we need to implement
'Chain of Responsibility' principle.

A ‘Chain of Responsibility’ principle implements a singly linked list. Here, all the objects are connected with each other. A message/command is dispatched to
the head node of the singly linked list. If the head node cannot handle the
command/message, then it will delegate to its next object . This way, the
message/command is delegated from one node to another unless the
message can be handled by the appropriate object.

**Design of Chain of Responsibility Principle.**

<img src="/assets/img/COR_UML.png" alt="COR_UML">

__Chain of Responsibility__

**How to implement the behavioural pattern to realise ‘Chain of
Responsibility’ design pattern here?**

1. XMPP command Enums – All the commands that can be supported by the
STB system. We can always extend it.

2. XMPP Stanza – This is the base class – head node for the chain of
responsibility principle i.e. singly linked list. A command/message will always be dispatched first to this head node of the pipeline. If the message cannot be handled, then it will call it’s next object to handle it. This way, the message will be delegated to next object unless the message can be handled. This class should have a routine/method to build the singly linked list i.e next pointer.
A client will dispatch the XMPP commands to this class object only. Also, it will
register itself with this class. Internally, during registration, it will append the new object into its singly linked list. Also, this class will have a
virtual method to handle the message. This class will just delegate the message to its next object .

3. XMPP – pipeline objects – These can be extended easily. For the given
problem, the XMPP pipeline objects are – codeDownProcessor,
hddDiagnosticsProcessor, and rebootStbProcessor. Each of these objects
will implement the virtual method to handle the message. If any of the object
cannot handle the message, then it will call the head node/super class/base
class to delegate the message to its next object.

4. client – The client will create all the pipeline objects and the base object i.e. XMPP Stanza. All the pipeline objects will be registered with the head node i.e. XMPP Stanza. As discussed earlier, during registration, the head node/base
class will append the pipeline object to its singly linked list.

Here is the code for each class.

  * XMPP command Enums

 {% highlight cpp %}

  #ifndef XMPPCOMMANDS_H
  #define XMPPCOMMANDS_H
  enum xmppCommands
  {
    codeDownloadProcess,
    hddDiagnosticsProcess,
    rebootStbProcess,
    MAX_COMMAND
  };
// XMPPCOMMANDS_H
  #endif

{% endhighlight %}

  * XMPP Stanza – Head node/ Super Class/ Base class

  {% highlight cpp %}

  #ifndef XMPPSTANZA_H
  #define XMPPSTANZA_H
  #include "XmppCommands.h"
  #include <QDebug>
  class XmppStanza
  {
    private:
      XmppStanza * m_pnext;
    public:
      XmppStanza()
      {
        m_pnext = NULL;
      }
      /** build a singly linked list ** /
      void addNextStanzaProcessor(XmppStanza * next)
      {
        if( m_pnext)
        {
          m_pnext->addNextStanzaProcessor(next);
        }
        else
        {
          m_pnext = next;
        }
      }

      virtual void processStanza(xmppCommands commands)
      {
        if( m_pnext )
        {   
          m_pnext->processStanza(commands);
        }
      }
      virtual ~XmppStanza()
      {
        qDebug()<<"Destructor of Xmpp Stanza is invoked";
      }
};
  #endif // XMPPSTANZA_H

{% endhighlight %}


  * Pipeline Object – codeDownProcessor.

{% highlight cpp %}

#ifndef CODEDOWNLOADPROCESSOR_H
#define CODEDOWNLOADPROCESSOR_H
#include "XmppCommands.h"
#include "XmppStanza.h"
#include <QDebug>
class codeDownloadProcessor : public XmppStanza
{
  private:
  public:
      codeDownloadProcessor()
      {
        qDebug()<<"codeDownloadProcessor constructor inovked";
      }
      ~codeDownloadProcessor()
      {
        qDebug()<<"codeDownloadProcessor destructor inovked";
      }
      virtual void processStanza(xmppCommands commands)
      {
        if( commands == codeDownloadProcess)
        {
          qDebug()<<"Downloading the Image!!!";
        }
        else
        {
          /** delegate the command ** /
          qDebug()<<"codeDownloadProcessor delegating";
          XmppStanza::processStanza(commands);
        }
      }
};
#endif // CODEDOWNLOADPROCESSOR_H

{% endhighlight %}


  * Pipeline Object – hddDiagnosticsProcessor.

{% highlight cpp %}

#ifndef HDDDIAGNOSTICSPROCESS_H
#define HDDDIAGNOSTICSPROCESS_H
#include "XmppCommands.h"
#include "XmppStanza.h"
#include <QDebug>
class hddDiagnosticsProcessor : public XmppStanza
{
  private:
  public:
    hddDiagnosticsProcessor()
    {
      qDebug()<<"hddDiagnosticsProcessor constructor inovked";
    }
    ~hddDiagnosticsProcessor()
    {
      qDebug()<<"hddDiagnosticsProcessor destructor inovked";
    }
    virtual void processStanza(xmppCommands commands)
    {
      if( commands == hddDiagnosticsProcess)
      {
        qDebug()<<"Getting the Health of HDD!!!";
      }
      else
      {
        /** delegate the command ** /
        qDebug()<<"hddDiagnosticsProcessor delegating";
        XmppStanza::processStanza(commands);  
      }
    }
};
#endif // HDDDIAGNOSTICSPROCESS_H

{% endhighlight %}


  * Pipeline Object – rebootStbProcessor.

{% highlight cpp %}

#ifndef REBOOTSTBPROCESSOR_H
#define REBOOTSTBPROCESSOR_H
#include "XmppCommands.h"
#include "XmppStanza.h"
#include <QDebug>
class rebootStbProcessor : public XmppStanza
{
  private:
  public:
    rebootStbProcessor()
    {
      qDebug()<<"rebootStbProcessor constructor inovked";
    }
    ~rebootStbProcessor()
    {
      qDebug()<<"rebootStbProcessor destructor inovked";
    }
    virtual void processStanza(xmppCommands commands)
    {
      if( commands == rebootStbProcess)
      {
        qDebug()<<"Rebooting the STB!!!";
      }
      else
      {
        /** delegate the command ** /
        qDebug()<<"rebootStbProcessor delegating";
        XmppStanza::processStanza(commands);
      }
    }
};
#endif // REBOOTSTBPROCESSOR_H

{% endhighlight %}


  * Client

{% highlight cpp %}

#include <QtCore/QCoreApplication>
#include "XmppCommands.h"
#include "XmppStanza.h"
#include "codeDownloadProcessor.h"
#include "hddDiagnosticsProcessor.h"
#include "rebootStbProcessor.h"
int main(int argc, char * argv[])
{
  QCoreApplication a(argc, argv);
  XmppStanza xmppCmds;
  codeDownloadProcessor xmppSoftwareUpgrade;
  hddDiagnosticsProcessor xmppHddHealth;
  rebootStbProcessor xmppRebootStb;
  xmppCmds.addNextStanzaProcessor(&xmppSoftwareUpgrade);
  xmppCmds.addNextStanzaProcessor(&xmppHddHealth);
  xmppCmds.addNextStanzaProcessor(&xmppRebootStb);
  xmppCmds.processStanza(rebootStbProcess);
  xmppCmds.processStanza(codeDownloadProcess);
  xmppCmds.processStanza(hddDiagnosticsProcess);
  xmppCmds.processStanza(MAX_COMMAND);
  return a.exec();
}

{% endhighlight %}

Here is the output.

<img src="/assets/img/COR_Output.png" alt="COR_Output">

The example shows the basic delegation idea. A production dispatcher should also define how an unhandled command is reported, who owns each handler, and how handler lifetimes relate to the chain.

This brings an end to the topic of the Chain of Responsibility pattern.
Here is the entire code that can be downloaded.

[Source_code_COR_Pattern](https://drive.google.com/open?id=19BCediyhqoeB7vQWyJZnhWbGlwrgZyj-)
