---
layout: post
title:  "Calling JavaScript from C++ with Qt WebKit"
date:   2015-04-12 14:13:31 +1300
categories: cpp
description: Two historical Qt WebKit techniques for calling JavaScript from C++, with lifecycle and loading considerations.
---
This article discusses on how to call a JavaScript function from C++ using
Qt Framework. This framework uses Qt-Webkit. Currently, there are two ways
to achieve this.

1. **Install Signals and Slots for the Javscript function.**
2. **Using the in-built API – evaluate JavaScript**
Note: The Javascript evaluation by the C++ class will be understood once the
web-page is loaded. Thus, we should add the JavaScript to the window
object, once the web-page is loaded. This can be done by installing the slot
for the signal – javaScript WindowObject Cleared.

Here are the details for each mechanism.

1. Install signal and slots for the JavaScript function.
a) Add Java script window object to the javaScript WindowObject Cleared slot.
b) Declare a signal in the class.
c) Emit the signal
d) In the Javascript, connect the signal to the Javascript function slot.
Here is the syntax to connect.


{% highlight text %}

<Javascript_window_object>.<signal_name>.connect(<Javascript function name>)

{% endhighlight %}

Note, you can do a callback to the Javascript only once the webpage is
loaded. This can be done by connecting to the slot emitted by the signal
loadFinished() in the C++ applicat ion.
Let ’s see t he real example now.

Here is the simple form - HTML/JavaScript

{% highlight text %}

<html>
<head>
<script>
function alert_click()
{
  alert("you clicked");
}
function JavaScript_function()
{
  alert("Hello");
}
myoperations.alert_script_signal.connect(JavaScript_function);
</script>
</head>
<body>
<form name="myform">
<input type="button" value="Hit me" onclick="alert_click()">
</form>
</body>
</html>

{% endhighlight %}

Here is the C++,Qt Code.

{% highlight text %}

#include <QtGui/QApplication>
#include <QApplication>
#include <QDebug>
#include <QWebFrame>
#include <QWebPage>
#include <QWebView>
class MyJavaScriptOperations: public QObject
{
  Q_OBJECT
  public:
        QWebView * view;
        MyJavaScriptOperations();
  signals:
        void alert_script_signal();
        public slots:
        void JS_ADDED();
        void loadFinished(bool);
};

void MyJavaScriptOperations::JS_ADDED()
{
  qDebug()<<__PRETTY_FUNCTION__;
  view->page()->mainFrame()->addToJavaScriptWindowObject("myoperations", this);
}

void MyJavaScriptOperations::loadFinished(bool oper)
{
  qDebug()<<__PRETTY_FUNCTION__<< oper;
  emit alert_script_signal();
}

MyJavaScriptOperations::MyJavaScriptOperations()
{
  qDebug()<<__PRETTY_FUNCTION__;
  view = new QWebView();
  view->resize(400, 500);
  connect(view->page()->mainFrame(), SIGNAL(javaScriptWindowObjectCleared()), this, SLOT(JS_ADDED()));
  connect(view, SIGNAL(loadFinished(bool)), this, SLOT(loadFinished(bool)));
  view->load(QUrl("./index.html"));
  view->show();
}

int main(int argc, char * argv[])
{
  QApplication a(argc, argv);
  MyJavaScriptOperations * jvs = new MyJavaScriptOperations;
  return a.exec();
}
#include "main.moc"

{% endhighlight %}

2. Using the in-built API – evaluateJavaScript

Here, the C++ class should know the Java Function to call. However, this is not
required in the signal/slot mechanism, which was described earlier. Please see
the steps here.
a) Add Java script window object to the javaScript WindowObject Cleared slot .
b) Invoke t he API from page->mainframe-
evaluate JavaScript (“JavaScript_function()”)
c) In the Javascript , declare the
Javascript windowobject.method_name(“Javascript function name that will be
invoked from this method”);
Here is the sample code.

Form code - HTML/Javascript

{% highlight text %}

<html>
<head>
<script>
function alert_click()
{
  alert("you clicked");
}
function JavaScript_function()
{
  alert("Hello");
}
myoperations.firecb(JavaScript_function);
</script>
</head>
<body>
<form name="myform">
<input type="button" value="Hit me" onclick="alert_click()">
</form>
</body>
</html>

{% endhighlight %}

Here is the QT- main.cpp file .

{% highlight text %}

#include <QtGui/QApplication>
#include <QApplication>
#include <QDebug>
#include <QWebFrame>
#include <QWebPage>
#include <QWebView>
class MyJavaScriptOperations : public QObject {
Q_OBJECT
public:
  QWebView * view;
  MyJavaScriptOperations();
  void firecb();
signals:
  void alert_script_signal();
public slots:
  void JS_ADDED();
  void loadFinished(bool);
};
void MyJavaScriptOperations::JS_ADDED()
{
  qDebug()<<__PRETTY_FUNCTION__;
  view->page()->mainFrame()->addToJavaScriptWindowObject("myoperations", this);
}
void MyJavaScriptOperations::loadFinished(bool oper)
{
  qDebug()<<__PRETTY_FUNCTION__<< oper;
  firecb();
}

void MyJavaScriptOperations::firecb()
{
  qDebug()<<__PRETTY_FUNCTION__;
  view->page()->mainFrame()->evaluateJavaScript("JavaScript_function()");
}

MyJavaScriptOperations::MyJavaScriptOperations()
{
  qDebug()<<__PRETTY_FUNCTION__;
  view = new QWebView();
  view->resize(400, 500);
  connect(view->page()->mainFrame(), SIGNAL(javaScriptWindowObjectCleared()), this, SLOT(JS_ADDED()));
  connect(view, SIGNAL(loadFinished(bool)), this, SLOT(loadFinished(bool)));
  view->load(QUrl("./index.html"));
  view->show();
}
int main(int argc, char * argv[])
{
  QApplication a(argc, argv);
  MyJavaScriptOperations * jvs = new MyJavaScriptOperations;
  return a.exec();
}
#include "main.moc"

{% endhighlight %}

Here is the link to download the source code –

* [Source_code_QtWebkit](https://drive.google.com/file/d/1bgwRpgysvooT-rlrKXWYgot-xf8vOHp3/view?usp=sharing)
