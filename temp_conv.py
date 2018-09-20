user_conversion = input("Enter 'F' to convert to Fahrenheit or 'C' to convert to Celsius: ").lower()

user_temperature = int(input("Enter your temperature: "))

def conversion_type(conversion, temp):
    if (conversion == 'f'):
        celcius_to_fahrenheit(temp)
    elif (conversion == 'c'):
        fahrenheit_to_celcius(temp)
    else:
        print("Invalid option")


def fahrenheit_to_celcius(temp):
    celcius = (temp - 32) * 5 / 9
    print(celcius)

def celcius_to_fahrenheit(temp):
    fahrenheit = temp * 9 / 5 + 32
    print(fahrenheit)

conversion_type(user_conversion, user_temperature)