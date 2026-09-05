import random

while(1):
    user_preference = input("Whether you want to play or not (y/n): ").lower().strip()

    if user_preference == 'y':

        pc_guess = random.randint(1,100)
        count = 0
        while True:
            count = count + 1
            print("Enter 0 while prompt to end the game")

            attempt = int(input("Guess a number between 1 to 100: "))

            if attempt == 0:
                user_preference = attempt
                print("User ended the game.")
                break

            elif attempt == pc_guess:
                print(f"Hurray!, you guessed correctly at your {count} attempt.")
                break

            elif attempt < pc_guess and attempt >= 1 :
                print("Your guess is lower, try again!")
                
            elif attempt > pc_guess and attempt <= 100:
                print("Your guess is higher, try again!")

            else:
                print("Invalid guess.Try again!")

    elif user_preference == 'n':
        print("Thank you for playing!.")
        break

    else:
        print("Invalid choice!")

        

