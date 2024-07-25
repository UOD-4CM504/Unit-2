# Casting  

  It is very common that you will need to convert one data type to another.

  Type the following into the console:

  ```python
  print("The meaning of life is " + 42)
  ```

  You will the following ``TypeError``:

  ``TypeError: can only concatenate str (not "int") to str``

  This is because you are trying to add a ``str`` and an ``int``. Python does not know how to do this. To correct this you need to do something called casting.

  The following code casts (converts) the ``int`` to a ``str`` using the constructor function ``str()``:

  ```python
  print("The meaning of life is " + str(42))
  ```

  If you try this you will see that it works. 
  
  Type ``str(42)`` into the console on its own and you will see that it returns the ``str`` ``'42'`` (note it uses single quotes, but that is the same as double quotes in Python!).

Note that we could have done the following:

```python
print(f"The meaning of life is {42}")
```
This is because the python f-string knows how to convert the number 42 to play nicely with the string. Try it in the console.

## 1. How to Cast 

Casting in python is therefore done using constructor functions:

| Function | Description |
| --- | --- |
| ``int()`` | Constructs an integer number from an integer, a float (by removing all decimals), or a string (providing the string represents a whole number) |
| ``float()`` | Constructs a float number from an integer, a float, or a string (providing the string represents a float or an integer) |
| ``str()`` | Constructs a string from a wide variety of data types, including strings, integers, floats, and booleans |
| ``bool()`` | Constructs a boolean from a wide variety of data types, including strings, integers, floats, and booleans |

### 1.1 Examples

Try these in the console:

```python
int(1)           # Creates an int with value 1
int("2")         # Creates an int with value 2
int(4.3)         # Creates an int with value 4
int(True)        # Creates an int with value 1
int(False)       # Creates an int with value 0
```

```python
float(1)         # Creates a float with value 1.0
float("2")       # Creates a float with value 2.0
float("3.142")   # Creates a float with value 3.142
float(4.3)       # Creates a float with value 4.3
float(True)      # Creates a float with value 1.0
float(False)     # Creates a float with value 0.0
```

```python
str(1)           # Creates a str with value '1'
str("3.142")     # Creates a str with value '3.142'
str(4.3)         # Creates a str with value '4.3'
str(True)        # Creates a str with value 'True'
str(False)       # Creates a str with value 'False'
```

``bool()`` can throw up some unexpected results unless you understand what it is doing.

You might think that ``bool("0")`` would result in ``False``, it doesn't! 

Python treats everything as ``True`` other than ``False``, ``0``, an empty string ``""`` and some other things we have yet to encounter, empty lists, dictionaries, tuples, and the ``None`` keyword which represents no value at all (more on that later).
```python
bool(1)          # Creates a bool with value True
bool("3.142")    # Creates a bool with value True
bool(4.3)        # Creates a bool with value True
bool("0")        # Creates a bool with value True
bool(True)       # Creates a bool with value True
bool(False)      # Creates a bool with value False
bool(0)          # Creates a bool with value False
bool("")         # Creates a bool with value False
bool([])         # Creates a bool with value False
bool({})         # Creates a bool with value False
bool(())         # Creates a bool with value False
bool(None)       # Creates a bool with value False
```

***
# === TASK ===
Write a program in **main.py** so that it outputs the following to the console for a given X and Y.
``` The result of multiplying X by Y is X*Y ```

For example, for 2.1 and 3:

```
Please enter a number:
2.1
Please enter another number:
3
The result of multiplying 2.1 by 3.0 is 6.3
```

For example, for 5.2 and 3.4:

```
Please enter a number:
5.2
Please enter another number:
3.4
The result of multiplying 5.2 by 3.4 is 17.68
```
***Note that to pass the tests you must have exactly the output above, apart from the numbers which will differ depending on what the user inputs.***
***

## References

[W3Schools - Python Casting](https://www.w3schools.com/python/python_casting.asp)