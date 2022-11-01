from collections import Counter

my_list = [10,10,10,5,5,2,9,9,9,9,9,9]
counter = Counter(my_list)

print(counter)
print(counter[10])
print(counter[777])

most_common = counter.most_common(1)
print(most_common)

most_common = counter.most_common(1)
print(most_common[0][0])
