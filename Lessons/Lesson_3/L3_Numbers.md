# Numbers  

 Python has three numeric types:

 * ```int```
 * ```float```
 * ```complex```

Unless you are doing something specifically mathematical you will only use ```int``` and ```float```. So we will cover just these in this lesson. 

## 1. ints and floats 

The following table provides a summary of ``int`` and ``float``.

| Data Type | Description |
| --- | --- |
| ``int`` | An integer. There is no upper or lower limit to how high or low it can be (Python 3). |
| ```float``` | A decimal number. A double-precision floating-point number, equivalent to double in many other programming languages. |

### 1.1 int 

An ``int`` (integer) is simply a whole number such as ``5`` or ``-100``. If you assign a whole number to a variable, python will automatically know that the type of object is an ``int``. 

Type the following two lines in the console:

```python
a = 10
type(a)
```

You will see that the output confirms that ``a`` is of type ``int``.

### 1.2 float 

An ``float`` (floating point number) is a number containing one or more decimals, such as ``5.3`` or ``-100.43``. If you assign a decimal number to a variable, python will automatically know that the type of object is an ``float``. 

Type the following two lines in the console:

```python
a = 10.6
type(a)
```

You will see that the output confirms that ``a`` is of type ``float``.

You can find out the minimum and maximum float using

```python
import sys
print(sys.float_info.min)
print(sys.float_info.max)
```

On the Repl.it systems it is 
``-2.2250738585072014e+308`` to ``1.7976931348623157e+308``. Which is approximately ``-2.23*(10**308)`` to ``1.80*(10**308)``

That is astronomically big!

### 1.3 Dynamic Typing

You can combine an ``int`` and a ``float``. Python will internally understand to convert the ``int`` to a ``float`` so that you can combine two floats.

For example, type the following into the console,

```python
a = 1 + 3.3
print(a)
type(a)
```
the first line is adding an ``int`` and a ``float`` which results in an object of type ``float`` with the value ``4.3``.

## 2. Arithmetic Operators

Number objects can be combined with the following arithmetic operators. 

| Operator | Name | Example
| --- | --- | --- |
| ``+`` | Addition | ```x + y``` |
| ``-`` | Subtraction | ```x - y``` |
| ``*`` | Multiplication | ```x * y``` |
| ``/`` | Division | ```x / y``` |
| ``%`` | Modulus | ```x % y``` |
| ``**`` | Exponentiation | ```x ** y``` |
| ``//`` | Floor Division | ```x // y``` |

All of ``+``, ``-``, ``*`` and ``/`` will be familiar to you. However, ``%``, ``**`` and ``//`` may not be.

#### 2.0.1 Modulus (``%``)
The modulus operator is very useful for testing if a whole number is divisible by another whole number. It is an implementation of modulo (clock) arithmetic in mathematics. 


If a number is divisible by another the output of ``x % y`` will be ``0`` (``x`` and ``y`` can be positive or negative).
```python
10 % 3 # output is 1 (not divisible)
10 % 2 # output is 0 (divisible)
14 % 4 # output is 2 (not divisible)
14 % 7 # output is 0 (divisible)
```

