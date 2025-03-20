nested_list = [1, 2, [3, 4], 5]
sublist = [6, 7, 8]

nested_list[2].extend(sublist)
print(nested_list)
