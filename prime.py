user_input = int(input("Enter a number: "))


def prime(valid):
    print(valid)
    if (valid < 2):
        print("Not a prime number")
    elif (valid == 2):
        print("Prime number")
    for number in range(2, valid):
        if (valid % number) == 0:
            print("Not a prime number")
            break
        else:
            print("Prime number")
            break



prime(user_input)

