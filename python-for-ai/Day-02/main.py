name=input("Enter your name: ")
age= int(input("Enter your age: "))
status=input("Whether you are a student?: ").lower()

def adult_status(age):
    if age>=18:
        return "an adult."
    else:
        return "a minor."
age_status = adult_status(age)

if(status == "yes"):
    college=input("Enter your college name: ")
    branch=input("Enter your branch name: ")
    print(
        f"Hey {name}! You are currently {age} years old.\n"
        f"You are a student at {college} and currently studying {branch}.\n"
        f"You are {age_status},\n"
        f"Your age next year will be {age + 1}."
        )

elif status=="no":
    print(f"Hey {name},\n"
    f"you are {age_status},\n"
    f"Thank you for coming!."
    )

else:
    print("Enter yes or no.")