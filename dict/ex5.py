dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]
new_dict = {key: dict[key] for key in keys if key in dict}

print(new_dict)