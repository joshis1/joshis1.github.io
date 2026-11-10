---
layout: post
title: "JavaScript Fundamentals Compared with C++"
description: "Compare JavaScript and C++ values, types, arrays, null, undefined, and common operators."
date:   2021-03-12 14:13:31 +1300
categories: JavaScript
---

This article compares selected JavaScript and C++ fundamentals. The languages share some
syntax, but differ in their type systems, runtime behavior, and memory models.

## Variables and boolean values
`var`, `let`, and `const` declare JavaScript bindings; `true` and `false` are boolean
literals. JavaScript has a `number` type for integer-like and floating-point values.
C++ instead has distinct numeric types and declarations such as `int`, `float`, and
`bool`.

{% highlight javascript %}
var variable = 5; // A JavaScript number.
console.log(variable);
variable = true; // A boolean value.
console.log(variable);
{% endhighlight %}

The next example is also JavaScript:

{% highlight javascript %}
var variable = 'text';
console.log(variable);
{% endhighlight %}

## `typeof`
JavaScript reports both integer-like and floating-point numeric values as `"number"`.

{% highlight javascript %}
var var1 = 6.5;
console.log(typeof var1); // number

var var2 = 'text';
console.log(typeof var2); // string

var var3 = true;
console.log(typeof var3); // boolean

{% endhighlight %}

## C++ `typeid`
In C++, `typeid` is part of run-time type information (RTTI). This example uses
`std::string`, so it includes the string header explicitly.

{% highlight cpp %}

#include <typeinfo>
#include <iostream>
#include <string>


class myclass
{
  int mynumber;
  float myfloat;
};

int main()
{
  int myint = 10;
  float myfloat = 1.2;
  char mychar = 'a';
  std::string mystring = "My String";
  int arr[3] = {1,2,3};
  myclass myclass_instance;
  std::cout<<"Type of myint is "<<typeid(myint).name()<<std::endl;
  std::cout<<"Type of myfloat is "<<typeid(myfloat).name()<<std::endl;
  std::cout<<"Type of mychar is "<<typeid(mychar).name()<<std::endl;
  std::cout<<"Type of mystring is "<<typeid(mystring).name()<<std::endl;
  std::cout<<"Type of arr is "<<typeid(arr).name()<<std::endl;
  std::cout<<"Type of myclass_instance is "<<typeid(myclass_instance).name()<<std::endl;
  return 0;
}

{% endhighlight %}

Here are the results.

{% highlight bash %}

 ./test1.out
Type of myint is i
Type of myfloat is f
Type of mychar is c
Type of mystring is NSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
Type of arr is A3_i
Type of myclass_instance is 7myclass

{% endhighlight %}

## Arrays
Array is a collection of values. It can be a collection of the same types or mixed types in javascript. Array is actually an object in javascript. In C++ array cannot be of mixed types. Also, the array may not be an object type in C++, if the array is a collection of int then it is not an object type. However, if the array is a collection of class type then it is an object type. Here is an example.

{% highlight javascript %}

var var4 = [1,2,3]; // array is a collection of values.
console.log(typeof var4); // object

var var1 = [1,2,3,'4']; // collection of mixed types

{% endhighlight %}

## How to access array elements
This is just like C or C++ language where we use subscript to access the particular element in the array. It is very similar to C except that when we access array out of boundaries in javascript then it returns undefined. In C, technically it is still undefined but in C you might get a crash or some junk value depending on how it is laid out in the memory.

{% highlight javascript %}

var var4 = [1,2,3]; // array collection of values.
console.log(var4[0]); // first element in the array.

console.log(var4[4]); // undefined.

{% endhighlight %}

Example in C - Array out of boundaries

{% highlight cpp %}

#include <stdio.h>

int main()
{
   int x[] = { 1,2,3};
   printf("The first value is x[0] = %d\r\n", x[0]);
   printf("Array out of bounds 4th element = %d\r\n", x[4]);
   return 0;

}

{% endhighlight %}

The result I saw was -

{% highlight bash %}

 ./test2.out
The first value is x[0] = 1
Array out of bounds 4th element = 545694709

{% endhighlight %}

As you can see, we got some garbage value when we accessed array out of boundaries. This is technically undefined because we can even get a crash.
Example -

