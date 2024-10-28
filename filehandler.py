# file_handling_assignment.py

def main():
    filename = "my_file.txt"

    # Step 1: File Creation and Writing
    try:
        with open(filename, 'w') as file:
            # Writing three lines of text with a mix of strings and numbers
            file.write("Hello, this is line 1.\n")
            file.write("Line 2 includes a number: 42\n")
            file.write("The final line of the first write operation.\n")
        print(f"File '{filename}' created and initial lines written successfully.")

    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred while creating or writing to the file: {e}")

    # Step 2: File Reading and Displaying
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nContents of the file after the initial write:")
            print(content)

    except FileNotFoundError:
        print("File not found: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    # Step 3: File Appending
    try:
        with open(filename, 'a') as file:
            # Appending three more lines
            file.write("Now adding more content.\n")
            file.write("Here's line 5.\n")
            file.write("Final appended line.\n")
        print("\nAdditional lines appended successfully.")

    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

    # Step 4: Final File Read to Display Updated Content
    try:
        with open(filename, 'r') as file:
            updated_content = file.read()
            print("\nContents of the file after appending:")
            print(updated_content)

    except FileNotFoundError:
        print("File not found: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

if __name__ == "__main__":
    main()
