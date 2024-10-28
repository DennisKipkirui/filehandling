## Demonstrate your understanding of Python file handling by completing the following tasks.

## Tasks:
## File Creation:
## Create a Python script (file_handling_assignment.py) that does the following:
## Creates a new text file named "my_file.txt" in write mode ('w').
## Write at least three lines of text to the file, including a mix of strings and numbers.

## File Reading and Display:
## Enhance your script to read the contents of "my_file.txt" and display them on the console.

## File Appending:
## Modify the script to open "my_file.txt" in append mode ('a').
## Append three additional lines of text to the existing content.

## Error Handling:
## Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError).

Explanation of the Code
File Creation and Writing:

Opens my_file.txt in write mode ('w') and writes three initial lines.
Uses try and except to handle potential issues, such as permissions errors.
File Reading and Displaying:

Opens the file in read mode ('r') to display the contents written so far.
Exception handling is included to manage file-not-found scenarios.
File Appending:

Reopens my_file.txt in append mode ('a') and appends three additional lines.
Exception handling ensures graceful handling if issues arise.
Final File Read:

Reads the updated contents to display all lines, verifying both write and append operations were successful.
This script provides robust file handling with error management and meets each of your specified requirements.