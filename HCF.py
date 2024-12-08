#HCF
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

if n2>n1:
    n1,n2=n2,n1
#now n1 is greater than n2

while n2 is not 0:
    r=n1%n2
    n1=n2
    n2=r
print("The HCF of the numbers is ",n1)
