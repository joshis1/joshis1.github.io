---
layout: post
title: "JavaScript Switch Statements and Loops"
description: "Compare JavaScript switch statements, loops, and operators with equivalent C/C++ examples."
date:   2021-03-17 14:13:31 +1300
categories: JavaScript
---

This article is all about basic javascript features like switch and looping. This is in continuation to the basic javascript conditional structs.

## switch
This is very similar to C/C++ language.
The syntax looks same i.e. switch, case, default and break. Also, the behaviour is same. In C++, you cannot use string in the case statement whereas in javascript you can do so. Here is an example.

{% highlight javascript %}
var luckyNumber = 8;

switch(luckyNumber)
  {
    case 1:
      console.log('Is 1');
      break;

    case 8:
      console.log('Is 8 ');
      break;

    default:
      console.log('Default');
      break;
  }


{% endhighlight %}

Here is the output -

{% highlight text %}

"Is 8 "
{% endhighlight %}

Now, let's code the same in C/C++.

{% highlight cpp %}

#include <stdio.h>

int main()
{
   int luckyNumber = 8;

   switch(luckyNumber)
   {
      case 1:
         printf("Is 1 \r\n");
         break;

      case 8:
         printf("Is 8 \r\n");
         break;

      default:
         printf("Default \r\n");
         break;
   }
   return 0;
}

{% endhighlight %}

In C, you will see the same result.

{% highlight text %}
Is 8
{% endhighlight %}

In C++, you cannot use string in the switch statement.
Here is the example.

{% highlight cpp %}

#include <iostream>

int main()
{
   std::string luckyName = "shreyas";

    switch(luckyName)
    {
       case "Joshi":
          std::cout<<"Joshi lucky name"<<std::endl;
          break;
       case "shreyas":
          std::cout<<"shreyas lucky name"<<std::endl;
          break;
       default:
          std::cout<<"default"<<std::endl;
    }

    return 0;

}

{% endhighlight %}

This is very much possible in javascript. Here it is proven.

{% highlight javascript %}
 var luckyName = "shreyas";

    switch(luckyName)
    {
       case "Joshi":
         console.log('Joshi lucky name');
          break;
       case "shreyas":
         console.log('shreyas lucky name');
          break;
       default:
         console.log('default');
    }
{% endhighlight %}

When we run this, we see -

{% highlight text %}

"shreyas lucky name"

{% endhighlight %}

Rest is same here, if you forget putting break then it won't break and all the following case statement will be executed. This holds true in C, C++ and javascript.

## for loop
Let's talk about the for loop in C/C++ and javascript now. You will be surprised to see the syntax here.
They both have the same syntax. Here is an example.

{% highlight javascript %}

for ( var i = 0; i < 5; i++)
  {
    console.log(i);
  }

{% endhighlight %}

Here is the output.

{% highlight text %}

 0
 1
 2
 3
 4

{% endhighlight %}

Here is the C++ version and you will see it is very similar.

{% highlight cpp %}

#include <iostream>

int main()
{
  for(int i = 0; i < 5; i++)
  {
     std::cout<<i<<std::endl;
  }
  return 0;
}

{% endhighlight %}

Also, the output is same as what we have seen in the javascript case. I won't cover nested loops since it is same as what we do in C/C++ case. Also, the break in javascript is same as C/C++. break exits out of the current control structure. continue is used to skip the statement.

## How to concatenate string and integer in javascript and C/C++
In javascript, it is very straight forward. Just use + operator to combine number with string. Here is how we do in javascript.


{% highlight javascript %}

var j = 17;
console.log('Concatenate with number = ' + j);

{% endhighlight %}

You can't do this directly in C++. However, you can use to_string() to convert int to string type and then concatenate the two strings using + operator. Here is an example.

{% highlight cpp %}

#include <iostream>
int main()
{
   int j = 17;
   std::cout<<"Concatenate with number = " + std::to_string(j)<<std::endl;
   return 0;
}

{% endhighlight %}

## Looping through arrays
In javascript, you can loop through array using its property length to identify the length of the array.
However, in C++, it is not that straight forward. Here is an example.

