# Dictionaries: Creating, Accessing, and Modifying

# 1. Creating Dictionaries
# Using curly braces
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using the dict() constructor
car = dict(brand="Toyota", model="Corolla", year=2020)

print("Person Dictionary:", person)
print("Car Dictionary:", car)

# 2. Accessing Values
print("Name:", person["name"])          # Accessing using key
print("City:", person.get("city"))       # Using get() method

# Accessing a non-existent key using get() returns None
print("Country:", person.get("country", "Not specified")) # Provide default value

# 3. Modifying Dictionaries
# Adding a new key-value pair
person["job"] = "Engineer"
print("After adding job:", person)

# Updating an existing key
person["age"] = 26
print("After updating age:", person)

# Removing a key-value pair
removed_value = person.pop("city")
print("After removing city:", person, "| Removed Value:", removed_value)

# Using del to remove a key
del person["job"]
print("After deleting job:", person)

# Clearing all items
car.clear()
print("After clearing car dictionary:", car)

# 4. Iterating Through Dictionaries
# Iterating over keys
print("Keys:")
for key in person.keys():
    print(key)

# Iterating over values
print("Values:")
for value in person.values():
    print(value)

# Iterating over key-value pairs
print("Key-Value Pairs:")
for key, value in person.items():
    print(key, ":", value)

# 5. Dictionary Methods
# Checking if a key exists
print("Is 'name' in person?:", "name" in person)

# Copying a dictionary
person_copy = person.copy()
print("Copied Dictionary:", person_copy)

# Merging dictionaries using update()
extra_info = {"hobby": "Painting", "pet": "Dog"}
person.update(extra_info)
print("After merging extra_info:", person)

# 6. Nested Dictionaries
nested_dict = {
    "Alice": {"age": 25, "job": "Engineer"},
    "Bob": {"age": 30, "job": "Doctor"}
}

print("Nested Dictionary:", nested_dict)
print("Alice's Job:", nested_dict["Alice"]["job"])
