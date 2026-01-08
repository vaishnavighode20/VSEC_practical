n=int(input("Enter no. "))
num=0
while n>0:
    digit=n%10
    num=num*10 + digit
    n=n//10
print(num)