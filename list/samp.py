list1 = ["A", "B", "C"]
list2 = ["1", "2", "3"]

concatenated = [a + b for a, b in zip(list1, list2)]
print(concatenated) 