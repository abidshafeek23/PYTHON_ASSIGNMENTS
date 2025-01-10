"""
month = int(input("Enter the month: "))
if 1 <= month <= 12:
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    print(f"Month {month} is {months[month - 1]}")
else:
    print("Invalid month number.")
    """
"""
age = int(input("Enter your age: "))
if age < 16:
    ticket_price = 6 / 2
elif age >= 60:
    ticket_price = 6 / 3
else:
    ticket_price = 6
print(f"Your ticket costs £{ticket_price:.2f}")
"""
"""
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10
print(f"The reversed number is {reverse}")
"""
"""
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")
"""
"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b and a > c:
    greatest = a
elif b > c:
    greatest = b
else:
    greatest = c
print(f"The greatest number is {greatest}")
"""
"""
num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))
print(f"The multiples of {num} are:")
for i in range(1, limit + 1):
    print(num * i)                                                                                                                                                                                                                  
"""
"""
while True:
    value = input(":")
    if value == "done":
        print("Done")
        break
    else:
        print(value)
   """
"""
for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
 """

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

