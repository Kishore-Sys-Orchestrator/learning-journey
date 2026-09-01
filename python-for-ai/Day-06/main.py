#Day-06: Student record

name = input("Enter you name: ")
age = int(input("Enter your age: "))
department = input("Enter your department name: ")
marks = input("Enter your marks in each subjects with white space between each: ").split()
def student_record_manage(name,age,department,marks):
    marks_num = []
    for mark in marks:
        marks_num.append(float(mark))
    passed =0
    failed =0
    for mark in marks_num:
        if mark >= 35:
            passed = passed + 1
        else:
            failed = failed + 1
    total_marks =sum(marks_num)
    length_of_marks = len(marks_num)
    student_record = {
                    "Name":name,
                    "Age":age,
                    "Department":department,
                    "Marks":marks_num,
                    "Total_marks":total_marks,
                    "Average_marks":total_marks/length_of_marks,
                    "Maximum_marks":max(marks_num),
                    "Minimum_marks":min(marks_num),
                    "Number_of_subjects_passed":passed,
                    "Number_of_subjects_failed":failed
                    }
    print("----Student Record----")
    for key,value in student_record.items():
        print(f"{key} : {value}")

if not marks:
    print("No empty entry is allowed, please enter the marks.")
else:
    student_record_manage(name,age,department,marks)