{% highlight cpp %}
#include <stdio.h>

int main()
{
   int x[] = { 1,2,3};
   printf("The first value is x[0] = %d\r\n", x[0]);
   printf("Array out of bounds 4th element = %d\r\n", x[432423423]);
   return 0;

}

{% endhighlight %}

Now, when I run it , I get a bus error - crash since I am accessing some unreachable memory.

{% highlight bash %}
 ./test2.out
The first value is x[0] = 1
Bus error
{% endhighlight %}

## `undefined` in JavaScript
`undefined` is a primitive value, not an error message. It commonly indicates that a
value has not been assigned or that a property is missing. Although it can be assigned
explicitly, it is usually clearer to leave a value uninitialized or use `null` to
represent intentional absence.

{% highlight javascript %}
const missingValue = undefined;
console.log(missingValue); // undefined
{% endhighlight %}

## null
Use `null` when you intentionally want to represent the absence of an object value.

{% highlight javascript %}

var var1 = null;
console.log(var1); // null

{% endhighlight %}

## Comparing `null` and `undefined`
These are distinct JavaScript values with different types. Loose equality considers them
equal, but strict equality does not. C++ `nullptr` is a null pointer value and is not
equivalent to JavaScript `null` or `undefined`.

{% highlight cpp %}

#include <iostream>

void func(int *a);
void func(int b);

void func(int *a)
{
   std::cout<<"func with pointer type called"<<std::endl;
}

void func(int b)
{
   std::cout<<"func with int type called"<<std::endl;
}

int main()
{
   func(NULL);
   return 0;
}

{% endhighlight %}

This overload can be ambiguous because `NULL` is a macro whose definition varies by
implementation and may convert to an integer or pointer. C++11's `nullptr` provides a
dedicated null pointer value.

{% highlight cpp %}

$g++ -std=c++11 test2.cpp -o test2.out
test2.cpp: In function â€˜int main()â€™:
test2.cpp:21:13: error: call of overloaded â€˜func(NULL)â€™ is ambiguous
   21 |    func(NULL);
      |             ^
test2.cpp:7:6: note: candidate: â€˜void func(int*)â€™
    7 | void func(int *a)
      |      ^~~~
test2.cpp:12:6: note: candidate: â€˜void func(int)â€™
   12 | void func(int b)

{% endhighlight %}

## How do we fix the above issue?
nullptr is a keyword introduced in C++11. This fixes the above issue described. In order to initialize pointers with some initial reset value, we use nullptr. Now, when we call func(nullptr), it will call the func(int *a). If we call func(0) then it will call func(int b). Here is the code.

{% highlight cpp %}
#include <iostream>

void func(int *a);
void func(int b);

void func(int *a)
{
   std::cout<<"func with pointer type called"<<std::endl;
}

void func(int b)
{
   std::cout<<"func with int type called"<<std::endl;
}

int main()
{
   func(0);
   func(nullptr);
   return 0;
}

{% endhighlight %}

Now, let's compile this out and run.

{% highlight bash %}

./test2.out
func with int type called
func with pointer type called

{% endhighlight %}

In JavaScript, `null` is a primitive value, although the historical `typeof null`
behavior reports `"object"`.

{% highlight javascript %}

var x = null;
console.log(typeof x);  // object

{% endhighlight %}

## Comparing values and types
The values are different even though loose equality treats them as equal.

{% highlight javascript %}

console.log(null == undefined); // true
var y = undefined;
console.log(typeof y); // undefined

{% endhighlight %}

## Check the value and type together
In order to check the value and type together in javascript, use triple equals symbol i.e. ===.

{% highlight javascript %}

console.log(null === undefined); // false

{% endhighlight %}

## NaN
`NaN` means â€œnot a numberâ€ and is a numeric value used for invalid numeric results. It
is not an exception; use `Number.isNaN()` to test for it.

{% highlight javascript %}

var var1 = NaN;
console.log(var1); //NaN
console.log(typeof var1); //  number
{% endhighlight %}

This brings end to the very basic comparison of javascript features with C++.

References -

http://www.vishalchovatiya.com/mastering-c-books-courses-tools-tutorials-blogs-communities/
