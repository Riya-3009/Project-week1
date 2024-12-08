n=int(input("Enter the number of terms in the series: "))
fiblist=[0,1]
for i in range(0,n):
    fiblist.append(fiblist[i]+fiblist[i+1])
print(fiblist)
