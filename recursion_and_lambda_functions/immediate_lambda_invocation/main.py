celsius_temperature = 23

# The `lambda` function for converting temperature 
# from `celsius_temperature` variable to fahrenheit temperature 
fahrenheit_temperature = (lambda x :(((9 * x) / 5) + 32))(celsius_temperature)

# Testing the result
print(f'{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit')


