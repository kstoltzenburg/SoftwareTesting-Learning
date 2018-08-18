# Learn Python3 The Hard Way

https://learnpythonthehardway.org/python3/

## Exercise 1 (Print Strings)

You can use " and ' for strings
And nest them, e.g.
* "I'll see this printed 'correctly'."
* 'Yes, and "this" as well.'

## Exercise 2 (Comments)

Why do I have to read code backward?
* It's a trick to make your brain not attach meaning to each part of the code, and doing that makes you process each piece exactly. This catches errors and is a handy error-checking technique.
* Did you find more mistakes? Fix them.

## Exercise 3 (Numbers)

How does % work?

* Modulo is what's left over after a divison, where you are just operating on whole numbers. 
* Take example: 100.0 - 25 * 3 % 4
* This equates to: 100 - ((25 * 3) modulo 4)
* 75 modulo 4 = 3
* 4 fits 18 times in 75, leaving 3 over

What is the order of operations?
* In the United States we use an acronym called PEMDAS which stands for Parentheses Exponents Multiplication Division Addition Subtraction. That's the order Python follows as well. The mistake people make with PEMDAS is to think this is a strict order, as in "Do P, then E, then M, then D, then A, then S." The actual order is you do the multiplication and division (M&D) in one step, from left to right, then you do the addition and subtraction in one step from left to right. So, you could rewrite PEMDAS as PE(M&D)(A&S).
* In German: Punkt vor Strich, von links nach rechts.

