# Python: Where to start
In this guide, we are going to cover the fundamentals of Python as a programming language.

To be sure that all that you can find what you want, here is a list of the topics that will be covered. Simply go to what area of the document you would like to visit.

- Introduction/The Starting Point
- Commenting Code
- Data Types
- Numbers and Mathematical Operators
- Strings
- Boolean and Equality Operators
- Variables
- Concatenation and String Methods
- Control Flow
- Collections, Lists and Dictionaries
- Loops (While, For)
- Functions

Just remember: Python can be a puzzle. Do not panic if you are stuck, just logically think about all of the information you know!


## Introduction/The Starting Point

We will assume that you have a code editor on hand when beginning this tutorial, but if you do not then you *must* get one as soon as possible. Standard text editors, while they do accept python code, do not allow you to have extra support for problems that may arise, such as trying to remember where a bracket would need to go (more on that later).

For now, ensure that you have one and, to ensure that you can run the code you create, an ability to run any code you write. PyCharm, recommended by many, has this capability built in, but there are plenty of alternatives you can use.

Now that you have the ability to run code, let's do just that. All programming languages should have you start with "Hello World" to understand the syntax and workings of the language. Try running the following in your python .py file in use:

```
print("Hello, world!")
```
If your environment if successfully set-up, you should be able to run this and receive the output "Hello, world!" in the results terminal (this should appear on your screen after running the code if it wasn't already present. If it hasn't appeared, consult the help guide of the software you are using, you could either not have it set-up correctly or there might be simply a minimised terminal somewhere.

Assuming there are no issues, congratulations! You have just written your first piece of code in Python and got it to run successfully. Now, there is plenty more to learn, as we will see, but this first step being done right is an excellent start.

## Commenting Code

Before we progress into the actual main information of Python, a quick note. When it comes to coding, it is a much needed formality to be able to comment your code. What this means is giving a sort of "commentary" on what your code is doing throughout the process. Not only does this help explain things to someone who may be reading your code, but it may also help explain it to yourself! Everyone, even the best programmers, forget things, so imagine how frustrating it would have to be to revisit an old piece of work in Python (or any other programming language for that matter) that you have made, only to realise you have not explained how it works. You would have to revisit all of it and relearn it, while you could just save yourself the hassle and comment where needed!

Here is an example of commenting within a piece of code:
```
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
- Boolean: It may sound scary, but don't worry. Boolean is simply put one of two statements, "True" or "False". In code, this is written as `True` or `False` (it may be helpful to know that you can in some cases use `0` for Boolean values to indicate false instead of the word and also `1` (or simply not `0`) to indicate a Boolean to be true. This isn't to say that 0 is a Boolean rather than an integer, but rather it is just an equivalent to it for if a comparison is necessary.

## Numbers and Mathematical Operators

By now you should know about the `print()` function and data types. With your knowledge of these, let's test printing values other than strings.
```
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

```
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
```
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
You should hopefully be familiar with + as the operator for addition, - as the operator for subtraction, * as the operator for multiplication and / as the operator for division. You are excused however if you are not familiar with the last operator seen, %. This is the modulo operator, which returns the remaining amount once the division of the first number over the second number has been completed. For example, with `23 % 7`, we have 7, 14, 21...and then we cannot get any further without going beyond the goal of 23, so the modulo gives the result for `23 - 21`, so `2`. This value the modulo gives will of course therefore be `0` if a number divides perfectly into another, for example `25 % 5`, as we know `25` is a multiple of `5`.
