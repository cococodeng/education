data = [1,2,3,4,-4]

for i in range(len(data)):
    if data[i]<0:
        data[i]=0

print(data)

data = [1,2,-4,-3]
 
for indx, num in enumerate(data):
    if num < 0:
        data[indx] = 0
        
print(data)