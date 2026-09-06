# Day-9

# Dice Rolling Game

Building on random number generation and file handling, I created a **Dice Rolling Game** that lets you roll dice multiple times, track play statistics, and log results with timestamps.

## Features:
- Roll two dice at once
- Choose how many times to roll
- Track total rolls and play sessions
- Save logs with date & time
- View complete log history
- Continuous play until exit
- Input validation for wrong entries
- Exit option (`n`)

## Concepts Practiced:
1. `random.randint()`
2. Functions (`def rolling()`)
3. `while` Loop for continuous play
4. `for` Loop for multiple rolls
5. Counters (`roll_count`, `play_count`)
6. `datetime.datetime.now()`
7. File handling (`open()`, `with open()`)
8. File modes (`a`, `r`)
9. Writing formatted logs
10. String methods (`.lower()`, `.strip()`)
11. Input validation
12. Persistent storage of logs

## How to run?

```bash
python main.py
```

## Example output:

```text
Enter (y (yes) / n (no) / l (log): y
Enter how many times want to roll: 3
(4,2)
(6,1)
(3,5)

Enter (y (yes) / n (no) / l (log): l
[06-09-2026 | 23:45:12]
You have played 1 times!
You have rolled 3 times!

Enter (y (yes) / n (no) / l (log): n
Thank you for playing!
```


# Number Guessing Game

This project is a fun interactive **Number Guessing Game**.  
The computer randomly selects a number between 1 and 100, and the player tries to guess it.  
Hints are provided if the guess is too high or too low, and the game tracks the number of attempts.

## Features:
- Random number generation between 1–100
- Player guesses until correct or exits
- Hint system (higher/lower)
- Attempt counter
- Option to end the game early (`0`)
- Continuous play until user chooses to quit
- Input validation for wrong entries

## Concepts Practiced:
1. `random.randint()`
2. `while` Loop for continuous play
3. Nested `while True` loop for guessing
4. Counters (`count`)
5. Conditional logic (`if / elif / else`)
6. String methods (`.lower()`, `.strip()`)
7. Input validation
8. Breaking loops (`break`)

## How to run?

```bash
python main.py
```

## Example output:

```text
Whether you want to play or not (y/n): y
Enter 0 while prompt to end the game
Guess a number between 1 to 100: 50
Your guess is lower, try again!
Guess a number between 1 to 100: 75
Your guess is higher, try again!
Guess a number between 1 to 100: 63
Hurray!, you guessed correctly at your 3 attempt.

Whether you want to play or not (y/n): n
Thank you for playing!.
```