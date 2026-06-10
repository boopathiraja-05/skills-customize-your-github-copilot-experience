# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. Players will guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Set Up Game State

#### Description
Create the foundation of the Hangman game by setting up the word selection and game state tracking.

#### Requirements
Completed program should:

- Randomly select words from a predefined list
- Initialize tracking for attempts remaining
- Keep track of guessed letters and correct guesses
- Display the current progress in underscore format (_ _ _)

### 🛠️ Implement Letter Guessing

#### Description
Build the core gameplay loop that accepts letter guesses and updates the game state.

#### Requirements
Completed program should:

- Accept letter guesses from the user
- Check if guessed letters are in the word
- Update the display to show correct letters
- Track incorrect guesses and decrement attempts
- Prevent duplicate guesses

### 🛠️ Finish Game and Display Results

#### Description
Complete the game by implementing win/lose conditions and displaying appropriate messages.

#### Requirements
Completed program should:

- Check for win condition (all letters guessed)
- Check for lose condition (attempts exhausted)
- Display final messages for both win and lose scenarios
- Show the complete word and game statistics at the end
