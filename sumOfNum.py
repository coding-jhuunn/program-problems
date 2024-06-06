num = int(input("enter your number"))


sum = 0
totalSum=0
for i in range(0,num+1,1):
    sum = i + i
    totalSum+=sum
    print(i ,i, sum)


print(totalSum)