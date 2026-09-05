import random
import datetime
def rolling():
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    return num1, num2
roll_count = 0
play_count = 0
while(1):
    dice_rolling = input("Enter (y (yes) / n (no) / l (log):").lower().strip()
    if dice_rolling == 'y':
        number_of_times = int(input("Enter how many times want to roll: "))
        for n in range(number_of_times):
            num1,num2 = rolling()
            print(f"({num1},{num2})")
            roll_count = roll_count + 1
        play_count = play_count + 1
    elif dice_rolling == 'l':
        now = datetime.datetime.now()
        with open("dice_log.txt","a") as f:
            f.write(f"[{now.strftime("%d-%m-%Y | %H:%M:%S")}]\n"
                    f"You have played {play_count} times!\n"
                    f"You have rolled {roll_count} times!\n")
        with open("dice_log.txt","r") as f:
            for line in f:
                print(line.strip())
    elif dice_rolling == 'n':
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice!.")
    


