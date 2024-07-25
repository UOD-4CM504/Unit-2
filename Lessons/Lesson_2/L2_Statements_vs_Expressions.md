# Statements vs Expressions

So far you have already seen examples of both **statements** and **expressions** and your Python programs will be made up of both of these.

We will give a basic definition of the two, however, the real story is much more complicated. 
  
## 1. Statements

**Statements** instruct Python to do something, that is the Python interpreter can execute the **statement**. To date, you have seen two types of **statements**: print and assignment.

For example,

```python
print("Hello World!")
```
is a **statement** that instructs python to print the string ``"Hello World!"`` and,


```python
int1 = 1
```
is a **statement** that instructs Python to assign ``1`` to the variable ``int1``.

## 2. Expressions

**Expressions** differ from **statements** in that they evaluate to an object. They are a combination of objects and operators.

For example,

```python
3 + 5 
```
combines the integers (objects of type ``int``) ``3`` and ``5`` with the operator ``+`` and evaluates to the integer ``8``. 

This example,

```python
True and False
```
combines the boolean (objects of type ``bool``) ``True`` and ``False`` with the logical operator ``and`` and evaluates to the boolean ``False``.

## 3. Combining Statements and Expressions

Most of your code will tend to be a statement made up of expressions.

For example, you can assign the result of an expression to a variable. Consider the following statement (assignment)

```python
a = 3 + 5 
```

Here ``3 + 5`` is an expression and the result, ``8``, is assigned to the variable ``a``. The whole line is a statement that contains an expression.

***
# === TASK ===
A nice simple one.
 
Print ```Statements instruct Python to do something```
 
Print ```Expressions combine objects and operators and evaluate to an object```

Print ```Statements can include expressions```
***