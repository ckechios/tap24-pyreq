# Collections in Python

a = [1,2,"Three", 4.12]
b = {
    "id": 1234
}

print(a, type(a))
print(b, type(b))

# Access patterns for the data types
#    0 1 2
a = [1,2,"Three", 4.12]

print("Element 1:", a[0])
print("Element Last:", a[-1], a[3])

print("Slice a list:", a[1:3], type(a[1:3]))

print("-" * 10)
for el in a:
    print(el)

# Dictionaries
# {}
# { key1 : value1 , key2 : value2 }
print("----- Dictionary -----")
b = {
    "id": 1234,
    "name" : "John",
    "hobbies" : ["reading", "travel"],
    "email" : {
        "em1": "john@em.com",
        "em2": "j@em.com"
    }
}

print(b["name"])
k = "id"
print(b[k])

# id = 1234 - <datatype>
# name = John - <datatype>
# ....
print("---- Looping dictionary ---")
for el in b:
    print(el,"=", b[el], type(b[el]))

print("--- Access dict in dict ---")
print("Email 2:", b["email"]["em2"])