# What is a Data Type?
# Data type tells the kind of data stored in a variable.
# Without quotes Python thinks it is a variable name.
# With quotes it becomes a string.

# ==============================
# Python Data Types Example
# ==============================

# 1. String (str)
name = "Mohd Tasleem Khan"

# 2. Integer (int)
age = 27

# 3. Float (float)
height = 5.8

# 4. Boolean (bool)
is_student = True

# 5. List (list)
fruits = ["Apple", "Banana", "Mango"]

# 6. Tuple (tuple)
colors = ("Red", "Green", "Blue")

# 7. Set (set)
numbers = {1, 2, 3, 4, 5}

# 8. Dictionary (dict)
student = {
    "name": "Tasleem",
    "age": 27,
    "state": "Uttar Pradesh"
}

# 9. None Type
data = None


# ==============================
# Printing Values
# ==============================

print("String:", name)
print("Integer:", age)
print("Float:", height)
print("Boolean:", is_student)
print("List:", fruits)
print("Tuple:", colors)
print("Set:", numbers)
print("Dictionary:", student)
print("None Type:", data)


# ==============================
# Printing Data Types
# ==============================

print("\n----- DATA TYPES -----\n")

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(fruits))
print(type(colors))
print(type(numbers))
print(type(student))
print(type(data))