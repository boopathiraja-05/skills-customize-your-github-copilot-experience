def summarize_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file_handle:
            contents = file_handle.read()
    except FileNotFoundError:
        print(f"Could not find {file_path}.")
        return

    line_count = len(contents.splitlines())
    word_count = len(contents.split())
    character_count = len(contents)

    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {character_count}")


def show_notes(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file_handle:
            notes = file_handle.readlines()
    except FileNotFoundError:
        print("No notes file found yet. A new one will be created when you add your first note.")
        return

    if not notes:
        print("No saved notes yet.")
        return

    print("Saved notes:")
    for note in notes:
        print(f"- {note.strip()}")


def add_note(file_path):
    note = input("Enter a new note: ").strip()
    if not note:
        print("Note cannot be empty.")
        return

    with open(file_path, "a", encoding="utf-8") as file_handle:
        file_handle.write(note + "\n")

    print("Note saved.")


def main():
    notes_file = "notes.txt"
    show_notes(notes_file)

    while True:
        print("\n1. Summarize a file")
        print("2. Add a note")
        print("3. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            file_path = input("Enter the file path: ").strip()
            summarize_file(file_path)
        elif choice == "2":
            add_note(notes_file)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
