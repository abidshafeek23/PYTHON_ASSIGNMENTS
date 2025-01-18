"""
filename = input("Enter the file name to read: ")
try:
    file = open(filename, "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found.")
"""
"""
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")
try:
    source = open(source_file, "r")
    destination = open(destination_file, "w")
    content = source.read()
    destination.write(content)
    print("File copied successfully.")
    source.close()
    destination.close()
except FileNotFoundError:
    print("Source file not found.")
"""
"""
filename = input("Enter the file name: ")
try:
    file = open(filename, "r")
    content = file.read()
    words = content.split()
    print("Total number of words:", len(words))
    file.close()
except FileNotFoundError:
    print("File not found.")
"""
"""
user_input = input("Enter a string to convert to integer: ")
try:
    number = int(user_input)
    print("The integer is:", number)
except ValueError:
    print("Invalid input! Could not convert to integer.")
"""
"""
try:
    user_input = input("Enter a list of integers separated by space: ")
    numbers = [int(x) for x in user_input.split()]
    for num in numbers:
        if num < 0:
            raise ValueError("Negative integer found!")
    print("All integers are non-negative.")
except ValueError as e:
    print("Error:", e)

"""



"""
filename = input("Enter the file name to write to: ")
content = input("Enter the content to write to the file: ")
try:
    file = open(filename, "w")
    file.write(content)
    file.close()
    print("Content written to file successfully.")
    print("Welcome! Operation completed without errors.")
except Exception as e:
    print("An error occurred:", e)
"""

try:
    user_input = input("Enter a list of integers separated by space: ")
    numbers = [int(x) for x in user_input.split()]
    average = sum(numbers) / len(numbers)
    print("The average is:", average)
except ZeroDivisionError:
    print("Cannot compute the average of an empty list.")
except ValueError:
    print("Invalid input! Please enter integers only.")
finally:
    print("Program has finished running.")