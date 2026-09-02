# Day-07 Student Record Manager

Yesterday I was wrote a code that basically uses dictionary for single student entry.
But, today I wrote a menu-driven, multi-student database program that supports adding, updating, deleting, searching, and analyzing student records.

## Features

1. Student database creation
    - Maintains multiple student records using a list of dictionaries.
2. Add new students
    - Allows the user to specify how many students to add.
    - Collects name, age, department, and marks.
3. Student record storage
    - Stores each student's details as a dictionary inside the database list.
4. Update student details
    - Update a student's:
        - Name
        - Age
        - Department
        - Marks
5. Delete a student
    - Displays student indexes.
    - Allows deletion using the selected index.
6. Search student records
    - Searches for a student by name.
    - Retrieves:
        - Age
        - Department
        - Marks
7. Student existence checking
    - Uses a `found` flag to determine whether the requested student exists.
8. Individual student analysis
    - Calculates:
        - Total marks
        - Average marks
        - Maximum mark
        - Minimum mark
        - Subjects passed
        - Subjects failed
9. Pass/fail analysis
    - Uses 35 marks as the pass threshold.
10. Interactive menu
    - Provides options for adding, updating, searching, and analyzing students.
11. Continuous program execution
    - Uses a while loop so the menu can be used repeatedly.
12. Index-based student deletion
    - Uses enumerate() to display student positions and pop() to remove the selected record.
13. Formatted output
    - Uses f-strings to display student information and analysis clearly.
14. Input-based data processing
    - Accepts student information interactively through input().
15. Marks conversion and analysis
    - Converts mark strings into integers before performing calculations.

## Concepts Practiced

1. Lists of dictionaries
2. Nested data access
3. Looping through structured records
4. `append()`
5. `enumerate()`
6. Updating dictionary values
7. Searching records
8. Boolean flags (`found = False`)
9. Filtering data
10. `pop()`
11. `while` loop
12. Program state / variable lifetime
13. Functions and parameters
14. `.split()`
15. String → integer conversion
16. `=` vs `==`
17. `if / elif / else`
18. `for` loops
19. `sum()`
20. `len()`
21. `max()`
22. `min()`
23. Counters
24. Pass/fail analysis
25. Reading Python tracebacks
26. Debugging logic errors
27. Debugging type/value errors
28. Menu-driven program structure


## How to run ?

```bash
python main.py
```
## Example Output

```text
--------------Welcome to Student Database Manager--------------


Enter your option from below:
1. Entering the new student details
2. Updating the student details
3. Searching from the database
4. Analysis of a particular student
Enter your option here: 1
Welcome.

Enter how many new students you want to add: 1
Enter student detail like name:enter the name, age:enter the age, department:enter the department, marks:78 98 57 43 97
name:Kishore B,age:19,department:ECE,marks:90 91 92 93 94
[{'name': 'Kishore B', 'age': '19', 'department': 'ECE', 'marks': ['90', '91', '92', '93', '94']}]
Enter your option from below:
1. Entering the new student details
2. Updating the student details
3. Searching from the database
4. Analysis of a particular student
Enter your option here: 4
Enter the name of the student: Kishore B
----Analysis of Kishore B----

Total marks    : 460
Average marks  : 92.0
Maximum mark   : 94
Minimum mark   : 90
subjects passed: 5
subjects failed: 0
```