# Example 1--  json.laod()-- it work with a file.


import json

# write file/create file (data.json)
with open("data.json", "w") as file:

    json.dump({"Name": "John",
               "age": 25}, file)

# Read json

with open("data.json", "r") as file:
    data=json.load(file)

print(data)

# Append/update data

with open("data.json", "r") as file:
    data=json.load(file)
data["age"]= 35

# Update data back to file.
with open("data.json", "w") as file:
    json.dump(data, file)
print(data)