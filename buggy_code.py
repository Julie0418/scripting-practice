# def sum_of_numbers(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i
#     return sum

# n = int(input("Enter a number: "))
# print("Sum of numbers from 1 to", n, "is:", sum_of_numbers(n))


# def fizzbuzz(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# n = int(input("Enter a number: "))
# fizzbuzz(n)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
print("Temperature in Celsius:", temp_celsius)