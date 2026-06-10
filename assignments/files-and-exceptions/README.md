# 📘 Assignment: Working with Files and Exceptions

## 🎯 Objective

Practice reading and writing text files in Python while handling common errors safely. You will build a small notes app that loads existing notes, adds new ones, and keeps the program from crashing when a file is missing or input is invalid.

## 📝 Tasks

### 🛠️ Read and Summarize a Text File

#### Description
Write a function that opens a text file and summarizes its contents.

#### Requirements
Completed program should:

- Open a text file provided by the user.
- Count the number of lines, words, and characters in the file.
- Print the summary in a clear format.
- Use a `try`/`except` block to handle missing files.

### 🛠️ Build a Safe Notes App

#### Description
Extend the program so users can add new notes to a file and continue using the app even when errors happen.

#### Requirements
Completed program should:

- Let the user enter a note and append it to a notes file.
- Read and display all saved notes when the program starts.
- Handle invalid menu choices without crashing.
- Show a friendly message when the notes file does not exist yet.
- Use at least one custom function to keep the code organized.
