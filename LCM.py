#LCM
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))

if n2>n1:
    n1,n2=n2,n1
#now n1 is greater than n2

lcm=n1
while lcm%n1 is not 0 or lcm%n2 is not 0:
    lcm+=n1
print("LCM of the two numbers is ",lcm)
