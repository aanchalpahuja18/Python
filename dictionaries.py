# Dictionaries

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# 1. get()

print(capitals.get("India"))

#2. update()

print(capitals.update({"USA" : "America"}))
print(capitals.update({"Maharashtra": "Mumbai"}))

#3. pop()

print(capitals.pop("USA"))

#4. popitem()

print(capitals.popitem())

#5. keys()

print(capitals.keys())

#6. values()

print(capitals.values())

#7. items()

for key, value in capitals.items():
    print(f"{key} : {value}")

#8. clear()

print(capitals.clear())