{% highlight javascript %}

var arr = [1,2,3,4,5];

for(var i = 0; i < arr.length; i++)
  {
    console.log(arr[i]);
  }

{% endhighlight %}

In C++, you can use the method sizeof() to determine the length of the array in bytes and then you have to divide it by the size of an element to determine the length in numbers. Here is an example.

{% highlight cpp %}

#include <iostream>

int main()
{
  int arr[] = {1,2,3,4,5};

  for(int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++ )
  {
     std::cout<<arr[i]<<std::endl;
  }
  return 0;
}

{% endhighlight %}

Now, let's run this one.

{% highlight bash %}

./test_array.out
1
2
3
4
5

{% endhighlight %}

In javascript, array is an object.

## while
Just like in C/C++, you can use while in javascript.
In short, until and unless the condition is true keep looping. Here is an example.

{% highlight javascript %}

var condition = true;
var i = 2;

while (condition) {
   if( i == 3) {
     condition = false;
   }
  console.log(i);
  i++;
}

{% endhighlight %}

The output is

{% highlight text %}

2
3

{% endhighlight %}

Let's do the same in C language.

{% highlight cpp %}

#include <stdio.h>
#include <stdbool.h>

int main()
{
   bool condition = true;
   int i = 2;

   while (condition) {
      if( i == 3) {
         condition = false;
      }
      printf("%d\r\n",i);
      i++;
   }

   return 0;
}

{% endhighlight %}

The output is same as what we have seen in the javascript case.

## do while
Just like in C, do while is supported in javascript also.
do while ensures that the loop will be executed atleast once. Here is an example.

{% highlight javascript %}

var condition = false;
 do {
    console.log('Executed');
 }while(condition);

{% endhighlight %}

Here is an output.

{% highlight text %}

"Executed"

{% endhighlight %}

This holds true even in C language.

{% highlight cpp %}

#include <stdio.h>
#include <stdbool.h>

int main()
{
  bool condition = false;
  do {
       printf("Executed\r\n");
  }while(condition);

  return 0;
}

{% endhighlight %}

## + Operator
Just like in C/C++, you can use unary operators in javascript. For e.g.

{% highlight javascript %}

var number = 5;
number++; //post increment
console.log(number); //6

++number; //pre-increment
console.log(number); //7

var a = 5;
var b = 10;
a +=b; //shorthand syntax.
console.log(a); //15

{% endhighlight %}

Here is an example in C language.

{% highlight cpp %}

#include <stdio.h>

int main()
{
  int a = 5;
  int b = 10;
  int number = 5;
  number++; //post increment
  printf("%d\r\n",number); //6
  ++number; //pre-increment
  printf("%d\r\n",number); //7
  a +=b; //shorthand syntax.
  printf("%d\r\n",a); //15
  return 0;
}
{% endhighlight %}

## + Operator in Javascript and C++
The + operator in C++ can be used to concatenate
two strings together. Also, string and number using
to_string(). However, we cannot combine bool true with string. If we try to combine then true will become 1.
Similarly, false will become 0. Here is a code snippet to demonstrate.

{% highlight cpp %}

#include <iostream>

int main()
{
  float a = 5.2;
  float b = 4.5;
  std::cout<<"Sum of a + b "<<a+b<<std::endl;

  std::string s1 = "join ";
  std::string s2 = "us";
  std::cout<<s1+s2<<std::endl;

  int c = 3;
  std::cout<<s1+ std::to_string(c)<<std::endl;

  bool val = true;
  std::cout<<s1 + std::to_string(val)<<std::endl;

  std::cout<<s1 + std::to_string(b)<<std::endl;
  return 0;
}

{% endhighlight %}

Here is the output.

{% highlight bash %}

$ ./test_plus_operator.out
Sum of a + b 9.7
join us
join 3
join 1
join 4.500000

{% endhighlight %}

In javascript, we can do these things very easily.
Here is the javascript version. Even you can combine boolean true as string with another string.

{% highlight javascript %}

var a = 5.2;
var b = 4.5;

