# String Methods  

  Python has a number of built-in methods that you can use on strings to do simple transformations.

  You can see a comprehensive list via the link in the **References**.

  ## 1. What is a Method?

  A method is something you can call on an object that does something with that object. This will make more sense when we get to object-orientation later in the course.

For now, if we have a string we can call a method using the ``.`` notation and we will get back a new string.

For example, type the following into the console,

```python
"hello world".upper()
```
returns the new string:

```python
"HELLO WORLD"
```
Here we called the ``upper()`` method on the ``str`` object ``"hello world"`` and it gave us back the ``str`` ``"HELLO WORLD"``.

### 1.1 Be Careful

String methods return new strings, consider the following code:

```python
a = "hello world"    # (assign "hello world" to variable a)
a.upper()            # (call upper() on variable a)
print(a)             # (print a)
```
will output
```
hello world
```
This is because it returns a new string, it does NOT change the original string. So ``a`` is left as ``"hello world"``. 

We would either have to do the following to print out the upper case version,
```python
a = "hello world"    # (assign "hello world" to variable a)
print(a.upper())     # (print out the result of calling upper() on variable a)
```
or,
```python
a = "hello world"    # (assign "hello world" to variable a)
b = a.upper()        # (call upper() on variable a and assign result to variable b)
print(b)             # (print b)
```

## 1.2 Familiarise Yourself

Take a look at the following link - [W3Schools - Python String Methods](https://www.w3schools.com/python/python_ref_string.asp) and try some of these out. You will need some of them for the **TASK**.

***
# === TASK ===

Copy the following into **main.py**.
```python
sentence = input("Please enter a sentence:\n")

print(sentence)
```

Amend the code so that the inputted sentence is then printed out as
1. upper case
2. lower case
3. first character of each word is upper case 

For example,

```
Please enter a sentence:
The quick brown fox jumps over the lazy dog
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
the quick brown fox jumps over the lazy dog
The Quick Brown Fox Jumps Over The Lazy Dog
```
***Note that to pass the tests you must have exactly the output above, apart from the numbers which will differ depending on what the user inputs.***
***


# References 
  [W3Schools - Python String Methods](https://www.w3schools.com/python/python_ref_string.asp)
  