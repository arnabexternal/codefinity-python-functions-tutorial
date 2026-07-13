def even_numbers(start, stop):
    while start <= stop:
        if start % 2 == 0:
            yield start
        start += 1

# Testing the result
for num in even_numbers(1, 10):
    print(num)