You will see this in computational mathematics, for more info look at 
[Modulus Operator - Real Python](https://realpython.com/python-modulo-operator/)

It can also be used to find the remainder, but be careful, this doesn't work in all circumstances. I would always use ``math.remainder()``.

```python
import math # imports extra maths stuff
print(math.remainder(10, 3)) # remainder of 10/3 is 1
print(10 % 3) # output is 1. (% WORKS)

print(math.remainder(-10, 3)) # remainder of 10/3 is 1
print(-10 % 3) # output is 2. (% DOES NOT WORK)

print(math.remainder(10, -3)) # remainder of 10/3 is -1
print(10 % -3) # output is -2. (% DOES NOT WORK)

print(math.remainder(-10, -3)) # remainder of 10/3 is -1
print(-10 % -3) # output is -1. (% WORKS)
```

So it works when both numbers are positive or both numbers are negative. 

My advice is don't use it for the remainder. 

####  2.0.2 Exponentiation (``**``)

The exponentiation operator ``**`` takes the number ``x`` (called the base) to the power of ``y`` (called the exponent).

```python
2**3 # Evaluates to 8 (i.e. 2*2*2)
2**4 # Evaluates to 16 (i.e. 2*2*2*2)
5**2 # Evaluates to 25 (i.e. 5*5)
5**3 # Evaluates to 125 (i.e. 5*5*5)
```

####  2.0.3 Floor Division (``//``)

The floor division operator ``//`` takes the number ``x/y`` and rounds it down.

For example,

``10/4 `` is ``2.5`` rounded down is ``2``. 
So,
```python
10//4 # Evaluates to 2
```

``-10/4 `` is ``-2.5`` rounded down is ``-3``. 
So,

```python
-10//4 #Evaluates to -3
``` 




### 2.1 Order of Operations

When using arithmetic operators you need to be aware of the order in which Python evaluates an operator. This is known as the operator precedence.

For example,

```python
3 + 5 * 2
```

is ``16`` right? If you enter this into the console you will get ``13``. Well done if you spotted this.

This is because the multiplication ``*`` operator has higher precedence than the addition ``+`` operator. Python is doing the following

```
# This is not code, we are manually evaluating to see how Python works with this expression

3 + 5 * 2     # (Evaluate 5 * 2)
3 + 10        # (Evaluate 3 + 10)
13            # (Final Object)
```

If you want to force the ``3 + 5`` to be evaluated first, then you need to use parentheses.

```python
(3 + 5) * 2
```
This now evaluates to ``16``. Try it in the console.

The following table gives the arithmetic operator precedence. Higher entries have higher precedence.

| Operator | Name |
| --- | --- |
| ``()`` | Parentheses | 
| ``**`` | Exponentiation | 
| ``*``, ``/``, ``%``, ``//`` | Multiplication, Division, Modulus, Floor Division | 
| ``+``, ``-`` | Addition, Subtraction | 

### 2.2 Left-to-right Evaluation

You will notice from the table that some operators have the same precedence as each.

What happens then with the following:

```python
5 - 2 + 1
```

If you try this in the console you will get the answer ``4``. However, this could have been read as either ``3 + 1`` or ``5 - 3`` depending on whether you evaluated the ``-`` or ``+`` first.

Python follows the left-to-right convention. That is, if two operators are of the same precedence, then Python will evaluate the leftmost first. Hence:

```
# This is not code, we are manually evaluating to see how Python works with this expression

5 - 2 + 1     # (Evaluate 5 - 2)
3 + 1         # (Evaluate 3 + 1)
4             # (Final Object)
```

## 3. Comparison Operators

You can also compare two numbers and they will result in a ``bool`` object. Either ``True`` or ``False``.

| Operator | Name | Example |
| --- | --- | --- | 
| ``==`` | Equal |	``x == y`` |
| ``!=`` | Not equal | ``x != y`` |
| ``>`` |	Greater than | ``x > y`` |
| ``<`` | Less than | ``x < y`` |
| ``>=`` | Greater than or equal to | ``x >= y`` |
| ``<=`` | Less than or equal to | ``x <= y`` |

For example, the following expressions evaluate to:

| Expression | Result | 
| --- | --- | 
| ``3 < 5`` | ``True`` |
| ``3 > 3`` | ``False`` |
| ``3 >= 3`` | ``True`` |
| ``3 == 5`` | ``False`` |
| ``3 != 5`` | ``True`` |

### 3.1 Order of Precedence

All the comparison operators given above have lower precedence than the arithmetic operators.

| Operator | Name |
| --- | --- |
| ``()`` | Parentheses | 
| ``**`` | Exponentiation | 
| ``*``, ``/``, ``%``, ``//`` | Multiplication, Division, Modulus, Floor Division | 
| ``+``, ``-`` | Addition, Subtraction |
| ``==``, ``!=``, ``<``, ``>``, ``<=``, ``>=`` | Comparison Operators |

Therefore something like the following expression,

```python
3 + 5 == 3 * 5
``` 

is evaluated as follows:

```python
# This is not code, we are manually evaluating to see how Python works with this expression
3 + 5 == 3 * 5   # Evaluate 3 + 5
8 == 3 * 5       # Evaluate 3 * 5
8 == 15          # Evaluate 8 == 15
False
``` 


***Note: I would always want to convey my intention and not rely on the order of precedence, it is easy to forget. So I would rewrite the above as:***

```python
(3 + 5) == (3 * 5)
``` 

This is identical, but it tells the reader more explicitly that the stuff in the parentheses is evaluated first.

***
# === TASK ===
Copy the following code into **main.py**.

```python
# DO NOT TOUCH THE FOLLOWING LINES 4, 5 and 6
# THESE ARE USED FOR THE TESTS. 

a = int(input()) # leave this line alone
b = int(input()) # leave this line alone
c = int(input()) # leave this line alone

# TASK 1. 
# print out the type of 10.3 + 5

# TASK 2.
# print(a + b * c) # Correct this so that the ``+`` is evaluated first
# print(a**b+c)    # Correct this so that the exponent is b+c

# TASK 3. 
# print the output of a < b

# TASK 4. 
# print the output of (a < b) == (a <= b)
```

This reads in three whole numbers and stores them in variables ``a``, ``b`` and ``c``.

1. Print the type of ``10.3 + 5``

2. Fix the following two lines in **main.py**

```
print(a + b * c) # Correct this so that the ``+`` is evaluated first
print(a**b+c)    # Correct this so that the exponent is b+c
```

3. Print the output of ``a < b``

4. Print the output of ``(a < b) == (a <= b)``
***


# References

[W3schools Python Operators](https://www.w3schools.com/python/python_operators.asp)

[Precedence and Associativity of Operators in Python](https://www.programiz.com/python-programming/precedence-associativity)