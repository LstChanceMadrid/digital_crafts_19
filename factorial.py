input_number = int(input("Enter a number: "))


def calculate(input_number):
    if (input_number > 0):
        factorial(input_number)
    else:
        print("Your number must be a positive integer above 0")

def factorial(input_number):
    number = input_number + 1
    factorial = 1
    while number > 1:
        number -= 1
        factorial *= number
    print(factorial)


calculate(input_number)




