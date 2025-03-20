dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]

for key in keys:
    dict.pop(key, None)

print(dict)