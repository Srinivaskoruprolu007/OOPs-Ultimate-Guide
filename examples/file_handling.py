"""
File Handling in Python
-----------------------
This example demonstrates reading from, writing to, and appending to a file.
"""

def write_to_file(file_name, content):
    """
    Write content to a file.
    :param file_name: Name of the file to write.
    :param content: Content to write into the file.
    """
    with open(file_name, 'w') as file:
        file.write(content)
        print(f"Content written to {file_name}")

def read_from_file(file_name):
    """
    Read and print content from a file.
    :param file_name: Name of the file to read.
    """
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of {file_name}:\n{content}")
    except FileNotFoundError:
        print(f"Error: {file_name} does not exist.")

def append_to_file(file_name, content):
    """
    Append content to a file.
    :param file_name: Name of the file to append content.
    :param content: Content to append.
    """
    with open(file_name, 'a') as file:
        file.write(content)
        print(f"Content appended to {file_name}")

# Demonstration
file_name = "sample.txt"
write_to_file(file_name, "Hello, Python!\n")
read_from_file(file_name)
append_to_file(file_name, "This is an appended line.\n")
read_from_file(file_name)
