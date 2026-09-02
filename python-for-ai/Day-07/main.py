print("--------------Welcome to Student Database Manager--------------\n\n")

data = []
while(1):
    options = int(input("Enter your option from below:\n"
                        "1. Entering the new student details\n"
                        "2. Updating the student details\n"
                        "3. Searching from the database\n"
                        "4. Analysis of a particular student\n"
                        "Enter your option here: "))

    


    def option_1(data):
        print("Welcome.\n")
        student_count = int(input("Enter how many new students you want to add: "))

        for _ in range(student_count):
            user_input = input(
                "Enter student detail like name:enter the name, age:enter the age, "
                "department:enter the department, marks:78 98 57 43 97\n"
            )

            student = dict(item.split(':') for item in user_input.split(','))

            student["marks"] = student["marks"].split()

            data.append(student)

        for student in data:
            if not student["marks"]:
                student["marks"] = input(
                    f"Enter the marks for {student['name']}: "
                ).split()
            else:
                return data

        return data


    def option_2(data):
        option = input(
            "Enter your option: a.) changing the details, b.) delete a student: "
        )

        if option == 'a':
            name = input(
                "Enter the name of the student whose details you want to update: "
            )

            update_detail = int(
                input("Enter what you want to update(1.name, 2.age, 3.department, 4.mark): ")
            )

            found = False

            if update_detail == 1:
                new_name = input("Enter the new name: ")

                for student in data:
                    if student["name"] == name:
                        student["name"] = new_name
                        print(f"{name} updated to {new_name}")
                        found = True

            elif update_detail == 2:
                new_age = int(input("Enter the new age: "))

                for student in data:
                    if student["name"] == name:
                        student["age"] = new_age
                        print(f"age is updated to {new_age}")
                        found = True

            elif update_detail == 3:
                update_dep = input("Enter the new department name: ")

                for student in data:
                    if student["name"] == name:
                        student["department"] = update_dep
                        print(f"department details changed to {update_dep}")
                        found = True

            elif update_detail == 4:
                new_marks = input("Enter the new marks: ").split()

                for student in data:
                    if student["name"] == name:
                        student["marks"] = new_marks
                        print(f"Marks updated to {new_marks}")
                        found = True

            else:
                print("please enter the correct option")

            if not found:
                print(f"Sorry there is no {name} in the record")

        elif option == 'b':
            for index, student in enumerate(data):
                print(index, student["name"])

            print("Now you can see the entire student list with their index.\n")

            delete_index = int(
                input("Enter the index of the student to be deleted: ")
            )

            data.pop(delete_index)

            print(data)

        else:
            print("Please enter the correct option.")


    def option_3(data):
        search_name = input(
            "Enter the name of the student whose detail you want to search: "
        )

        search_value = int(
            input("Enter the option to search (1.age, 2.department, 3.marks): ")
        )

        found = False

        if search_value == 1:
            for student in data:
                if student["name"] == search_name:
                    print(f"Age of {search_name} is {student['age']}")
                    found = True

        elif search_value == 2:
            for student in data:
                if student["name"] == search_name:
                    print(
                        f"Department of {search_name} is {student['department']}"
                    )
                    found = True

        elif search_value == 3:
            for student in data:
                if student["name"] == search_name:
                    print(f"Marks of {search_name} is {student['marks']}")
                    found = True

        else:
            print("Please enter the valid option")

        if not found:
            print(f"Sorry there is no {search_name} in the record")


    def option_4(data):
        search_name = input("Enter the name of the student: ")

        found = False

        for student in data:
            if student["name"] == search_name:
                found = True

                marks = student["marks"]

                int_mark = []

                for mark in marks:
                    int_mark.append(int(mark))

                total_marks = sum(int_mark)
                average = total_marks / len(int_mark)
                maximum_mark = max(int_mark)
                minimum_mark = min(int_mark)

                pass_count = 0
                fail_count = 0

                for mark in int_mark:
                    if mark >= 35:
                        pass_count = pass_count + 1
                    else:
                        fail_count = fail_count + 1

                print(
                    f"----Analysis of {search_name}----\n\n"
                    f"Total marks    : {total_marks}\n"
                    f"Average marks  : {average}\n"
                    f"Maximum mark   : {maximum_mark}\n"
                    f"Minimum mark   : {minimum_mark}\n"
                    f"subjects passed: {pass_count}\n"
                    f"subjects failed: {fail_count}"
                )

        if not found:
            print(f"Sorry there is no {search_name} in the record")


    if options == 1:
        student_data = option_1(data)
        print(student_data)

    elif options == 2:
        option_2(data)

    elif options == 3:
        option_3(data)

    elif options == 4:
        option_4(data)

    else:
        print("Invalid options")