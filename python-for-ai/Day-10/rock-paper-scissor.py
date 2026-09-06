import random

while(1):
    user_choice = input("Your turn (r/p/s/e): ").lower().strip()
    options = {
        'r':'🪨',
        'p':'📃',
        's':'✂️'
    }
    if user_choice == 'r' or user_choice == 'p' or user_choice == 's':
        pc_choice = random.choice(list(options.keys()))
        print(f"Your choice is: {user_choice}")
        print(f"PC chose: {pc_choice}")
        if user_choice == 'r' and pc_choice == 'p':
            print("PC Won!")
        elif user_choice == 'p' and pc_choice == 'r':
            print("You Won!")
        elif user_choice == 'r'and pc_choice == 'r':
            print("Match draw. Try again!")
        elif user_choice == 'p'and pc_choice == 'p':
            print("Match draw. Try again!")
        elif user_choice == 'p' and pc_choice == 's':
            print("PC Won!")
        elif user_choice == 's' and pc_choice == 'p':
            print("You Won!")
        elif user_choice == 's'and pc_choice == 's':
            print("Match draw. Try again!")
        elif user_choice == 'r' and pc_choice == 's':
            print("You Won!")
        elif user_choice == 's' and pc_choice == 'r':
            print("PC Won!")

    elif user_choice == 'e':
        print("Thank you for playing!")
        break
    else:
        print("Invalid Choice. Try again!")

