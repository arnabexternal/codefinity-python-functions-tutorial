def describe_dog(name, breed, age):
    # Check if the age is valid
    if age < 0:
         return f'Invalid age for {name}. Age cannot be negative.'
    # Check if the dog is a newborn
    elif age == 0:
        return f'{name} is a newborn {breed}. A bundle of joy!'
    # Check if the dog is 1 year old
    elif age == 1:
        return f'{name} is a 1-year-old {breed}. A great companion!'
    # For all other ages, including plural years
    else:
        return f'{name} is a {age}-year-old {breed}. An old dog with much wisdom!'

# Test the function with various scenarios
description = describe_dog('Buddy', 'Labrador', 3)
print(description)