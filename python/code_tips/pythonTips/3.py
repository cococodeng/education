data = [3,4,1,5,6,76,7]
sorted_data = sorted(data, reverse=True)

print(sorted_data)


data = [{"name": "Max", "age": 6},
        {"name": "Lisa", "age": 20},
        {"name": "Ben", "age" : 9}]

sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)


data = [{"name": "Max", "age": 6, "height": 120},
        {"name": "Lisa", "age": 20, "height": 130},
        {"name": "Ben", "age" : 9, "height": 110}]

sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)

sorted_data = sorted(data, key=lambda x: x["height"])
print(sorted_data)

