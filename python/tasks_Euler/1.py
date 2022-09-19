def move_zeros(array):
    zeroes=0
    if array.count(0)!=0:
        while array.count(0)!=0:
            array.remove(array[array.index(0)])
            zeroes=zeroes+1
    array = array + [0]*zeroes
    return array


print([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([]))