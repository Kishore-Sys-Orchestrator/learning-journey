marks_str = input("Enter the marks with a space between each: ").split()

def mark_analyzer(marks_str):
    marks_num = []
    
    for mark in marks_str:
        marks_num.append(float(mark))
        
    number_of_sub = len(marks_num)
    total_marks = sum(marks_num)
    average = total_marks/number_of_sub
    maximum = max(marks_num)
    minimum = min(marks_num)
    passed = 0
    failed =0
    for mark in marks_num:
        if mark >=40:
            passed = passed + 1
        else:
            failed = failed + 1

    print(
        "-----Student Marks Analyzer-----\n"
        f"Total subjects: {number_of_sub}\n"
        f"Total marks obtained: {total_marks}\n"
        f"Average: {average}\n"
        f"Maximum mark obtained: {maximum}\n"
        f"Minimum marks obtained: {minimum}\n"
        f"Number of subjects passed: {passed}\n"
        f"Number of subjects failed: {failed}\n"
    )

if len(marks_str) == 0:
    print("You didn't enter any marks. So, please enter your marks.")
else:
    mark_analyzer(marks_str)