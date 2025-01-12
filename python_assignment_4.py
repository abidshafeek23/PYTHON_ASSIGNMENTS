"""
def calculate(arg1, arg2=10, arg3=None):
    if arg3 is None:
        print("Sum:", arg1 + arg2)
    else:
        print("Product:", arg1 * arg2 * arg3)
calculate(5)
calculate(75,23)
calculate(14,32,96)
"""
"""
def filter_long_strings(strings):
    return [string for string in strings if len(string) >= 5]

input_strings = ["apple", "orange", "banana", "pineapple", "grape","rat","cat","bat"]
result = filter_long_strings(input_strings)
print(result)
"""
"""
def evaluate_expression(expression):
    return eval(expression)
expression = "6 * 7 + 12"
result = evaluate_expression(expression)
print(result)
"""
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes(numbers):
    return list(filter(is_prime, numbers))

input_numbers = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14,15,16,17,18,19]
result = filter_primes(input_numbers)
print(result)  
"""
def convert_to_uppercase(strings):
    return list(map(str.upper, strings))

input_strings = ["sand", "dust", "aster","quest"]
result = convert_to_uppercase(input_strings)
print(result)