# -*- coding: utf-8 -*-
num1=100
num2=100
if(num1>num2):
    print("Num1 is greater than Num2")
elif(num1==num2):
    print("Num1 and Num2 are equall")
else:
    print("Num1 is less than Num2")
print("iam not part of if else")
    
#Input and check
std = int(input("Enter the value"))
if(std==1):
    print("Value is 1")
elif(std==2):
    print("you are in 2nd Standard")
elif(std==3):
    print("you are in 3rd standard")
else:
    print("you are in other than above standards")
    
#while
start=1
end=10
while(start < end):
    print(start)
    start =start+1

#for
for i in range(10):
    print(i)

for i in range(10,20):
    print(i)

for i in range(10,30,2):
    print(i)
for i in range(20,10,-1):
    print(i)

#looping
def sum(num1,num2):
    result=num1+num2
    print("Result",result)
sum(20,30)

#function
def sum(num1,num2):
    result=num1+num2
    return result
result=sum(60,50)
print("Result",result)
