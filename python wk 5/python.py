def create_file():
    try:
        # Create a new text file in write mode
        with open('my_file.txt', 'w') as file:
            # Write at least three lines of text, including a mix of strings and numbers
            file.write("Hello, this is my first line.\n")
            file.write("The year is 2024.\n")
            file.write("I have 3 apples and 2 oranges.\n")
        print("File 'my_file.txt' created and content written.")
    
    except (PermissionError, Exception) as e:
        print(f"Error while creating the file: {e}")

def read_file():
    try:
        # Read the contents of "my_file.txt" and display them
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("Content of 'my_file.txt':")
            print(content)

    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    
    except PermissionError:
        print("Error: You do not have permission to read 'my_file.txt'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file():
    try:
        # Open "my_file.txt" in append mode
        with open('my_file.txt', 'a') as file:
            # Append three additional lines of text
            file.write("This is an additional line 1.\n")
            file.write("Here comes another line, number 2.\n")
            file.write("Finally, this is line number 3.\n")
        print("Content appended to 'my_file.txt'.")
    
    except (PermissionError, Exception) as e:
        print(f"Error while appending to the file: {e}")

if __name__ == "__main__":
    create_file()      
    read_file()        
    append_to_file()   
    read_file()        