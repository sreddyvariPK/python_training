Python for Absolute Beginners Course

![](media/python-absolute-beginners.jpg)



**Theory Concepts:**

**I. About Python:** 

​    Python is a widely used general-purpose, high-level programming language. It was initially designed by Guido van Rossum in 1991 and developed by Python Software Foundation. It was mainly developed for emphasis on code readability, and its syntax allows programmers to express concepts in fewer lines of code

**II.PEP naming conventions:**

​    A naming convention is a convention (generally agreed scheme) for naming things. Conventions differ in their intents, which may include to: Allow useful information to be deduced from the names based on regularities.

**Variable**: Use a lowercase single letter, word, or words. Separate words with underscores to improve readability. 

**example**: y , variable , my_variable

**Class**: Start each word with a capital letter. Do not separate words with underscores. This style is called camel case.

**example**: Model , MyClass

**III.Indentations:**
	Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. Python uses indentation to indicate a block of code.

**IV.Data types and variables:**	Refer /parctices/variables.py for more exercises: 
	Variables are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some space in memory. Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory.
	Python has five standard data types
        Numbers : Number data types store numeric values. Number objects are created when you assign a value to them.
![pythonnumbers](media/pythonnumbers.PNG)
        **String**: Strings in Python are identified as a contiguous set of characters represented in the quotation marks.
        **List**: A list contains items separated by commas and enclosed within square brackets ([]).
        **Tuple** : A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.
        **Dictionary**: Python's dictionaries are kind of hash table type. 

**V.Receiving Inputs from users:**
	**Example**: 	
		Name = input(“enter name: “)
		Color = input(“enter favourite color: ”)
		Print(“name” + Name + “ color is” + color)
	**Formatted Strings:**	
		msg = f'{person_name} likes {favourite_car} car'
**VI.Type Conversion:**
	**Example**:
		birth_year = input(“birth year: “)
        age  = 2020 – birth_year // Error occurs because int and string using
        age = 2020 – int(birth_year)
        Print(age)

**VII.Strings & String Methods:**
        content = “Python for Beginners”
        Print(len(content)
        Print(upper(content)
        Print(lower(content))
        Print(content.find(‘n’))
        Print(content.replace(‘Be’, ‘BE’))
        Print(‘Python’ in content)

**VIII.Operators:** 
	Operators are special symbols in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the operand.

1 + 2 => Here, + is the operator that performs addition. 1 and 2 are the operands and 3 is the output of the operation.

Python divides the operators in the following groups:

**Arithmetic operators:** Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.

![arithmaticoperators](media/arithmaticoperators.PNG)


Note: Refer /practices/operators.py for more exercises

**Comparison operators :** Comparison operators are used to compare values. It returns either True or False according to the condition.
Note: Refere operators.py for more exercises

**Logical operators:** Logical operators are the and, or, not operators.
Note: Refer /practices/operators.py for more exercises

![logical](media/logical.PNG)

**Assignment operators :** Assignment operators are used in Python to assign values to variables.
![assignment](media/assignment.PNG)

**Identity operators:** "is" and "is not" are the identity operators in Python.
![identityOperators](media/identityOperators.PNG)

**Membership operators:** in and not in are the membership operators in Python. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).
![membershipOperators](media/membershipOperators.PNG)

**Bitwise operators:** Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.
![bitwiseOperators](media/bitwiseOperators.PNG)

Loops:
    While loops - Refer /practices/while_loop.py for more exercises

​	For Loops - Refer for_loop,py for more exercises

​	Nested Loops - Refer nested_loop.py for more exercises

Lists - lists.py