console.log('Sum of a + b ' + (a + b) );

var s1 = "join ";
var s2 = "us";
console.log(s1+s2);

var c = 3;
console.log(s1 + c);

var val = true;
console.log(s1 + val);

{% endhighlight %}

Here is the output.

{% highlight text %}

"Sum of a + b 9.7"
"join us"
"join 3"
"join true"

{% endhighlight %}

## Concatenating array with strings
This is straightforward in JavaScript. In C++, one option is to use `std::ostringstream`
to build a string from the array elements:

{% highlight cpp %}

#include <iostream>
#include <sstream>

int main()
{
  int arr[] = {1,2,3,4};
  std::string str = "Hello";
  std::ostringstream ostr;

  for(int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++)
  {
     ostr<<arr[i];
  }

  std::string mystr = ostr.str();
  mystr.pop_back();
  std::cout<<mystr + str<<std::endl;
  return 0;
}

{% endhighlight %}
Here is the output.

{% highlight bash %}

  ./test_ostream.out
  1,2,3,4Hello

{% endhighlight %}


This is straightforward in javascript. Hre is the same code in javascript.

{% highlight javascript %}

var arr = [1,2,3,4];
var str = 'Hello';

console.log(arr + str);

{% endhighlight %}

Here is the output.

{% highlight text %}

"1,2,3,4Hello"

{% endhighlight %}

In C++, you cannot simply concatenate array with a string. You need to first convert that array into string. You can do this by using a ostringstream data type to insert each element. Next, call str() method of ostringstream to convert that into string.
So, its a bit of work. Many can argue that C++ lacks such features. There is another way to look into it. C++ allows user to implement the way user wants rather than forcing them. This makes C++ more flexible but at the same time you need to do more hard work. It all depends on what you want. I like the idea that if I can design my system very well then I know what logic needs to be fast and what needs to be normal.
This way the fast part I can implement in C++ whereas the other parts I can implement in javascript.

## Add boolean with int in javascript and C++
As you already know that true in C++ is nothing but 1 and false in C++ is nothing but 0. This is true even in javascript. So, if you add int with true then it will add 1 to the int value. Similarly, if you will add false with a number then the value won't change since you are adding 0 effectively. Here is the C++ code snippet.

{% highlight cpp %}

#include <iostream>

int main()
{
  bool a = true;
  int  b = 12;
  bool c = false;
  std::cout<< a + b<<std::endl;
  std::cout<<c + b  <<std::endl;
  return 0;
}

{% endhighlight %}

Here is the output since true is 1 therefore when you add 12 with true, it becomes 13. Similarly, false is 0 therefore when you add 12 with false, it remains 12. Here is the output.

{% highlight bash %}

$ ./test_bool_add.out
13
12
{% endhighlight %}

Now, let's check the same behaviour in javascript. You will see that javascript behaves exactly like the above. Here is the code snippet.

{% highlight javascript %}

  var a = true;
  var b = 12;
  var c = false;
  console.log(a+b);
  console.log(b+c);

{% endhighlight %}

The output is same 13 and 12.

## Add variable with null
You shouldn't try adding null with the integer in C++ since it is a bad thing. But, the point is that null is nothing but 0 in value. This is what you will see if you add null to int in C++. Obviously, you will get a compilation warning since null is actually (void*)0 so you are converting pointer to non pointer type here. Here is the snippet code. By the way in C++ we have NULL and it is all in upper case because internally it is a macro. In javascript, null is all in lowercase and has a value 0.

{% highlight cpp %}

#include <iostream>
int main()
{
  int a = 12;
  int b = NULL;
  std::cout<<a+b<<std::endl;
  return 0;
}

$ g++ test_null.cpp -o test_null.out
test_null.cpp: In function ‘int main()’:
test_null.cpp:6:11: warning: converting to non-pointer type ‘int’ from NULL [-Wconversion-null]
    6 |   int b = NULL;

{% endhighlight %}

Here is the javascript version of using null.

{% highlight javascript %}

var a = 12;
var b = null;

console.log(a+b); //output is 12
console.log(typeof null); // object

