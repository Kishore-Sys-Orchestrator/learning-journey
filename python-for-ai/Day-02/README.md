# Day 2 - Python Fundamentals

## What I Learned

Today I learned:

- Variables and user input using `input()`
- `str` and `int` data types
- Type casting using `int()`
- String methods such as `.lower()`
- f-strings for formatting output
- Arithmetic operations
- Conditional statements: `if`, `elif`, `else`
- Assignment operator `=`
- Equality comparison operator `==`
- Defining and calling functions
- Parameters and arguments
- Returning values using `return`

## What I Built

I built a small Personal Profile Analyzer that combines the concepts I learned today.

The program:

- Asks the user for their name and age.
- Asks whether they are a student.
- If they answer `yes`, it asks for their college and branch.
- If they answer `no`, it skips the college and branch questions.
- If they enter anything other than `yes` or `no`, it displays an invalid-input message.
- Determines whether the user is an adult or minor.
- Calculates their age for the next year.

## Concepts Practiced

- Variables and `input()`
- Type casting
- `str` and `int`
- `.lower()`
- f-strings
- Conditional statements
- Comparison and assignment operators
- Functions
- Parameters and arguments
- `return`

## Mistakes I Made

1. I called a function without passing the required argument.
2. I initially structured my conditionals incorrectly. I placed the age check inside the student-status condition even though the two decisions were independent.
3. I confused `is` with `==` when comparing values.
4. I initially printed the result inside my function instead of returning it. I learned that returning a value makes the function more reusable because the calling code can decide how to use the result.

## What I Understand Better Now

I understand how data flows through a simple Python program: I can take input, convert it to the required type, make decisions using conditionals, pass data into functions, and return results from functions.

I also understand the difference between `=` for assignment and `==` for comparing values.

## What I Will Build on Day 3

I will learn and practice the Python concepts that are needed for the next task rather than trying to learn Python topics randomly.

I am following a need-based learning approach: I will first identify what the next task requires, then learn the necessary concepts and apply them while building.