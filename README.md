# Python: Where to start
In this guide, we are going to cover the fundamentals of Python as a programming language.

To be sure that all that you can find what you want, here is a list of the topics that will be covered. Simply go to what area of the document you would like to visit.

- [Introduction/The Starting Point](#introductionthe-starting-point)
- [Commenting Code](#commenting-code)
- [Data Types](#data-types)
- [Numbers and Mathematical Operators](#numbers-and-mathematical-operators)
- [Strings](#strings)
- [Boolean and Equality Operators](#boolean-and-equality-operators)
- [Variables](#variables)
- [Concatenation and String Methods](#concatenation-and-string-methods)
- [Control Flow](#control-flow)
- [Lists and Dictionaries](#lists-and-dictionaries)
- [Loops (While, For)](#loops-while-for)
- [Functions](#functions)

Just remember: Python can be a puzzle. Do not panic if you are stuck, just logically think about all of the information you know!


## Introduction/The Starting Point

We will assume that you have a code editor on hand when beginning this tutorial, but if you do not then you *must* get one as soon as possible. Standard text editors, while they do accept python code, do not allow you to have extra support for problems that may arise, such as trying to remember where a bracket would need to go (more on that later).

For now, ensure that you have one and, to ensure that you can run the code you create, an ability to run any code you write. PyCharm, recommended by many, has this capability built in, but there are plenty of alternatives you can use.

Now that you have the ability to run code, let's do just that. All programming languages should have you start with "Hello World" to understand the syntax and workings of the language. Try running the following in your python .py file in use:

```py
print("Hello, world!")
```
If your environment if successfully set-up, you should be able to run this and receive the output "Hello, world!" in the results terminal (this should appear on your screen after running the code if it wasn't already present. If it hasn't appeared, consult the help guide of the software you are using, you could either not have it set-up correctly or there might be simply a minimised terminal somewhere.

Assuming there are no issues, congratulations! You have just written your first piece of code in Python and got it to run successfully. Now, there is plenty more to learn, as we will see, but this first step being done right is an excellent start.

## Commenting Code

Before we progress into the actual main information of Python, a quick note. When it comes to coding, it is a much needed formality to be able to comment your code. What this means is giving a sort of "commentary" on what your code is doing throughout the process. Not only does this help explain things to someone who may be reading your code, but it may also help explain it to yourself! Everyone, even the best programmers, forget things, so imagine how frustrating it would have to be to revisit an old piece of work in Python (or any other programming language for that matter) that you have made, only to realise you have not explained how it works. You would have to revisit all of it and relearn it, while you could just save yourself the hassle and comment where needed!

Here is an example of commenting within a piece of code:
```py
# This is a commented line in the code, we use the hash symbol for comments.

print("Hello, world!")
# This function prints to the console the phrase "Hello, world!"

"""
You can also use three pairs of speech marks for multi-line comments, which are commonly used in scripts as an authoring tool at the beginning.

Comments are not read by the program when the code is ran, so you are free to put whatever you need to in the comments as they will not affect the output!
"""
```
Practise your ability to write code and comment at the same time, then move onto the next section.

## Data Types

Now that you know your code is working and you can comment effectively, here is a list of what data types you are likely to see during your time with Python:
- Strings: `"Strings are written like this within Python, surrounded by quotation/speech marks. If it is within the marks, it is part of the string, so all of this is in this example!"`.
- Integer Numbers: If you are familiar with mathematics in school, you may be aware that an integer is, simply put, a whole number. This means any number from `1` to `100` and beyond are integers, so long as they are whole.
- Floating Point Numbers: In the most straightforward definition, a floating point is a decimal number in Python. This is any number that is either **NOT** whole, ***OR*** is a whole number but with an included decimal value. For example, `26.4` is a floating point number, but also so is `90.0` as it has been written with a decimal despite in mathematics this being classified as a whole number. In Python, this means it isn't an integer.
- Boolean: Boolean is simply put one of two statements, "True" or "False". In code, this is written as `True` or `False` (it may be helpful to know that you can in some cases use `0` for Boolean values to indicate false instead of the word and also `1` (or simply not `0`) to indicate a Boolean to be true. This isn't to say that 0 is a Boolean rather than an integer, but rather it is just an equivalent to it for if a comparison is necessary.

## Numbers and Mathematical Operators

By now you should know about the `print()` function and data types. With your knowledge of these, let's test printing values other than strings.
```py
print(23)
print(26.5)
print(18.0)
print(True)
```
When you run this code, you should get an output of:
```
23
26.5
18.0
True
```
So, we know that we can print these data types without a problem. But what if we have a value that we cannot figure out before printing, or maybe a trick value such as `"True"`? This example is NOT a boolean, yet when you print it it will have the same output as the boolean value `True`! Luckily, there is a way to get around this. Python has a way to show you what type of data a value is, so we can just print *that* to the output instead to find out what type it really is.

```py
print(type(23))
print(type(26.5))
print(type(18.0))
print(type(True))
print(type("True"))
```
Running the above code will lead to an output of:
```
<class 'int'>
<class 'float'>
<class 'float'>
<class 'bool'>
<class 'str'>
```
Where `'int'` refers to integers, `'float'` refers to floating point numbers, `'bool'` refers to boolean values and `'str'` refers to strings. We can now distinguish between values super easily! Of course, this is not every type of data type you will come across, but for now it is a good starting point.

We can also use mathematical operators within the print function to receive an output of the calculated value. For example:
```py
print(23 + 7)
print(23 - 7)
print(23 * 7)
print(23 / 7)
print(23 % 7)
```
returns:

```
30
16
161
3.2857142857142856
2
```
Note that the division operator results in a floating point number despite both numbers being integers in the input. This isn't a result of just this example, division always results in a floating point number.

You should hopefully be familiar with + as the operator for addition, - as the operator for subtraction, * as the operator for multiplication and / as the operator for division. You are excused however if you are not familiar with the last operator seen, %. This is the modulo operator, which returns the remaining amount once the division of the first number over the second number has been completed. For example, with `23 % 7`, we have 7, 14, 21...and then we cannot get any further without going beyond the goal of 23, so the modulo gives the result for `23 - 21`, so `2`. This value the modulo gives will of course therefore be `0` if a number divides perfectly into another, for example `25 % 5`, as we know `25` is a multiple of `5`.

## Strings

What strings entail we have already covered, but there is more to know about strings. We will cover some of that information here.

Every character in a string is usually what is known as a "Unicode character", and Python only ever sees this as the case for strings. What this means is Python cannot distinguish what is a word or a number for a string, it just works with what unicode characters are in the string and does not make sense of any patterns, the only thing it will do is ensure that the string is printed in the order requested (so if I wanted to print the work `"duck"`, it will always do this. It is also important to know that every unicode character has another way to write them, which is more accurate to the name "unicode". For example, let's say we want to print the letter `'B'`. We could just write:
```py
print('B')
```
*Or*, we could write the following to print it:
```py
print(u'\u0042')
```
The result is the same, an output of `B`. You may be asking what is necessarily the point of this, but this is actually a great tool for characters you might not usually see on a keyboard! For example, if you are using a QWERTY keyboard from the UK or US, you likely have not seen the "section sign" § on your keyboard. Instead of finding the symbol online, you can just use the code for the character:
```py
print(u'\u00A7')
```
produces the output `§`. It was also mentioned that the unicode characters being looked at are not recognised by Python as words or sentences. This means Python can easily work with finding a character within an index. An index is a way to identify the parts of the string, so for example if you have a word such as `duck`, an index can help show you what is at a certain position. Using the `duck` example, writing as an input `"duck"[2]` would return the letter `c`. Indices start counting at index 0, so `0` here is the letter `d` in the output.

## Boolean and Equality Operators

Booleans are either True or False, as was mentioned. You can also have equality operators deduce what exactly is true and what is false. For example:
```py
print(6 == 3)
```
outputs `False`. The same can be tested for the inequality signs:
```py
print(6 > 3)
print(6 != 3)
```
outputs `True` for both print functions. The equality operators are: `==` for testing equality, `>` for testing greater than, `>=` for testing greater than or equality, `<` for testing less than, `<=` for testing less than or equality and `!=` for testing inequality.

## Variables
In Python you are more likely to be using variables than using regular data types ("literals"). You can define variables by following the example:
```py
variable = value
```
The variable should be on the left or you will get an error. You can put anything on the right so long as it is valid without a variable, and you can also have variables interact with other variables:
```py
a = 22
b = 33
c = a + b
print(c)
```
will output `55`.

## Concatenation and String Methods
You can combine strings together into one larger string:
```py
firstname = "Joe"
lastname = "Bloggs"
full_name = firstname + " " + lastname
print(full_name)
```
outputs `Joe Bloggs`. You need to have the space here as Python does not recognise you want a space without it. Escape characters are usable when you need to add items such as quotes or apostrophes into a string. For example:
```py
print("The following quote is inside a quote: \" Hello, I am an O\'Neill Brother.\"")
```
outputs `The following quote is inside a quote: "Hello, I am an O'Neill Brother."`. 

String methods are ways to modify a string. For example, with the previous value `firstname`, we can input:
```py
print(firstname.upper())
```
to get the output `JOE`, all of it in capital letters. This is just one of many possible string methods you can do.

## Control Flow
`if` statements are able to indicate you should do sometime if the requirements are met. There is also `elif` which gives another requirement for when `if` is not met and finally `else` which is something you can make happen if none of the requirements in `if` (or also `elif` if included) are met.

## Lists and Dictionaries
Lists and Dictionaries are forms of Collections within Python. Lists are sometimes known as "Arrays" in other languages and simply hold a list of values in an order given by the user. Lists can also include other lists as the values. For example:
```py
example_list = [23, 44, 22, 10, 7, 22]
```
This is a valid list. Note that lists can include duplicate values and have values other than integers. They can have any value, including strings.

Dictionaries are similar, but they have the requirement of keys for every value in the dictionary. The user can then call a key to get the value:
```py
example_dict = {
    "key1":"value1"
    "key2":"value2"
}
```

## Loops (While, For)
Loops are ways to have a piece of code repeat until a certain condition is met, to save you duplicating code over and over again. For a For loop example:
```py
For i in "values":
    print(i)
```
outputs:
```
v
a
l
u
e
s
```
This loop continues going until `i` moves through all of the items in the string `"values"`.

While loops are organised differently:
```py
i = 0
while i < 6:
    print(i)
    i += 1
```
Here we have the value of i increment by 1 each time until the loop has happened for i = 5. Afer this, the while loop stops. The output is:
```
0
1
2
3
4
5
```

## Functions
Functions are inputs you can type such as the print function we have seen a lot of, but you can also define your own functions which you can then call:
```py
def test_func(argument1, argument2, etc.):
    sum = argument1 + argument2
    print(sum)

test_func(41, 4)
```
which for the example above outputs `45`. Keep in mind though, functions don't need arguments. You can have as many as you want or none at all, so long as the function itself is logically fine.
