# String Indexing and Slicing  

A string is a sequence of characters representing Unicode characters.

For example the string ``"Helloworld"`` can be thought of like this.

![Hello World String](assets/helloworld_string.png)

Unlike many programming languages, Python does not have a character type and a character is just a string (``str``) of length ``1``.

## 1. String Indexing

You can access elements of the string using square brackets ``[]`` and the index of the position you wish to access. 

Note indexing starts at ``0``. So the first character has an index of ``0``.

![String indexing](assets/helloworld_string_indexing.png)

For example,

```python
str1 = "String Indexing"

print(str1[0]) # prints the first character "S"
print(str1[4]) # prints the 5th character "n"
```

### 1.1 IndexError

If you try the following:

```python
str1 = "String Indexing"

print(str1[15]) # IndexError
```

You will get an exception as there is no 16th character (index 15 tries to access the 16th character).

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

### 1.2 Negative Indexing

We can also access the characters of the string from the end.

![String indexing](assets/helloworld_string_negative_indexing.png)

For example,
```python
str1 = "String Indexing"

print(str1[-1]) # prints the last character "g"
print(str1[-2]) # prints the second to last character "n"
```

### 1.3 Length of a String

The ``len()`` function will return the length of the string.

```python
str1 = "String Indexing"

print(len("String Indexing")) # prints 15
```

## 2. String Slicing

We can easily get substrings from a given string by using string slicing.

For example, we can get ``"Index"`` from the string ``"String Indexing"``.

The following gets the characters from position 7 to position 11 (12 not included)
```python
str1 = "String Indexing"

print(str1[7:12]) # prints Index
```
**Basically you specify the start index and the end index (not included), separated by a colon, to return a part of the string.**

### 2.1 Start to a Given Position

You can get all characters from the start to a given position by:

```python
str1 = "String Indexing"

print(str1[0:6]) # prints String
## OR
print(str1[:6]) # prints String
```

The second way is very common and is shorthand for the start index ``0``.

### 2.2 A Given Position to the End

You can get all characters from a given position to the end of the string using.

```python
str1 = "String Indexing"

print(str1[4:15]) # prints ng Indexing
## OR
print(str1[4:])   # prints ng Indexing
```
The second way is quite common and it means we don't need to know the length of the string!

Otherwise, in general you would need to do the following

```python
str1 = "String Indexing"

print(str1[4:len(str1)]) # same as str1[4:15] or str1[4:]
```

### 2.3 Negative Slicing

You can also slice using negative indexing.

```python
str1 = "String Indexing"

print(str1[-3:]) # prints out the last 3 characters - "ing"
print(str1[-4:-2]) # prints out character 11 and 12. Same as str1[11:13]
```

***
# === TASK===
Copy the following into **main.py**.
```python
# DO NOT EDIT THESE TWO LINES
firstname = input("Please enter a first name: \n")  # leave this alone!
surname = input("Please enter a surname: \n")  # leave this alone!

# -------------------------------------------------------

# Edit the following line so that it prints out the first character of the first name
print(f"The first character of the first name is {firstname}")

# Edit the following line so that it prints out the last character of the surname (negative indexing)
print(f"The last character of the surname is {surname}")

# Edit the following line so that it prints the initials of the person. e.g. Mary Smith would result in M.S
print(f"The person's initials are {firstname}.{surname}")

# Edit the following line so that it prints the first 3 characters of the first name. For example Mary would print out Mar
print(f"The first 3 characters of the first name are {firstname}")

# Edit the following line so that it prints the last 4 characters of the surname
print(f"The last 4 characters of the surname are {surname}")
```


1. Edit the following line so that it prints out the first character of the first name
```python
print(f"The first character of the first name is {firstname}")
```
2. Edit the following line so that it prints out the last character of the surname (negative indexing)
```python
print(f"The last character of the surname is {surname}")
```
3. Edit the following line so that it prints the initials of the person. e.g. Mary Smith would result in M.S
```python
print(f"The person's initials are {firstname}.{surname}")
```
4. Edit the following line so that it prints the first 3 characters of the first name. For example, Mary would print out Mar
```python
print(f"The first 3 characters of the first name are {firstname}")
```
5. Edit the following line so that it prints the last 4 characters of the surname (note we assume for simplicity that the surname contains at least 4 characters, what happens if it is less than 4?)
```python
print(f"The last 4 characters of the surname are {surname}")
```
An example of the correct program for the input ``Mary Smith`` is given below.
```
Please enter a first name:
Mary 
Please enter a surname:
Smith
The first character of the first name is M
The last character of the surname is h
The person's initials are M.S
The first 3 characters of the first name are Mar
The last 4 characters of the surname are mith
```
***