---
layout: post
title: "JavaScript Functions, Closures, and Error Handling"
description: "Explore try/catch/finally, closures, IIFEs, and function properties in JavaScript."
date:   2021-04-08 14:13:31 +1300
categories: JavaScript
---

This article introduces JavaScript exceptions, closures, immediately invoked function
expressions (IIFEs), and selected function properties.

## try, catch and finally
Use `try`/`catch` for operations that can throw exceptions, and handle only errors the
application can respond to meaningfully. For example, `JSON.parse()` can throw on invalid
input, while `parseInt()` generally returns `NaN`. A `finally` block is useful for cleanup
and runs before normal completion unless execution is forcibly terminated.

{% highlight javascript %}

  try{
    test(); //throws an error.
  }
  catch(e) {
    console.log('SJ - catch block ' + e.toString()); // "SJ  - catch block ReferenceError: test is not defined"
  }

  finally{
   console.log('Finally block executed'); //Finally block executed
  }

{% endhighlight %}

This second example completes without entering `catch`, then runs `finally`.

{% highlight javascript %}

 try{
    console.log('Hello world');
  }
  catch(e) {
    console.log('SJ - catch block ' + e.toString()); //
  }

  finally{
   console.log('Finally block executed');
  }

{% endhighlight %}

Here is the output.

{% highlight text %}

"Hello world"
"Finally block executed"

{% endhighlight %}

## Closures
A closure is a function together with access to the lexical environment in which it was
created. Closures can retain values for later callbacks:

{% highlight javascript %}

function generator(input) {
   var number = input;
   return function() {
     return number*2;
   };
}

var calc = generator(900); // returns a function
var anotherCalc = generator(1000); //returns a function
console.log(calc()); //1800
console.log(anotherCalc()); //2000

{% endhighlight %}

## Immediately invoked function expressions
An IIFE is a function expression invoked immediately. Its local variables do not become
global bindings.

{% highlight javascript %}

 (function calc() {
  var number = 10;
  console.log(number); //10
})();

{% endhighlight %}

## Why IIFEs are important
An IIFE can create a local scope and avoid introducing bindings into the global scope.
It does not isolate side effects performed through objects passed into it.

## Passing value to the IIFEs
You can pass the parameters to the IFFEs also. Here is an example.

{% highlight javascript %}

 (function calc(input) {
  var number = input;
  console.log(number); //10
})(100);

{% endhighlight %}

## Usage of passing parameters to IIFEs
Here is an example that illustrates the usage of passing parameters to the IIFEs.
For example, you have a global obj. Now, you want to add the property value to the global obj. You can do this using IIFEs.

{% highlight javascript %}

var obj = {}; //declare and define an object
console.log(obj); //[object Object] { ... }

 (function calc(input) {
   input.name = 'Shreyas'
})(obj);

console.log('After IIFE is executed'); //"After IIFE is executed"
console.log(obj); // [object Object] { name: "Shreyas" }

{% endhighlight %}

## Built in methods and properties of functions
## arguments
In a regular function, `arguments` is an array-like object containing the arguments
passed to the call. It is not an array; rest parameters are generally preferred in new
code.

{% highlight javascript %}

  function message(msg) {
    console.log(msg); //Hi
    console.log(arguments); //[object Arguments] { 0: "Hi", 1: 10}
    console.log(arguments[0]); //Hi
    console.log(arguments[1]); //10
    console.log(arguments[2]); //undefined
    console.log(arguments.length); //2
  }
  message('Hi', 10);

{% endhighlight %}

## name of the function
The `name` property gives a function's name. The `length` property counts formal
parameters before the first one with a default value; it is not necessarily the number
of arguments required at runtime.

{% highlight javascript %}

  function message(msg) {
    console.log(msg); //Hi
  }

  var xFunc = message;
  console.log(xFunc.name); //"message"
  console.log(xFunc.length); //1

{% endhighlight %}

This brings an end to this topic.

References -

https://stackoverflow.com/questions/15455009/javascript-call-apply-vs-bind#:~:text=Call%20invokes%20the%20function%20and,and%20any%20number%20of%20arguments.

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind

https://jsbin.com/vomadedive/edit?html,js,console,output
