number = float(input("Type any number: "))

def type_of_num(number):
    if number.is_integer():
        num_type = "Integer"
    else:
        num_type = "Decimal"
    return num_type
num_type =type_of_num(number)

def sign_of_num(number):
    if number < 0:
        num_sign = "Negative"
    elif number == 0:
        num_sign = "Zero"
    else:
        num_sign = "Positive"
    return num_sign

num_sign = sign_of_num(number)

def parity_of_num(number):
    if number % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"
    return parity

square = number ** 2
absolute = abs(number)

print(
    "___Number analysis___\n"
    f"Type: {num_type}\n"
    f"Sign: {num_sign}\n"
)

if number.is_integer():
    parity = parity_of_num(number)
    print(f"Parity: {parity}\n")
else:
    print(f"A decimal number cannot be classified as even or odd.\n")

print(
    f"Square: {square}\n"
    f"Absolute: {absolute}\n"

    "Thank you for coming!"
)

