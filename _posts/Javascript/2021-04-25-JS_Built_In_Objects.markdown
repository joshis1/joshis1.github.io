---
layout: post
title: "JavaScript Built-in Objects and APIs"
description: "Examples using JavaScript timers, strings, Math, Date, and regular expressions."
date:   2021-04-25 14:13:31 +1300
categories: JavaScript
---

This article introduces JavaScript timers and selected built-in APIs for numbers, strings,
dates, and regular expressions.

## setTimeout
`setTimeout()` schedules a function to run after a delay in milliseconds. The delay is a
minimum wait, not an exact execution time.

{% highlight javascript %}

setTimeout(function(){
  console.log('Hello');
}, 2000); //after 2 seconds, we see Hello

{% endhighlight %}

## setInterval
Just like a timer, this will keep executing the given function at the interval specified in this method. Here is an example. In the example below, we will see ping every half a second.

{% highlight javascript %}

 setInterval(function() {
    console.log('ping');
 }, 500);

{% endhighlight %}

## Stopping the timer
`setInterval()` schedules repeated calls until it is cancelled. Actual timing can vary,
so this example prints approximately four messages before cancellation.

{% highlight javascript %}

 var interval = setInterval(function() {
    console.log('Ping');
 }, 500);

 setTimeout(function(){
   clearInterval(interval);
 }, 2000);

{% endhighlight %}

## Transforming format and Values
There are certain in built methods that are very much important in order to transform the format from string to a number.

{% highlight javascript %}

var a = '5';
console.log(a); // "5"
console.log(parseInt(a)); //5

var a = 'test';
console.log(parseInt(a)); // NaN

var a = 'FB123';
console.log(parseInt(a)); //NaN
console.log(parseInt(a, 16)); // 1028387

var a = 10;
console.log(a.toString()); // '10'

var a = 10.3;
console.log(a.toFixed()); // "10" (toFixed returns a string)

console.log(a.toFixed(2)); //10.30

{% endhighlight %}

## String methods
Strings are immutable, but they support indexed access and methods that return new
strings or other values.

{% highlight javascript %}
  var string = 'Any text';
  console.log(string);

  console.log(string.length); //8
  console.log(string[2]); //'y'

  console.log(string.charAt(2)); //'y'

  var newString  = string.concat(' add new string');

  console.log(newString); //"Any text add new string"

  var uppString = string.toUpperCase();
  console.log(uppString); //"ANY TEXT"

  var lowString = string.toLowerCase();
  console.log(lowString); //"any text"

  var splitString = string.split(' ');
  console.log(splitString); //["Any", "text"]
  console.log(splitString[0]); //"Any"
  console.log(splitString[1]); //"text"

  var userString = ' Any text ';
  console.log(userString); //" Any text "
  // all the heading and trailing white spaces will be removed when used trim
  console.log(userString.trim()); //"Any text"

  console.log(string); //"Any text"

{% endhighlight %}

## Math Objects
Math object provides a lot of built in methods and properties. Here is a list of such properties and methods.

{% highlight javascript %}

  var pi = Math.PI;
  console.log(pi); //3.141592653589793

  var e = Math.E;
  console.log(e); //2.718281828459045

  var a = -3;
  console.log(Math.abs(a)); //3

  var a = 1.27;
  console.log(Math.round(a)); //1

  console.log(Math.ceil(a)); //2
  console.log(Math.floor(a)); //1

  var a = 2;
  console.log(Math.exp(a)); //7.38905609893065 nothing but e^2

  var e = Math.E;
  console.log(Math.log(e)); //1

  console.log(Math.max(1, 100, 1000)); //1000

  console.log(Math.min(1,100,1000)); // 1
  console.log(Math.random()); //any floating poing with 0.00x
  var rand = Math.random() * 100;
  console.log(rand); // some floating point
  var rand1 = Math.floor(rand);
  console.log(rand1); // Integer from 0 through 99.
  // Add 1 to get an integer from 1 through 100.
  console.log(rand1 + 1);

{% endhighlight %}

## Date Object
The `Date` object represents a point in time. Numeric date components use the local
timezone and a zero-based month index. Prefer the standard ISO date-time format when
parsing strings; other formats may be implementation-dependent.

{% highlight javascript %}

  var today = new Date();
  console.log(today); //gets an object
  console.log(today.toString()); //"Mon Apr 26 2021 08:25:13 GMT+1000 (Australian Eastern Standard Time)"

  // Numeric months start at 0: 0 is January and 3 is April.
  var today = new Date(2021, 03, 30);
  console.log(today.toString()); // Local time; the displayed timezone depends on the system.

 var today = new Date('2021-05-01T00:00:00Z');
 console.log(today.toISOString()); // "2021-05-01T00:00:00.000Z"

 // Date.parse returns milliseconds since the Unix epoch for a valid date string.
 console.log(Date.parse('2021-05-01T00:00:00Z'));

var today = new Date();
console.log(today.getDate()); //26

// the weekday in js starts from Sunday i.e. 0
// today is Monday therefore 1.
console.log(today.getDay()); //1

{% endhighlight %}

## Regular expression
A regular expression pattern is expressed in javascript using / /. Just like string is expressed in ' ', a regular expression pattern is expressed as / /. The regular expression is nothing but an object. You can use exec() method of a regular expression object in order to do pattern matching on a string. Otherwise, you can use match() method of a string to do pattern matching. Here is an example.

{% highlight javascript %}

var s = 'abc';
var patt = /ab/;
var s1 = 'test';

console.log(patt.exec(s)); //["ab"]
console.log(s1.match(patt)); //null

var s1 = 'joo';
var patt1 = /[j-mz]oo/;
console.log(patt1.exec(s1)); // ["joo"]

var s2 = 'loo';
var patt1 = /[j-mz]oo/;
console.log(s2.match(patt1)); //["loo"]

var s2 = 'noo';
var patt1 = /[j-mz]oo/;
console.log(s2.match(patt1)); //null

console.log(patt1); //[object RegExp] { ... }

console.log(patt1.toString()); //"/[j-mz]oo/"

{% endhighlight %}

You can also use test() method of regEx object to get the result true or false based on whether the match was found or not. Here is an example.

{% highlight javascript %}

var s2 = 'noo';
var patt1 = /[j-mz]oo/;
console.log(patt1.test(s2)); //false

var s2 = 'joo';
var patt1 = /[j-mz]oo/;
console.log(patt1.test(s2)); //true

{% endhighlight %}

Regular expressions can help match text, but validation should be designed carefully for
the expected input and security requirements.

This brings an end to the built in object topic in javascript.

References -

https://stackoverflow.com/questions/15455009/javascript-call-apply-vs-bind#:~:text=Call%20invokes%20the%20function%20and,and%20any%20number%20of%20arguments.

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind

https://jsbin.com/vomadedive/edit?html,js,console,output

https://javascript.info/settimeout-setinterval

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
