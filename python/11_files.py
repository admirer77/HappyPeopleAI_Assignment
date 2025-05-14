import os

# 1. Write a program to read text file
def read_text_file(file_path):
    # Question: Write a program to read text file
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Driver code for reading text file
example_file = 'example.txt'
write_text_file(example_file, "This is a sample text for example.txt.\nIt contains multiple lines of text.\nThis is the third line.")
print("Reading text file:")
print(read_text_file(example_file))


# 2. Write a program to write text to .txt file using InputStream
def write_text_file(file_path, text):
    # Question: Write a program to write text to .txt file using InputStream
    with open(file_path, 'w') as file:
        file.write(text)

# Driver code for writing text to .txt file
output_file = 'output.txt'
write_text_file(output_file, "This is a sample text written to output.txt.")
print("\nText written to output.txt.")


# 3. Write a program to read a file stream
def read_file_stream(file_path):
    # Question: Write a program to read a file stream
    with open(file_path, 'rb') as file:
        content = file.read()
    return content

# Driver code for reading file stream
print("\nReading file stream:")
print(read_file_stream(example_file))


# 4. Write a program to read a file stream supports random access
def read_file_random_access(file_path, start, length):
    # Question: Write a program to read a file stream supports random access
    with open(file_path, 'rb') as file:
        file.seek(start)
        content = file.read(length)
    return content

# Driver code for reading file stream with random access
print("\nReading file stream with random access (start=10, length=20):")
print(read_file_random_access(example_file, 10, 20))


# 5. Write a program to read a file a just to a particular index using seek()
def read_file_seek(file_path, index):
    # Question: Write a program to read a file a just to a particular index using seek()
    with open(file_path, 'r') as file:
        file.seek(index)
        content = file.read()
    return content

# Driver code for reading file from index using seek()
print("\nReading file from index 10 using seek():")
print(read_file_seek(example_file, 10))


# 6. Write a program to check whether a file is having read access and write access permissions
def check_file_permissions(file_path):
    # Question: Write a program to check whether a file is having read access and write access permissions
    read_access = os.access(file_path, os.R_OK)
    write_access = os.access(file_path, os.W_OK)
    return read_access, write_access

# Driver code for checking file permissions
read_access, write_access = check_file_permissions(example_file)
print(f"\nFile read access: {read_access}, write access: {write_access}")