{% endhighlight %}

## Adding number with undefined in javascript
You cannot add undefined with a number in javascript.
If either operand is `undefined`, numeric addition produces `NaN`. `undefined` is a
JavaScript value, not an error; assigning it explicitly is usually unnecessary.

{% highlight javascript %}

var a = 12;
var b = undefined;
console.log(a+b); // NaN

{% endhighlight %}

## Adding number with NaN in javascript
You cannot add NaN with a number in javascript. If you do so, then the result will be NaN.

{% highlight javascript %}

var a = 12;
var b = NaN;

console.log(a+b); //NaN

{% endhighlight %}

## Subtraction in javascript
The subtraction of numbers in javascript is same as in C.
Here is the code snippet.

{% highlight javascript %}

var a = 12;
var b = 1;
a -=b;
console.log(a); //11
a--;
console.log(a); //10
--a;
console.log(a); //9

{% endhighlight %}

Here is the code in C language.

{% highlight cpp %}

#include <stdio.h>

int main()
{
  int a = 12;
  int b = 1;
  a -=b;
  printf("%d\r\n",a); //11
  a--;
  printf("%d\r\n",a); //10
  --a;
  printf("%d\r\n",a); //9
  return 0;
}

{% endhighlight %}

## Subtract a substring from a string in javascript and C++
This is neither supported by javascript nor by C++ directly. You cannot use - operator to subtract substring from a string.

In C++, in order to delete a substring from a string, first you need to get the starting index of the matching substring using find(). Here is the code snippet to do so.
In C++, we need index to find out where the first occurence of the substring starts and then delete from there using the substring length.

{% highlight cpp %}

#include <iostream>
int main()
{
 std::string s1 = "Split us";
 std::string s2 = "us";
 int pos = s1.find(s2);
 //std::cout<<pos<<std::endl;
 s1.erase(pos,s2.length());
 std::cout<<s1<<std::endl; // Split
 return 0;
}

{% endhighlight %}

Let's do the same thing in javascript.
In javascript, we can simply use replace() method of string to replace the substring with nothing i.e. "". Here is the code snippet.

{% highlight javascript %}

 var a = 'Split us';
 var b = 'us';
 var result = a.replace(b,"");
 console.log(result); //Split

{% endhighlight %}

In case you simply try to use - operator in javascript to delete a substring from a string then you will get NaN. Here is a code snippet. Similarly, in C++ you will get a compilation error.

{% highlight javascript %}

var a = 'Split us';
var b = 'us';
console.log(a -  b); //NaN

{% endhighlight %}

## Subtract a string number from a number
In javascript, if you try to subtract a string number from a number then javascript will try to change the string number into a number and do the subtraction. In a way, javascript is smart enough to interpet this what a user might be wanting. Here is a code snippet.

{% highlight javascript %}

 var a = 12;
 var b = '1';
 console.log(a - b); //11
 console.log(b - a);; // -11

{% endhighlight %}

In C++, you need to use stoi() to convert string to integer. You cannot simply subtract it. Also, you need to do exception handling in case you are passing invalid string that cannot be converted to int. In this code, I am not handling the exception. Ideally, your code should be inside try block to catch any associated exceptions.

{% highlight cpp %}

#include <iostream>

int main()
{
  std::string b = "1";
  int a = 12;
  std::cout<<"a-b "<<a - std::stoi(b)<<std::endl;
  std::cout<<"b-a "<<std::stoi(b) - a <<std::endl;
  return 0;
}

{% endhighlight %}

Here is the output.

{% highlight bash %}

$ ./test_subtract_string_number.out
a-b 11
b-a -11

{% endhighlight %}

## Multiplication of numbers in C++ and javascript
The multiplication of numbers in C++ and javascript are same. Here is the javascript version using shorthand.

{% highlight javascript %}

 var a = 12;
 var b = 2;
 a *=b;
console.log(a); //24

{% endhighlight %}

Here is the C++ version, which is same.

{% highlight cpp %}

  #include <iostream>
  int main()
  {
    int a = 12;
    int b = 2;
    a *=b;
    std::cout<<a<<std::endl; //24
    return 0;
  }

