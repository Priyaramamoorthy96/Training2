### An Introduction to PEP-8
The Python programming language has evolved over the past year as one of the most favourite programming languages. This language is relatively easy to learn than most of the programming languages. It is a multi-paradigm, it has lots of open source modules that add up the utility of the language and it is gaining popularity in data science and web development community.
#### Indentation
When programming in Python, indentation is something that you will definitely use. However, you should be careful with it, as it can lead to syntax errors. The recommendation is therefore to use 4 spaces for indentation. For example, this statement uses 4 spaces of indentation
```
Example :
if True:
    print("If works")
```
#### Maximum Line Length
Generally, it's good to aim for a line length of 79 characters in your Python code.
Following this target number has many advantages. A couple of them are the following:
- It is possible to open files side by side to compare;
- You can view the whole expression without scrolling horizontally which adds to better readability and understanding of the code.
- Comments should have 72 characters of line length. You'll learn more about the most common conventions for comments later on in this tutorial!

In the end, it is up to you what coding conventions and style you like to follow if you are working in a small group and it is acceptable for most of the developers to divert from the maximum line length guideline. However, if you are making or contributing to an open source project, you'll probably want and/or need to comply with the maximum line length rule that is set out by PEP-8.
```
Example :
total = (A +
         B +
         C)
```
### Blank Lines
In Python scripts, top-level function and classes are separated by two blank lines. Method definitions inside classes should be separated by one blank line.
### Whitespaces in Expressions and Statements
You should try to avoid whitespaces when you see your code is written just like in the following examples:
```
Example :
func(data, {pivot: 4})
x = 1
y = 2
long_variable = 3
```
### Source File Encoding
A computer cannot store "letters", "numbers", "pictures" or anything else; It can only store and work with bits, which can only have binary values: yes or no, true or false, 1 or 0, etc. As you already know, a computer works with electricity; This means that an "actual" bit is the presence or absence of a blip of electricity. You would usually represent this (lack of) presence with 1 and 0.
To use bits to represent anything at all besides bits, you need a set of rules. You need to convert a sequence of bits into something like letters, numbers and pictures using an encoding scheme or encoding. Examples of encoding schemes are ASCII, UTF-8, etc
### Comments
Comments are used for in-code documentation in Python. They add to the understanding of the code. There are lots of tools that you can use to generate documentation, such as comments and docstrings, for your own module. Comments should be more verbose so that when someone reads the code, the person would get the proper understanding of the code and how it is being used with other pieces of the code.
Comments start with the # symbol. Anything written after the hashtag does not get executed by the interpreter. For example, the following code chunk will only give back "This is a Python comment"
### Imports
Importing libraries and/or modules is something that you'll often do when you're working with Python for data science. As you might already know, you should always import libraries at the start of your script.
### Naming Conventions
When you program in Python, you'll most certainly make use of a naming convention, a set of rules for choosing the character sequence that should be used for identifiers which denote variables, types, functions, and other entities in source code and documentation.
