def list_sum(numbers):
    if len(numbers) == 0:          # Base case
        return 0
    return numbers[0] + list_sum(numbers[1:])  # Recursive case

# Testing the result
print(list_sum([1, 2, 3, 4, 5]))   # 15
print(list_sum([10, 20, 30]))      # 60
print(list_sum([]))                # 0