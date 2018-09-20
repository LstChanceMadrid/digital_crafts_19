user_input = input("Enter a word: ")


def backwards_user_input(user_input):
    #defining the variable to store the concatenated letters
    reversed_word = ""
    for index in range(len(user_input) - 1, -1, -1):
        #adding the letters to the variable beginning from the last index
        reversed_word = reversed_word + user_input[index]
    return reversed_word

backwards = backwards_user_input(user_input)


def palindrome(user_input):
    if (user_input == backwards):
        print('palindrome')
    else:
        print("not a palindrome")

palindrome(user_input)