{% endhighlight %}

Just like pre-increment or post-increment, we cannot do pre or post multiplication in C or javascript. Here is a code snippet. You will get a syntax error in javascript as well as C++.

{% highlight javascript %}
 var a = 12;
 console.log(a**);
{% endhighlight %}

Here is the C++ version.

{% highlight cpp %}

#include <iostream>

int main()
{
  int a = 12;
  std::cout<<a**;
  return 0;
}

$ g++ test_multiply_shorthand.cpp -o test_multiply_shorthand.out
test_multiply_shorthand.cpp: In function ‘int main()’:
test_multiply_shorthand.cpp:6:17: error: expected primary-expression before ‘;’ token
    6 |   std::cout<<a**;

{% endhighlight %}

## Multiplying float number with integer in javascript and C++
There is no concept of floating point and int in javascript. In javascript the decimal number and integers are nothing but numbers only. In fact, you will find a lot of issues with floating point numbers in javascript here. Execuse me a number in javascript which has decimal points since there is nothing called floating point in javascript.

{% highlight javascript %}

 var a = 1.3;
 var b = 2;
 console.log(a*b); //2.6

{% endhighlight %}

Similarly in C++, you need to use float to store the result.

{% highlight cpp %}

#include <iostream>

int main()
{
  float a = 1.3;
  int b = 2;
  std::cout<<a*b<<std::endl;
  float c = a * b;
  int d = a * b;
  std::cout<<"Stored in float "<<c<<std::endl;
  std::cout<<"Stored in int "<<d<<std::endl;
  return 0;
}

./test_float.out
2.6
Stored in float 2.6
Stored in int 2

{% endhighlight %}

As you can see above the results are same. If you use int to store the floating point number in C then the decimal part will be truncated.

## Multiplying floating point number with another floating point number in javascript and C++
Well, this is a very big topic in the sense that javascript stores number in the 64 bit floating point adhering to the IEEE 754 standard. This leads to the fact that floating point mathematics doesn't lead to the accurate number. For example, open the calculator and multiply 1.3 and 2.2, you should get 2.86. However, when you do the same in the javascript world, you will get some other result. This is because of the fact that javascript stores the number according to the IEEE 754 standard i.e. 64 bit binary format. Here is the code snippet.

{% highlight javascript %}

console.log(1.3 * 2.2); //2.8600000000000003

{% endhighlight %}

So, what is IEEE-754 standard says, it represents the number in 1 bit for sign, 11 bits for exponent and 52 bits for Mantissa. For example, represent 263.3 in the
IEEE-754 standard.

{% highlight text %}

 263 in binary is 100000111
 0.3 in binary is (0.01001-----)
 Now, combine them
 100000111.01001-----
 Now, move the decimal point to extreme left with only 1 bit left. Here is the output.

 1.0000011101001----- , in order to do that you shifted 8 positions.
 Now, you have to multiply with 2^8.

 1.0000011101001----- * 2^8

 Now, represent this in IEEE 754 format.
 Sign bit is 0 since it is a positive number.
 sign - 0
 exponent - 8 exp bits, add 127 + 8 to 135
 Mantissa - fraction bits - 0000011101001

{% endhighlight %}

This was all about internals. How, do we actually get what we want. We can use big.js javascript library to get the normal results. Also, we can use toFixed() to get around this. Here is a code snippet.

{% highlight javascript %}

 var a = 1.3;
 var b = 2.2;
 console.log((a * b).toFixed(2)); //2.86

{% endhighlight %}

## Multiplying floating number represented as string with a number
In javascript, when you try to multiply '2.2' i.e a string with a number, javascript is intelligent enough to deduce that you want to multiply two numbers. Thus, it automatically converts the string '2.2' into a number and then multiplies it with another number.  Here is the code snippet.

{% highlight javascript %}

 var a = 2;
 var b = '2.2';
 console.log(a*b); //4.4

{% endhighlight %}

