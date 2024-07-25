# Strings  

This lesson introduces you to the basics of strings in Python. 

Python has a built-in datatype ``str`` known as a string, you can think of this as a piece of text. 


## 1. Basic Printing of Strings


Strings can be printed to the console using the python ```print()``` function (we will explore functions in detail later in the course).

For example:
```python
print("hello world!")
```

Prints ```hello world!``` to the console. 

Whatever is contained between the brackets will be printed out to the console using double quotes ```""```.

## 2. Quotes

In Python strings can be enclosed in either single quotes ```'...'``` or double quotes ```"..."```

For example:
  ```python
print('hello world!')
```

Also prints ```hello world!``` to the console as per section 1. 


***NOTE: Although we can use both, please stick to double quotes as most languages represent strings with double quotes!***

## 3. Escape Characters

```
My first program was "Hello World!" in Python
```

Try the following in the **console**.

```python
print("My first program was "Hello World!" in Python")
```

You will see a ```SyntaxError: invalid syntax```, this is the Python interpreter telling you that it does not understand the code you have entered. If you look closely you will see that it is pointing to the ```H```, the character after the second ```""```. This is because it is illegal to put a double quote character ```"``` within a string.

To fix this we need to use an **escape character**, in Python, this is the ```\``` (backslash) followed by a particular character. 

Amend the previous line of code to include backslashes for the quotes in the string.

```python
print("My first program was \"Hello World!\" in Python")
```

If you run this you will now get the desired output ```My first program was "Hello World!" in Python```.

There are a number of special escape characters in Python, you can look them up. We will just look at the following:

| Name | Escape Character |
| --- | --- |
| tab | `\t` |
| new line | `\n`|
| backslash | `\\` |
| single quotation mark | `\'` (You only need to use this when the string in enclosed is single quotation marks.) |
| double quotation mark | `\"` (You only need to use this when the string in enclosed is double quotation marks.) |

For example,

```python
print("My first program was \"Hello World!\" in Python\n\nPython is cool!")
```

prints out :

```
My first program was "Hello World!" in Python
  
Python is cool!
```

## 4. Multiline Strings

Multiline strings let us write multiple lines in a string without escape characters or multiple print statements. In Python, they start with `'''` or `"""` and end the same way.


```python
numbers = '''3
5
6
7
'''  
print(numbers)
```

The above will print out the following to the console.

```
3
5
6
7
```

If you have an escape character in your multiline string and you want this to appear in the console you should escape it with another ```\```. 

For example,

```python
print('''This is a multiline string.

The tab escape character in python is \t.
''')
```
will result in the output:

```
This is a multiline string.

print('''This is a multiline string.

The tab escape character in python is   .
''')
```
i.e. it will put a tab into the output. To get ```\t``` to show up you need to escape it with another ```\``` as follows:

```python
print('''This is a multiline string.

The tab escape character in python is \\t.
''')
```

***NOTE: This is the same in a normal string. To output an escape character as text you should escape it!***

## 5. Concatenating Strings
  
To concatenate, or combine, strings you can use the ```+``` operator.

For example, 

```python
str1 = "Hello"
str2 = "World!"

print(str1 + str2)
```
results in the output:

```
HelloWorld!
```

To get the standard ```Hello World!``` we could do the following.

```python
str1 = "Hello"
str2 = "World!"

print(str1 + " " + str2)
```

Note that you can also just concatenate strings within the print function:

```python
print("Hello" + " " + "World")
```

## 6. Formatting Strings

We can also combine strings using the ```format()``` method.

The ``format()`` method takes the passed arguments and puts them in the string where the placeholders ``{}`` are:

For example,
```python
str1 = "string 1"
str2 = "string 2"
print("Hello {} and hello {}.".format(str1, str2))
```

results in the output:

```
Hello string 1 and hello string 2.
```

We can also achieve this using index numbers starting at ```{0}```

```python
str1 = "string 1"
str2 = "string 2"
print("Hello {0} and hello {1}.".format(str1, str2))
```

This is especially useful if you wish to repeat strings stored in variables.

For example, 

```python
str1 = "string 1"
str2 = "string 2"
print("Hello {0} and hello {1}.\nBye {0} and bye {1}.".format(str1, str2))
```
results in the output:

```
Hello string 1 and hello string 2.
Bye string 1 and bye string 2.
```

## 7. f-Strings

Since Python 3.6 you can use f-Strings (formatted string literals), we will use these throughout the course, but you should understand how to use the others in case someone else has written code using them.

We can achieve the previous output by doing the following:
```python
str1 = "string 1"
str2 = "string 2"
print(f"Hello {str1} and hello {st2}.\nBye {str1} and bye {str2}.")
```
which again results in the output:

```
Hello string 1 and hello string 2.
Bye string 1 and bye string 2.
```

Note that in front of the string we put an ``f``. This tells python that anything in curly braces should be evaluated. So in the example above, the values of ``str1`` and ``str2`` are substituted into the string.

***
# === TASK ===
1. Print ```Programming in Python``` to the console. &nbsp;

2. Print ```Programming in Python with single quotes``` to the console using single quotes ```''```.

3. Print the following to the console.
```
I know how to put "quotes" into a string.
  
And put in new lines!
```
4. Using a multiline string print
```
I am using a multiline string to:
- print multiple lines 
- without the use of the escape character \n
```
to the console.

5. Create the following strings and store them in the variables ```str1``` and ```str2```

```python
str1 = "string 1"
str2 = "string 2"
```
Print ```Hi, I am string 1 and I am string 2!``` to the console using string concatenation.

6. Print ```string 1 is before string 2 and string 2 is after string 1``` to the console using f-strings.

The entire output of the program should be as follows:
```
Programming in Python
Programming in Python with single quotes
I know how to put "quotes" into a string.

And put in new lines!
I am using a multiline string to:
- print multiple lines
- without the use of the escape character \n
Hi, I am string 1 and I am string 2!
string 1 is before string 2 and string 2 is after string 1
```
***
