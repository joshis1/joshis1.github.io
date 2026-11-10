---
layout: post
title: "JavaScript Objects, Prototypes, and Functions"
description: "An introduction to JavaScript object creation, properties, prototypes, constructors, and function methods."
date:   2021-04-01 14:13:31 +1300
categories: JavaScript
---

JavaScript objects are accessed through references. This article introduces object
creation, property access, prototypes, constructors, and function methods.

## Creation of object
There are various ways to create an object. We will discuss all these methods to create an object here.

## Simply notational way to create an object
A simple way to create an object in javascript is shown below. An object consists of properties and function. Also, within an object you can have another object. Let's have a look here.

{% highlight javascript %}

  var person = {
    name: 'Shreyas', //field name and value
    age: 38,
    details: {
     hobbies: ['sports', 'guitar', 'photography'],
     location: 'Australia',
    },
    greet: function() {
     console.log('Hello ' + this.name);
    },
  };

console.log(person.name); // "Shreyas"
console.log(person.details.hobbies); //["sports", "guitar", "photography"]
person.greet(); //"Hello Shreyas"

{% endhighlight %}

Here person stores the reference to the piece of memory that points to the data shown above.
Now, let's make identical memory. However, since these are two different memory their references will differ too.
Check this out.

{% highlight javascript %}

  var person = {
    name: 'Shreyas', //field name and value
    age: 38,
    details: {
     hobbies: ['sports', 'guitar', 'photography'],
     location: 'Australia',
    },
    greet: function() {
     console.log('Hello ' + this.name);
    },
  };

  var person_1 = {
    name: 'Shreyas', //field name and value
    age: 38,
    details: {
     hobbies: ['sports', 'guitar', 'photography'],
     location: 'Australia',
    },
    greet: function() {
     console.log('Hello ' + this.name);
    },
  };

  console.log(person == person_1); // false: these are distinct object instances.

{% endhighlight %}

## How to access field value in object
Use dot notation when the property name is known, or bracket notation when it is
computed or not a valid identifier. JavaScript objects are not associative arrays.

{% highlight javascript %}

var person = {
    name: 'Shreyas', //field name and value
    age: 38,
    details: {
     hobbies: ['sports', 'guitar', 'photography'],
     location: 'Australia',
    },
    greet: function() {
     console.log('Hello ' + this.name);
    },
  };

  var field = 'age';
  console.log(person[field]); //38
  console.log(person['details']['hobbies']); // ["sports", "guitar", "photography"]

  console.log(typeof person); //object
  console.log(typeof person.name); //string
  console.log(person instanceof Object); //true

{% endhighlight %}

Another definition of object is that it is nothing but key,value pairs including functions.

## Using new to create an object
`Object()` can return the same object passed to it; it does not clone the object or set it
as a new object's prototype.

{% highlight javascript %}

  var person = {
    name: 'Shreyas', //field name and value
    age: 38,
    details: {
     hobbies: ['sports', 'guitar', 'photography'],
     location: 'Australia',
    },
    greet: function() {
     console.log('Hello ' + this.name);
    },
  };

  var samePerson = new Object(person);
  console.log(samePerson === person); // true

{% endhighlight %}

Passing `null` to `new Object()` still creates an ordinary object. To create an object
with no prototype, use `Object.create(null)`:

{% highlight javascript %}

 var personUnique = new Object(null);
 console.log(personUnique); //[object Object] { ... }
 console.log(personUnique instanceof Object); // true

{% endhighlight %}

## Using `Object.create()`
`Object.create()` creates an object with the supplied prototype.

{% highlight javascript %}

 var person = {
    name: 'Shreyas', //field name and value
    age: 38,
    details: {
     hobbies: ['sports', 'guitar', 'photography'],
     location: 'Australia',
    },
    greet: function() {
     console.log('Hello ' + this.name);
    },
  };
 var objPerson = Object.create(person);
 objPerson.name = 'Neha';
 console.log(objPerson.age); //38
 console.log(objPerson.name); //Neha
 objPerson.greet(); // "Hello Neha"
 console.log(objPerson instanceof Object); // true
 console.log(Object.getPrototypeOf(objPerson) === person); // true

{% endhighlight %}

The Object.create() way has an advantage that we can use prototype i.e. inheritance easily. You can also create an object without using prototype field i.e. by passing null. Here is an example.

{% highlight javascript %}

 var objPerson = Object.create(null);
 console.log(objPerson);
 console.log(objPerson instanceof Object); //false

{% endhighlight %}

## Prototypes
Property lookup follows an object's prototype chain. Ordinary object literals inherit
from `Object.prototype`; avoid modifying built-in prototypes because changes affect
unrelated code.