In C++, this cannot happen implicitly, you need to convert the string to a floating point. Just like std::stoi(), you can use std::stof(). Ideally, you should do this inside try block to catch any translation issues. Here is the code block.

{% highlight cpp %}

#include <iostream>

int main()
{
  int a = 2;
  std::string b = "2.2";

  float c = std::stof(b);
  std::cout<<c<<std::endl;
  std::cout<<"Result = "<<a*c<<std::endl; // 4.4

  return 0;
}

{% endhighlight %}

## Multiplying a alphanumeric string with another string
In javascript, this will lead to NaN i.e. not a number. In C++, you will get a compilation error when you try to multiply two strings. Here is the javascript code snippet.

{% highlight javascript %}

  var a = 'another';
  var b = 'join';
  console.log(a*b); //NaN

{% endhighlight %}

You cannot do this in C++, you will get compile time error. no match for operator *.

## Multiplying number with null
In javascript null or in C++ NULL is nothing but 0. So, if you multiply null with a number then you will get 0 in both the cases. Here is the code snippet. Ideally, you never multiply null with a number but what if somebody does is the question.

{% highlight javascript %}

  var a = 12;
  var b = null;
  console.log(a*b); //0

{% endhighlight %}

Let's see this in C++. In C++, we have NULL and not null. The NULL is nothing but pointer type i.e (void*)0. So, in the below code first you will get warning since you are converting from pointer type to non-pointer type. However, you will get the same result i.e. 0. Here is the code.

{% highlight cpp %}

#include <iostream>
int main()
{
  int a = 12;
  int b = NULL;

  std::cout<<a*b<<std::endl;
  return 0;
}

$g++ test_number_null_mul.cpp -o test_number_null_mul.out
test_number_null_mul.cpp: In function ‘int main()’:
test_number_null_mul.cpp:6:11: warning: converting to non-pointer type ‘int’ from NULL [-Wconversion-null]
    6 |   int b = NULL;

Output -
$ ./test_number_null_mul.out
0

{% endhighlight %}

## Multiplying number with infinity
The results are same if you multiply a number with infinity then the result is infinity. In C++, we have to use floating point to get the infinity. You have to use static method infinity() of numeric_limits template.
Here is an example.

{% highlight cpp %}

#include <iostream>
#include <limits>

int main()
{
  float a = std::numeric_limits<float>::infinity();
  std::cout<<a<<std::endl;
  int number = 12;

  std::cout<<a * number<<std::endl;

  return 0;
}

{% endhighlight %}

Here is the output and you can see that you get infinity as a result.

{% highlight bash %}
./test_infinity.out
inf
inf

{% endhighlight %}

In javascript, you have a keyword called Infinity. When you multiply a number with Infinity you get Infinity as a result. Here is a code snippet.

{% highlight javascript %}

var a = Infinity;
var number = 12;
console.log(a*number); // Infinity

{% endhighlight %}

## Division and Modulus
This is very much like C/C++.
You can use / to get the value and % to get the remainder.
Here is an example.

{% highlight javascript %}

  var a = 12;
  var b = 2;
  a/=b;
  console.log(a);  //6
{% endhighlight %}

Let's do the same thing in C/C++. You will find that it behaves exactly the same.

{% highlight cpp %}

 #include <iostream>

 int main()
 {
   int a = 12;
   int b = 2;
   a/=b;
   std::cout<<a<<std::endl; //6
   return 0;
 }

{% endhighlight %}

## Division of a number by a number in a string format
In C++, you need to convert that number in a string format to a number format then only you can do the division. However, in javascript this will happen implicitly. Here is the code.

{% highlight javascript %}

 var a = 12;
 var b = '2';
 console.log(a/b);

{% endhighlight %}

## Floating point division in javascript
The problem exists even for floating point division. This is because of the fact that we have already discussed - IEEE -754. For example, if you divide 3.3/2.2, you should get 1.5. However, in javascript you get the answer different. Here is the code snippet.

{% highlight javascript %}

  var a = 3.3
  var b = 2.2;
  console.log(a/b); // 1.4999999999999998
  console.log((a/b).toFixed(2)); // 1.50

