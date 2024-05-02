# Project Title

Word Guess Game

# Author

Gyening Kwadjo Augustine (Individual)

# Description

This Python program is a word guessing game where the player attempts to guess a randomly selected word from a predefined list of words. The program prompts the user to guess letters in the word within a limited number of tries.

## Functionality

### `to_str(mylist)`

- Function that concatenates the elements of a list into a string.
- Example: `to_str(['c','a','r'])` returns `'car'`.
- Parameters: `mylist` (list) - List of elements to concatenate.
- Returns: Concatenated string.

### Word Guessing Game Workflow

1. The game randomly selects a word from a predefined list of words.
2. The user has 7 tries to guess the word by inputting letters one at a time.
3. The program provides feedback on correct and incorrect guesses.
4. Displays the number of remaining tries after each guess.
5. If the user correctly guesses the entire word within the given tries, the game ends, and the correct word is displayed.
6. If the user exhausts all tries without correctly guessing the word, the game ends, and the correct word is revealed.

## Usage

1. Run the Python script.
2. Enter letters to guess the word within the specified number of tries.

## Code Structure

The main components of the program include:

- `to_str(mylist)`: Function to concatenate a list into a string.
- Word selection and initialization: Randomly selects a word from a list and initializes the guessing process.
- Guessing Loop: Allows the user to input letter guesses until the word is guessed correctly or until the number of tries is exhausted.
- Feedback: Provides feedback on correct and incorrect guesses, displaying the number of remaining tries.

## How to Run

- Ensure Python is installed.
- Execute the Python script containing the game code.

### Example Output

```
WORD GUESS GAME
-----
Enter a letter: t
-----
6 tries remaining
Enter a letter: a
-----
Incorrect
5 tries remaining
...
```

# Contributing
If you would like to contribute to this project, you can send a mail to gyeningaugustine7@gmail.com