{% highlight javascript %}

var person = {
    name: 'Shreyas', //field name and value
    age: 38,
    details: {
     hobbies: ['sports', 'guitar', 'photography'],
     location: 'Australia',
    },
    greet: function() {
     console.log('Hello ' + this.name);
    },
  };

 console.log(Object.getPrototypeOf(person)); // Object.prototype
 console.log(person.checkout); // undefined
 console.log(person.toString()); // "[object Object]"

{% endhighlight %}

An object can inherit from a prototype object without changing `Object.prototype`:

{% highlight javascript %}

var greeter = {
  greet: function() {
    console.log('Hello ' + this.name);
  }
};

var person = Object.create(greeter);
person.name = 'Shreyas';
person.greet(); // "Hello Shreyas"

{% endhighlight %}

prototypes are nothing but blue prints and you can create more objects using that blue print. Here is an example.

{% highlight javascript %}

var person = {
    name: 'Shreyas', //field name and value
    age: 38,
    details: {
     hobbies: ['sports', 'guitar', 'photography'],
     location: 'Australia',
    },
    greet: function() {
     console.log('Hello ' + this.name);
    },
  };

var sj = Object.create(person);
sj.name = 'SJ';

var neha = Object.create(person);
neha.name = 'Neha';

sj.greet();   //"Hello SJ"
neha.greet(); // "Hello Neha"

console.log(sj.__proto__ == person); // true
console.log(neha.__proto__ == person); // true

console.log(Object.getPrototypeOf(sj) == person); //true
console.log(Object.getPrototypeOf(neha) == person); //true

{% endhighlight %}

## Constructor functions
Another way to create an object is using constructor functions. This is a more preferred way than anything else. Here is the constructor function.


{% highlight javascript %}

 function Person(name, age) {
   this.name = name
   this.age = age
   this.greet = function() {
     console.log('Hello ' + this.name);
   }
 }

 var person1 = new Person('Neha',34);
 var person2 = new Person('Shreyas', 38);

 person1.greet();  // Hello Neha
 person2.greet();  // Hello Shreyas

 Person.prototype.name = 'noname';
 console.log(person1.name); // "Neha"
 console.log(person1 instanceof Person);  //true

 Person.prototype.greetGeneral = function() {
    console.log('General Hello ' + this.name);
 };

 person1.greetGeneral(); //General Hello Neha
 person2.greetGeneral(); //General Hello Shreyas

 var person3 = new Person();
 console.log(person3.name); //undefined

{% endhighlight %}

## `bind()`
`bind()` returns a new function with a chosen `this` value. The value of `this` in an
ordinary function call depends on how the function is called; it is not always the
browser `window` object.

{% highlight javascript %}

 function fn() {
    console.log(this);
  }

  var obj = {
   objFn: fn
  };

  var person = {
    name: 'Shreyas',
    age: 38
  };

 console.log(this); // Depends on script mode and runtime.
 obj.objFn(); //  obj object
 // Bind the current this value.
 obj.objFn.bind(this)(); // Now again you get Windows Object
 // Let's bind person's obj here.
 obj.objFn.bind(person)(); // person's object you are binding now.

{% endhighlight %}

Passing multiple arguments to the function using bind() call. You can pass multiple arguments to the function if the function requires that with bind(). Here is an example.

{% highlight javascript %}

 function fn(message) {
    console.log(message + this);
  }

  var obj = {
   objFn: fn
  };

  var person = {
    name: 'Shreyas',
    age: 38
  };

 obj.objFn.bind(person, 'Hi')(); // person's object you are binding now.

{% endhighlight %}

## `call()` and `apply()`
`call()` and `apply()` invoke a function immediately with a chosen `this` value.
`call()` accepts arguments individually; `apply()` accepts an array-like value. Unlike
either method, `bind()` returns a new function.

{% highlight javascript %}

 var person1 = {
   firstname: 'Shreyas',
   lastname: 'Joshi'
 };

 var person2 = {
  firstname: 'Neha',
  lastname: 'Gaud'
 };

 function say(greeting) {
   console.log(greeting + ' ' + this.firstname + ' ' + this.lastname);
 }

 say.call(person1, 'Hello');
 say.call(person2, 'Hello');

 var sayHelloSJ = say.bind(person1); // "Hello Shreyas Joshi"
 var sayHelloNeha = say.bind(person2); //"Hello Neha Gaud"

sayHelloSJ('hello'); // "hello Shreyas Joshi"
sayHelloNeha('hello'); // "hello Neha Gaud"

{% endhighlight %}

Here is an example of `apply()`:

{% highlight javascript %}

 var person1 = {
   firstname: 'Shreyas',
   lastname: 'Joshi'
 };

 var person2 = {
  firstname: 'Neha',
  lastname: 'Gaud'
 };

 function say(greeting) {
   console.log(greeting + ' ' + this.firstname + ' ' + this.lastname);
 }

 say.apply(person1, ['Hello']); //"Hello Shreyas Joshi"
 say.apply(person2, ['Hello']); //"Hello Neha Gaud"

{% endhighlight %}

## Object.defineProperty
According to MDN, this static method Object.defineProperty() defines a new property directly on an object, or modifies an existing property on an object, and returns the object.


With this property, you can also create a getter and setter for the property. Here is an example.

{% highlight javascript %}

 var person = {
   firstname: 'Shreyas',
   lastname: 'Joshi'
 };

 Object.defineProperty(person, "fullName", {
  get: function() {
   var fName =  this.firstname + ' ' + this.lastname;
   return fName;
  },

  set : function(fName) {
   //console.log(fName);
   var stringArray = fName.split(/(\s+)/);
   //console.log(stringArray);
   this.firstname = stringArray[0];
   this.lastname = stringArray[2];

  }
 });

 console.log(person.fullName); //"Shreyas Joshi"
 person.fullName = "Neha Gaud";
 console.log(person.fullName); // "Neha Gaud"

{% endhighlight %}

Also, you can add a property to an object using Object.defineProperty() static method. Here is an example. Let's say the account object has just withdraw function and now you want to add deposit function at the same time. This can be achieved using Object.defineProperty method. Here is an example.

{% highlight javascript %}

 var account = {
   cash: 12000,
   withdraw: function(amount) {
     this.cash -= amount;
     console.log('Withdraw ' + amount + ', new cash reserve is: ' + this.cash);
   }
 };

 account.withdraw(1000); //"Withdraw 1000, new cash reserve is: 11000"

//built in keys available for defineProperty like value.

 Object.defineProperty(account, 'deposit', {
   value: function(amount) {
     this.cash +=amount;
   }
 });

 account.deposit(3000);
 account.withdraw(0); //"Withdraw 0, new cash reserve is: 14000"

{% endhighlight %}

Other built in keys in Object.defineProperty like writable, enumerable, etc. Note by default writable is false. It means that we cannot change the property value unless we set the writable to true. Here is an example with writable set to true.

{% highlight javascript %}

 var account = {
   cash: 12000,
   withdraw: function(amount) {
     this.cash -= amount;
     console.log('Withdraw ' + amount + ', new cash reserve is: ' + this.cash);
   }
 };

Object.defineProperty(account, 'name', {
  value: '1000-1',
  writable: true  // by default writable is false.
});

console.log(account.name); //1000-1
account.name = '1000-3'; //this won't change if writable is not set to true
console.log(account.name); //1000-3

{% endhighlight %}

## Delete a property of an object
In javascript, if you want to delete a property of an object then you can use delete keyword. Here is an example.

{% highlight javascript %}

var person = {
   name: 'SJ',
   age: 38,
   city: 'Brisbane',
   greet: function() {
     console.log('Hello ' + this.name);
   }
};

console.log(person.name); //SJ
console.log(person.age); //38
delete person.age;
console.log(person.age); //undefined
person.greet(); // "Hello SJ"
delete person.name;
person.greet(); // "Hello undefined"

{% endhighlight %}

## Determine whether a property exists
The `in` operator checks both the object and its prototype chain. Use
`Object.hasOwn()` (or `Object.prototype.hasOwnProperty.call()` on older runtimes) when
you need to check only an own property.

{% highlight javascript %}

var person = {
   name: 'SJ',
   age: 38,
   city: 'Brisbane',
   greet: function() {
     console.log('Hello ' + this.name);
   }
};

console.log('name' in person); //true
console.log('NAME' in person); //false
console.log('greet' in person); //true
console.log('city' in person); //true

{% endhighlight %}


## Loop through own enumerable properties

`for...in` can also visit enumerable properties inherited from the prototype chain. Use
`Object.keys()` when you want to iterate over an object's own enumerable string keys.

{% highlight javascript %}

var person = {
   name: 'SJ',
   age: 38,
   city: 'Brisbane',
   greet: function() {
     console.log('Hello ' + this.name);
   }
};

for (var field of Object.keys(person)) {
  console.log(field + ' is ' + person[field]);
}

{% endhighlight %}

This brings an end to the elementary introduction of an object in javascript.

References -

https://stackoverflow.com/questions/15455009/javascript-call-apply-vs-bind#:~:text=Call%20invokes%20the%20function%20and,and%20any%20number%20of%20arguments.

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind

https://jsbin.com/vomadedive/edit?html,js,console,output
