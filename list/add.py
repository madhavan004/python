items = [10, 20, 30, 40, 50]
target = 30
new_item = 35

index = items.index(target) + 1
items.insert(index, new_item)
print(items)
