# Learn Python3 The Hard Way

https://learnpythonthehardway.org/python3/

## Other links

* https://www.josharcher.uk/categories/lpthw/

## Exercise 1 (Print Strings)

You can use " and ' for strings
And nest them, e.g.
* "I'll see this printed 'correctly'."
* 'Yes, and "this" as well.'

## Exercise 2 (Comments)

Why do I have to read code backward?
* It's a trick to make your brain not attach meaning to each part of the code, and doing that makes you process each piece exactly. This catches errors and is a handy error-checking technique.
* Did you find more mistakes? Fix them.

## Exercise 3 (Numbers & Math)

How does % work?

* Modulo is what's left over after a divison, where you are just operating on whole numbers. 
* Take example: 100.0 - 25 * 3 % 4
* This equates to: 100 - ((25 * 3) modulo 4)
* 75 modulo 4 = 3
* 4 fits 18 times in 75, leaving 3 over

What is the order of operations?
* In the United States we use an acronym called PEMDAS which stands for Parentheses Exponents Multiplication Division Addition Subtraction. That's the order Python follows as well. The mistake people make with PEMDAS is to think this is a strict order, as in "Do P, then E, then M, then D, then A, then S." The actual order is you do the multiplication and division (M&D) in one step, from left to right, then you do the addition and subtraction in one step from left to right. So, you could rewrite PEMDAS as PE(M&D)(A&S).
* In German: Punkt vor Strich, von links nach rechts.

## Exercise 4 (Variables)

Tricks taught so far:
* write comments to explain to yourself in english what it should do
* read your .py file backwards
* read your .py file out loud, saying even the characters

Take note:
* The = (single-equal) assigns the value on the right to a variable on the left. The == (double-equal) tests whether two things have the same value.
* Add space around operators like this so that it's easier to read.

Printing using comma separated values will add spaces around the values:

```
>>> print("There are", cars, "cars available.")
>>> There are 100 cars available. 
```

If you don't want to have the extra spaces, you can use string concatenation:

```
>>> print("There are " + str(cars) + " cars available.")
>>> There are 100 cars available. 
```

For more information, see: https://stackoverflow.com/questions/28669459/how-to-print-variables-without-spaces-between-values#

## Exercise 5 (more variables)

Syntax Error when run with < python3.6

https://stackoverflow.com/questions/2429511/why-do-people-write-the-usr-bin-env-python-shebang-on-the-first-line-of-a-pyt/2429517#2429517

Added shebang, made executable, run directly:

```
./myscript.py
```

* variables need to start with a character - "1" is not a valid variable name


