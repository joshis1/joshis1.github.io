---
layout: post
title: "JavaScript Conditionals and Comparison with C/C++"
description: "Explore JavaScript objects, functions, strict mode, truthiness, and conditional statements alongside C/C++ examples."
date:   2021-03-10 14:13:31 +1300
categories: JavaScript
---

This article introduces JavaScript objects, functions, strict mode, truthiness, and
conditional statements, with comparisons to C and C++.

## object
{% highlight javascript %}

var myobj = {
  //fields and methods
  //fields are properties
  // methods are functions
  name: 'Max'
};

console.log(myobj);

[object Object] {
  name: "Max"
}

console.log(myobj.name);

// "Max"

console.log(typeof myobj); // "object"

{% endhighlight %}

In C++, we need to declare a class first and then we instantiate it to create an object.

{% highlight cpp %}
#include <iostream>

class objTest
{
 public:
  std::string name;
};

int main()
{
  objTest myobj;
  myobj.name = "Max";
  std::cout<<"myobj.name "<<myobj.name<<std::endl;
  return 0;
}
{% endhighlight %}

## Using strict mode in Javascript
JavaScript has automatic semicolon insertion, but it does not make every line break a
statement boundary. Use a consistent semicolon style and avoid relying on ambiguous line
breaks. Strict mode does not require semicolons or `var`; it catches certain unsafe
behaviors, including assigning to an undeclared variable.

{% highlight javascript %}
"use strict";
let count = 0;
count += 1;
{% endhighlight %}

## Other tricks allowed by Javascript
JavaScript variables are dynamically typed: a binding can refer to values of different
types. Prefer clear, stable types in application code because changing types can make
programs harder to understand.

{% highlight javascript %}
  var var1 = 5;
  console.log(typeof var1); //number

  var1 = '10';
  console.log(typeof var1); // string

{% endhighlight %}

It is not a good practice to change the type of a variable since it makes debugging very difficult.


## Hoisting in Javascript
Hoisting describes how declarations are processed before code runs. It does not mean that
using a variable before its declaration is safe; `var`, `let`, and `const` have different
initialization and scope rules.

{% highlight javascript %}

   "use strict";
   x = 'hello'; // ReferenceError: x has not been declared.

{% endhighlight %}

Declare a variable before using it. A `var` declaration is hoisted within its function
or script, but its assignment remains at the original location. An undeclared assignment
throws in strict mode; in a non-strict classic script it can create or modify a global.

## functions in javascript
In javascript, you can create functions using keyword function. In C++, you don't have to write the keyword function.

{% highlight javascript %}

function calc() {
 console.log('Inside calc()');
}

calc(); // caller

{% endhighlight %}

In C++, you don't say function but simply the function has a signature.

{% highlight cpp %}

 void calc() {
   std::cout<<"Inside calc()"<<std::endl;
 }

 calc();

{% endhighlight %}

function is a type in javascript. Here is the code that will show that there is a type called function.

{% highlight javascript %}

var calc = function() {
  console.log('calc');
};

console.log(typeof calc); //"function"

var anotherFunc = calc;

anotherFunc(); // calc

{% endhighlight %}

## functions with parameters
{% highlight javascript %}

 function calc(number1, number2) {
   return number1 + number2;
 }

 var returned = calc();
 console.log(returned); //NaN

 var returned = calc(10,8);
 console.log(returned); // 18

 var returned = calc(10,8,10); // the extra parameter will be ignored

 console.log(returned); //18

 var calculator = calc;
 console.log(calculator(15,2)); //17

{% endhighlight %}

You can see that basic functions in javascript are more or less like C only. It is just that function is a type in javascript whereas in C there is no such keyword function. We just need signature in C or C++. In Javascript, we need function keyword.

## Control Structures
Conditional statements choose which code to execute. JavaScript uses `else if` (not
`elseif`) and also supports the conditional, or ternary, operator.

{% highlight javascript %}

var condition = true;
var anotherCondition = true;

 if(condition) {
   console.log('Executed');
 }
 else if(anotherCondition)
 {
    console.log('another condition executed');
 }
 else {
   console.log('nothing executed');
 }

{% endhighlight %}

Output is

{% highlight text %}

"Executed"

{% endhighlight %}

Now, let's see the same thing in C.

{% highlight cpp %}

#include <stdio.h>
#include <stdbool.h>

int main()
{
        bool condition = true;
        bool anotherCondition = true;

        if(condition) {
                printf("Executed");
        }
        else if(anotherCondition)
        {
                printf("another condition executed");
        }
        else {
                printf("nothing executed");
        }
        return 0;
}

{% endhighlight %}

The output is same -

{% highlight text %}

"Executed"

{% endhighlight %}

In JavaScript conditionals, values are converted to booleans. `0`, `-0`, `NaN`, the
empty string, `null`, `undefined`, and `false` are falsy; other values are truthy. C
conditions use scalar values and have different type rules.

{% highlight javascript %}

var condition = 234;
if(condition) {
console.log('Executed non-zero condition');
}
condition = 0;
if(condition) {
console.log('You wont see me');
}
condition = -1;
if(condition) {
console.log('Non-Zero is true condition');
}
{% endhighlight %}

Here is the output

{% highlight text %}

"Executed non-zero condition"
"Non-Zero is true condition"

{% endhighlight %}

Let's do the same thing in C and see how it behaves. You will notice that the behaviour is same. Here is the code.

{% highlight cpp %}

#include <stdio.h>

int main()
{
    int condition = 234;
    if(condition)
      {
        printf("Executed non-zero condition \r\n");
      }
    condition = 0;
    if(condition)
      {
        printf("You wont see me \r\n");
      }
    condition = -1;
    if(condition)
      {
        printf("Non-Zero is true condition \r\n");
      }
    return 0;
}

{% endhighlight %}


Here is the output

{% highlight bash %}

 ./test_cond1.out
Executed non-zero condition
Non-Zero is true condition

{% endhighlight %}

Please note that non-zero is treated as true only in conditional statement. It doesn't mean boolean true is a non-zero value. In fact, in javascript and C language true is nothing but 1 and false is nothing but 0 if we look from value perspective. But, also note that they are two different data types. The following code will explain it. Here is the javascript check.

{% highlight javascript %}
console.log(1 == true); // true
console.log(1 === true);  // false since they are different data types.
console.log(0 == false);  // true
console.log(0 === false); //false since they are different data types.

{% endhighlight %}

This holds true even in C language. Let's check that out.

{% highlight cpp %}

#include <stdio.h>
#include <stdbool.h>

int main()
{
  printf("Check 1 == true is %d \r\n", (1 == true));
  printf("Check 0 == false is %d \r\n", (0 == false));
  printf("Check if non-zero is true or not %d \r\n", (34 == true));
  printf("Check if any negative number is false or not %d \r\n", (-10 == false));
  //printf( 0 == false);

  return 0;
}

{% endhighlight %}

Here is the output.

{% highlight bash %}
./test_true_false.out
Check 1 == true is 1
Check 0 == false is 1
Check if non-zero is true or not 0
Check if any negative number is false or not 0

{% endhighlight %}

For example, a non-empty string is truthy, while `null` is falsy.

This brings end to the conditional structs of javascript.

References -

Practice javascript using -

https://jsbin.com/
