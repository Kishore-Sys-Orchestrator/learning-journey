# Day-09 Rock Paper Scissors Game 

After practicing file handling with the Books Manager, I built a fun interactive project — a **Rock Paper Scissors game**.  
This program uses Python’s `random` module to let the computer pick a choice, and you play against it with emoji‑based output.

## Features:
- Play Rock 🪨, Paper 📃, or Scissors ✂️
- Emoji display for choices
- Random computer choice
- Win/Loss/Draw detection
- Continuous play until exit
- Input validation for wrong entries
- Exit option (`e`)

## Concept Practiced:
1. `random.choice()`
2. Dictionaries for mapping
3. `while` Loop for continuous play
4. `if / elif / else` conditions
5. String methods (`.lower()`, `.strip()`)
6. Input validation
7. Game logic implementation

## How to run?

```bash
python main.py
```

## Example output:

```text
Your turn (r/p/s/e): r
Your choice is: r
PC chose: p
PC Won!

Your turn (r/p/s/e): s
Your choice is: s
PC chose: p
You Won!

Your turn (r/p/s/e): e
Thank you for playing!
```