Python
======

Basic notes on the python programming language. 


## Characteristics

* Python is dynamically typed - type and value of a variable are initialized on assignment, no pre-declaration necessary.
* Python uses pure indentation to identify code blocks

## Basics

### Shebang

https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

```
#!/usr/bin/env python3              # for python 3.x
#!/usr/bin/env python2              # for python 2.x
#!/usr/bin/env python               # rare, if compatible with both
```

### Data Types

#### print String vs. Object

```
>> myVariable = 'Hello World!' 
>> print myVariable
Hello World! 
```

... gives you the string representation of the object using str()

```
>> myVariable
'Hello World!'
```

... gives you the object, '' indicate it's a string, using repr()

* %s substitute a string
* %d substitute an integer
* %f substitutes a float

#### Boolean
Boolean are a special case of an Integer. Represented by Constants True and False, if you put it in a numerical context, e.g. an addition of numbers, True = 1 and False = 0. 

#### Strings
* a sequence of characters inside quotation marks.
* concatenated with +
* repetition with *

```
>> myString = 'Hello World!' 
```

* a subset can be extracted with [], e.g. myString[0] is the first character H
* ... and sliced with [ : ], myString[2:4] is ll
* .... from beginning - myString[:4], is: Hell
* .... and end - myString[2:], is: llo World! 
* '-' * 4 is ----
etc.
 
#### List, Tuples
* generic array
* List are in []
* Tuples are in (), and cannot be updated (~ read only lists)
* access subsets as for Strings, using [] position and [ ; ] for slice

#### Dictionaries
* are like hashes in perl
* key value pairs
* dicts are in {}

```
>>> aDict = {'host' ; 'earth'}
>>> aDict['port'] = 80            # add key value pair
>>> aDict
{'host' : 'earth', 'port' : 80 }
>>> aDict.keys()                  # show the keys
>>> aDict.['host']                # show value of a key
>>> for key in aDict
        print key, aDict[key]         # show all key value pairs
```

### Statements

#### If, elif, else

```
if <expression>:
    <if-suite>
elif <expression>:
    <elif suite>
else:
    <else-suite>
```


#### while

* while is executed until the expression becomes zero or false

```
while <expression>:
    <while suite>
```

#### for

* for is more a foreach iterative type loop like in a shell scripting language

```
for item in [a, b, c,]:
    print item
```


## Source

* Wesley J. Chun: Core Python Programming. 2nd Edition. Prentice Hall.

