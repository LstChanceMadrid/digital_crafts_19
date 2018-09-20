user_conversion = input("Enter 'F' to convert to Fahrenheit or 'C' to convert to Celsius: ").lower()

user_temperature = int(input("Enter your temperature: "))

#determines the conversion type and relays the temperature
def conversion_type(conversion, temp):
    if (conversion == 'f'):
        celcius_to_fahrenheit(temp)
    elif (conversion == 'c'):
        fahrenheit_to_celcius(temp)
    else:
        print("Invalid option")

#converts the given temperature to Celsius
def fahrenheit_to_celcius(temp):
    celcius = (temp - 32) * 5 / 9
    print(celcius)

#converts the given temperature to fahrenheit
def celcius_to_fahrenheit(temp):
    fahrenheit = temp * 9 / 5 + 32
    print(fahrenheit)

conversion_type(user_conversion, user_temperature)