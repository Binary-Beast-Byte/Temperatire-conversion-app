# You are responsible for writing a program that will convert a given temperature in degrees
# Fahrenheit to degrees Celsius and degrees Kelvin
print("welcome to the temperature conversion app created by Ravi !")

#getting input form the user in a degree farenheit
farenheit = float(input("Enter your temperature in degree farenheit: "))

#convert farenheit to degree celcius
celcius = (5/9)*(farenheit-32)

#rounding into 4 decimal places
celcius_round = round(celcius,4)

#convert farenheit to degree Kelvin
kelvin = (5/9)*(farenheit-32)+273.15

#rounding into 4 decimal places
kelvin_round = round(kelvin,4)

print("\n")
print("Temerature in celcius is: ",celcius_round)
print("Temerature in kelvin is: ",kelvin_round)



