# Variables and Assignment  

**Variables** are one of the most important things in programming languages. They allow us to assign a name to an object so we can store it for use later on in our program. 

## 1. Assignment

We assign an object to a **variable** using the assignment operator ```=```. For example,

```python
pi = 3.14
```
assigns ``3.14`` to the **variable** named ```pi```.

We can then use the variable in our programs. Consider the following program,

```python
pi = 3.14
radius = 6
circumference = 2 * pi * radius
print(circumference)
```

this will print the value of the circumference of the circle with radius 6. 

The point is that the line ```circumference = 2 * pi * radius``` now used the variables ```pi``` and ```radius```  to calculate the value of the ``circumference``.

This code is in **main.py** so you can run it if you wish.

The following image illustrates the binding of the variables to the objects in memory. Note it isn't really how Python works internally, but it is good enough as a mental picture.

![Variable Assignment](assets/variable_assignment.png "Variable Assignment")

## 2. Reassignment

Python lets you reassign a variable to another object. 

The following code,

```python
pi = 3.14
radius = 6
circumference = 2 * pi * radius
print(f"The circle with radius = {radius} has circumference = {circumference}")

radius = 0

print(f"The circle with radius = {radius} has circumference = {circumference}")
```
will output,

```
The circle with radius = 6 has circumference = 37.68
The circle with radius = 0 has circumference = 37.68
```

because we reassigned the **variable** ```radius``` to the value ```0```, but we did not recalculate the ``circumference``.

The following depicts the reassignment of the variable ``radius``.
![Variable Reassignment](assets/variable_reassignment.png "Variable Assignment")
Image reproduced from Chapter 2: Introduction to Computation and Programming Using Python.

## 3. Objects in Memory

Python stores objects in memory and when you assign a variable it binds that variable to the location of the object in memory. 

You can find the unique id of an object by using the ```id()``` function. This refers to the object's memory address and will be different each time you run the program. 

Input the following two lines into the console, remember to press enter after each line:

```python
pi = 3.14
```

```python
id(pi)
```
For now the ``id()`` function is a bit of a novelty. We will see later on that it can prove essential in debugging programs when we are editing mutable (changeable) types like lists. 

***Note that two objects can have the same id if one object has been removed from memory (Python automatically cleans up objects that are no longer used). Essentially the unique id is being re-used.***

***
# === TASK ===
This should be relatively simple, consider it a freebie.

```python
pi = 3.14
radius = 6
circumference = 2 * pi * radius
print(f"The circle with radius = {radius} has circumference = {circumference}")

# Reassign radius to the value 15
# Reassign circumference to the circumference of the circule with radius 15
# In addition to the existing print statement, print out the new circumference.

```
 
Copy the above code into **main.py** to do the following:

* Reassign ```radius``` to the value ```15```
* Reassign ```circumference``` to the circumference of the circule with radius ``15``
* In addition to the existing ```print``` statement, print out the new circumference.

The output of the program should be:
```
The circle with radius = 6 has circumference = 37.68
The circle with radius = 15 has circumference = 94.2
```
***