{% endhighlight %}

## Modulus gives remainder of the division
In C,C++ and javascript the modulus operator i.e % gives the remainder of the division. Here is an example.

{% highlight javascript %}

   var a = 10;
   var b = 3;
   console.log(a % b); // 1

{% endhighlight %}

## Division by Zero
If you divide a number by zero in javascript then you will get infinity as a result. In C++, if you divide a floating point with a zero then you will get infinity. However, if you divide integer with zero then you will get floating point exception error. Here is a C++ version.

{% highlight cpp %}

#include <iostream>

int main()
{
  float a = 10;
  float b = 0;
  std::cout<<a/b<<std::endl;
  std::cout<<5/0<<std::endl;
  return 0;
}

{% endhighlight %}

Here is the output. As you can see when the floating point number is divided by zero then you get infinity. However, you get floating point exception when you divide an integer with zero. I will say all these are architecture specific. If you have a power pc architecture then you might not even get an exception because power pc will handle the exception. I will say in C/C++ it is more architecture specific. I will never try to divide a number by zero in C/C++. If there is a possibility then I will keep it inside a try block and catch any exception.

{% highlight bash %}

$ ./test_division_by_zero.out
inf
Floating point exception

{% endhighlight %}

Here is a javascript version of dividing a number with zero.

{% highlight javascript %}

  var a = 10;
  var b = 0;
  console.log(a/b); // infinity.
  console.log(a%b); //NaN -- cant get any remainder.

{% endhighlight %}

## Dividing a number with infinity
When you divide a number with infinity you get zero both in C, C++ and javascript. Here is a C++ code.

{% highlight cpp %}
#include <iostream>
#include <limits>

int main()
{
  float a = std::numeric_limits<float>::infinity();
  int b = 10;
  std::cout<<b/a<<std::endl;  // 0
  return 0;
}

{% endhighlight %}

Similalry, when you divide a number with infinity in javascript you get 0. Here is a javascript code.

{% highlight javascript %}

 var a = Infinity;
 var b = 10;
 console.log(b/a); // 0

{% endhighlight %}

## Operators to compare values
In javascript, as you already know that double equals doesn't check the typeof the variable it simply compares the values. So, it is a best practice to use triple equals in order to compare the values in javascript. Here is the code snippet.

{% highlight javascript %}

console.log( 1 == 1); // true
console.log( 1 === 1); // true

console.log( 1 == '1'); // true
console.log( 1 === '1'); // false

console.log( 1 != 2); // true
console.log( 1 != '1'); // false
console.log( 1 !== '1'); // true

console.log( 1 >  0); // true
console.log( 1 >  1); // false
console.log(1 >= 1); //true

{% endhighlight %}

## Wierd comparison rules in javascript
We cannot compare NaN with anything. We cannot compare null with anything. If we do so then it will return false. Here is the code snippet.

{% highlight javascript %}

 console.log( NaN == NaN); //false
 console.log( 0 == null);  //false


{% endhighlight %}

Loose equality has special rules for `null` and `undefined`, while strict equality
distinguishes them. `NaN` is unequal to every value, including itself. Do not generalize
these comparisons to “anything compared with undefined is false.”

{% highlight javascript %}

 console.log( null == undefined); //true
 console.log( 0 == undefined);  //false

 {% endhighlight %}

## boolean operators
This is same in C/C++ and javascript. For 'and' condition you have to use && and for 'or' condition you have to use || operator. Also, you can use ! operator to negate the condition.

## Ternary operator
Just like in C, you can use ternary operator in javascript also. Here is an example.

{% highlight javascript %}

var a = 10;
var b = 10;
console.log( a == b ? 'Equal' : 'Not Equal');

{% endhighlight %}

## Precedence in javascript
JavaScript operators have defined precedence and associativity; do not rely on a
mnemonic such as BODMAS for language expressions. Use parentheses when they improve
clarity, and consult the reference:

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence


This brings end to the basic language constructs of javascript which is very much comparable to C, C++ except the floating point.

References -

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence


Practice javascript using -

https://jsbin.com/
