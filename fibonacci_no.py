#  Python Program for Fibonacci numbers
#function defination

no = int(input("enter the number :"))
a=0
b=1

print(a)
print(b)

if no==1:
        print(a)
else:
    for i in range(0,no):
            sum=a+b
            a=b
            b=sum
            print(sum)





