def add_entry():
    # Prompt the user to input a journal entry
    entry = input("Write your journal entry for today: ")
    try:
        # Open the file 'journal.txt' in append mode ('a')
        with open("journal.txt", "a") as file:
            # Write the entry to the file with a newline character
            file.write(entry + "\n")
        # Inform the user that the entry was added successfully
        print("Entry added successfully!")
    except IsADirectoryError:
        # Handle the case where 'journal.txt' is a directory instead of a file
        print("Error: 'journal.txt' is a directory, not a file.")
    except PermissionError:
        # Handle the case where the user does not have permission to write to 'journal.txt'
        print("Error: You do not have permission to write to 'journal.txt'.")

def read_entries():
    try:
        # Open the file 'journal.txt' in read mode ('r')
        with open("journal.txt", "r") as file:
            # Read all lines from the file into a list
            entries = file.readlines()
            # Iterate over each entry and print it
            for entry in entries:
                print(entry.strip())  # Remove leading/trailing whitespace and print
    except FileNotFoundError:
        # Handle the case where 'journal.txt' does not exist
        print("No journal entries found. Start by adding a new entry.")
    except IsADirectoryError:
        # Handle the case where 'journal.txt' is a directory instead of a file
        print("Error: 'journal.txt' is a directory, not a file.")
    except PermissionError:
        # Handle the case where the user does not have permission to read 'journal.txt'
        print("Error: You do not have permission to read 'journal.txt'.")

# Call the function to add a new journal entry
add_entry()
# Call the function to read and display journal entries
read_entries()
