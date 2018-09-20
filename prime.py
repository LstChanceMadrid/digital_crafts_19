user_input = int(input("Enter a number: "))


def prime(valid):
    print(valid)
    if (valid < 2):
        print("Not a prime number")
    elif (valid == 2):
        print("Prime number")
    else:
        next(valid)

def next(number):
    instance = 1
    for index in range(2, number):
        if (number % index == 0):
            instance += 1

    if (instance > 1):
        print("Not a prime number")
    else:
        print("Prime number")


prime(user_input)

