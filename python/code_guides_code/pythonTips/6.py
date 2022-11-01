from itertools import count


my_dict = {"item": "football", "price": 10.00}
# count = my_dict["count"] key error
print(count)

my_dict = {"item": "football", "price": 10.00}
count = my_dict.get("count")
print(count)

count = my_dict.setdefault("count",0)
print(count)
print(my_dict)