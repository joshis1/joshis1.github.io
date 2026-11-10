---
layout: post
title: "JavaScript Values, References, and Scope"
description: "An introduction to primitive values, object references, mutability, and JavaScript variable scope."
date:   2021-03-24 14:13:31 +1300
categories: JavaScript
---

When you assign a primitive value, the variable receives that value. JavaScript
primitives include strings, numbers, booleans, `null`, `undefined`, symbols, and bigints.

{% highlight javascript %}

  var aNumber = 5;
  console.log(aNumber); //5

  var anotherNumber = aNumber;
  console.log(anotherNumber); // 5

  aNumber = 12;
  console.log(aNumber); //12
  console.log(anotherNumber); //5

{% endhighlight %}

## Objects and references
Arrays and other objects are accessed through references. Assigning an object to another
variable copies the reference, so both variables can observe mutations to the same object.
This is a useful mental model, but JavaScript does not expose raw pointers or memory
addresses.

{% highlight javascript %}

  var array = [1,2,3];
  console.log(typeof array); //object
  var anotherArray = array;
  console.log(array); // [1,2,3]
  console.log(anotherArray); // [1,2,3]
  array.push(4);
  console.log(array); // [1,2,3,4]
  console.log(anotherArray); // [1,2,3,4]

{% endhighlight %}

## Mutability
Objects can be mutated; primitive values such as strings and numbers cannot. A `var` or
`let` binding can be reassigned to a different value. Reassigning an array does not
mutate the original array or change other references to it.

{% highlight javascript %}

 var array = [1,2,3];
 var anotherArray = array;

 array = ['a', 'b']; // now array points to a different piece of memory.

 console.log(array); // ['a', 'b']
 console.log(anotherArray); // [1,2,3] this still points to the old piece of memory i.e. [1,2,3]

{% endhighlight %}

## Immutable primitive values
String methods return new strings rather than changing the original string.

{% highlight javascript %}

 str = "ABC";
 str.toLowerCase();
 str_lower = str.toLowerCase(); // a new string is returned instead of changing it.
 console.log(str); // "ABC"
 console.log(str_lower); // "abc"

{% endhighlight %}

Javascript doesn't allow to change the value of a string. Here you can see that you need to assign the value to another string to see the LowerCase results.
Another example is slicing of the string. It is clear enough that string is immutable.

{% highlight javascript %}

var str = 'string';
var newstr = str.slice(1,3); // 1 and 3 index number are not included
console.log(str); // "string"
console.log(newstr); // "tr"

{% endhighlight %}

## Scope
JavaScript has several scope rules. `var` is function-scoped (or global-scoped outside a
function), while `let` and `const` are block-scoped. Prefer `const` by default and use
`let` when reassignment is needed; avoid undeclared assignments.

At the top level of a classic browser script, a `var` declaration becomes a property of
the global object. This does not apply in the same way to modules or other runtimes.

{% highlight javascript %}

var test = 'Global Scope';  // it's global
console.log(test); // Global Scope

function localScope() {
  var test = 'Local Scope'; // local variable because it is inside a function
  console.log(test); // Local Scope
}

localScope();
console.log(test); // Global Scope

{% endhighlight %}

This example updates a declared global binding. If a name is completely undeclared,
assignment can create a global only in a non-strict classic script; strict mode and
JavaScript modules throw a `ReferenceError`. Declare variables explicitly instead.

{% highlight javascript %}

var test = 'Global Scope';  // it's global
console.log(test); // Global Scope

function localScope() {
  test = 'Still Global Scope'; // since no var it is accessing global variable test
  console.log(test); // Still Global Scope
}

localScope();
console.log(test); //Still Global Scope
{% endhighlight %}

## `var` and block scope
`var` declarations are not block-scoped. This example shows how a declaration inside an
`if` block still refers to the same function-scoped binding:

{% highlight javascript %}

function myFunction() {
 console.log(i); // undefined
 var i = 0;
 console.log(i); // 0

 if(true) {
    var i = 5; // Reassigns the function-scoped i.
    console.log(i); // 5
 }

 console.log(i); // 5 since i is not block scoped but local scoped.

}

myFunction(); //call that function

{% endhighlight %}

`var` declarations are hoisted within their function, but their assignments remain at
the original location. Prefer `let` or `const` for block-scoped bindings.

{% highlight javascript %}

  var notNull = 1; // global
  function test() {
    if(!notNull) {
     console.log("Local value before initialization:", notNull); // undefined
     for (var notNull = 10; notNull <= 0; notNull++) {
       // The loop body does not run.
     }
     console.log("After the loop:", notNull); // 10

    }
    console.log(notNull); // 10  because it is inside the function test and therefore local variable.
  }

  test();

{% endhighlight %}

Avoid the next pattern: without a declaration, the assignment can affect a global in a
non-strict classic script, and throws in strict mode or a module.

{% highlight javascript %}

 var notNull = 1; // global
  function test() {
    if (!notNull) { // This is false because the global notNull is 1.
     console.log("Null-ish so far", notNull);
     for (notNull = 10; notNull <= 0; notNull++) {
       // This assignment is not declared.
     }
     console.log("Not it is not null", notNull); // 1 -- since it is a global variable.

    }
    console.log(notNull); // 1
  }

  test();

{% endhighlight %}

For new code, use `const` or `let` and avoid relying on `var` hoisting or implicit globals.

References -

http://www.vishalchovatiya.com/mastering-c-books-courses-tools-tutorials-blogs-communities/
