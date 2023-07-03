fibo=[1, 2]
sumf=0
while True:
    if(fibo[-1]<=4e6):
        fibo.append(fibo[-1]+fibo[-2])
    else:
        break
for i in range(1,len(fibo),2):
    print(fibo[i])
sumf = sum(fibo)
print(f'Sum of fibo =',sumf)