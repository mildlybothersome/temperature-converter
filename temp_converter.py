#Fahrenheit to Celsius calculator

#module import
import math

#while loop for temp check
run = True

while run:
    print("Welcome to the temperature coverter")
    print()
#Multiple inputs for vice versa calculations
    unit = input("Is your starting temperature in Fahrenheit or Celsius? ")
    if unit == "fahrenheit":
        temp = int(input("what is the temperature? "))
        output_temp = (temp - 32) * 5/9
        print(f"{temp} degrees Fahrenheit is equal to {math.floor(output_temp)} degrees Celsius.")

#remove capitalisation error
    elif unit == "Fahrenheit":
        temp = int(input("what is the temperature? "))
        output_temp = (temp - 32) * 5/9
        print(f"{temp} degrees Fahrenheit is equal to {math.floor(output_temp)} degrees Celsius.")


#celsius formula
    elif unit == "celsius":
        temp = int(input("what is the temperature? "))
        output_temp = (temp * 9/5) + 32
        print(f"{temp} degrees Celsius is equal to {math.floor(output_temp)} degrees Fahrenheit.")

#remove caps error
    elif unit == "Celsius":
        temp = int(input("what is the temperature? "))
        output_temp = (temp * 9/5) + 32
        print(f"{temp} degrees Celsius is equal to {math.floor(output_temp)} degrees Fahrenheit.")

#account for unknowns/spelling errors
    else:
        print("Error: Unknown unit. Please check spelling and try again")

    if input("Do you need to convert another temperature? ") == "no":
        run = False
print()
print("Thank you for using this converter")
