numbers = [1, 2, 3, 4, 5]
old_value = 3
new_value = 99

numbers = [new_value if x == old_value else x for x in numbers]
print(numbers)
