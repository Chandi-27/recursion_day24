#def add():
#   a=10
#    b=20
#   print(a+b)
#add()

"""def add():
    a=input()
    b=input()
    print(a+b)
add()
#it will aks the user to enter the input and the given inputs will be concatenated.

def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()

def add():
    try:
        a=input()
    except ValueError as err:
        print(err)
    try:
        b=input()
    except ValueError as err:
        print(err)
    print(a+b)
add()

def addNumbers():
    a=10
    b=20
    return (a+b)
sum=addNumbers()
print(sum)

def addNumber(a,b):
    return a+b
sum=addNumber(50,60)
print(sum)

def returningMultipleValues():
    return 10,20,30

output = returningMultipleValues()
print(output)

def chandi(a,b):
    return a*b
a=20
b=90
x=chandi(a,b)
print(x)

def fibonacci(n):
    f1=0
    f2=1
    print(f1,end=" ")
    print(f2,end=" ")
    f3=f1+f2
    print(f3,end=" ")
    while n>=4:
        f3=f1+f2
        f1=f2
        f2=f3
        print(f1+f2,end=" ")
        n=n-1
n=int(input())
fibonacci(n)

#lcm & hcf

def doJob(n):
    if n<=2:
        return
    print(n)
    doJob(n-1)
    print(n)
doJob(10)"""

def doJob2(n):
    if n<=5:
        return
    doJob2(n-1)
    print(n)
    doJob2(n-1)
    print(n)
doJob2(8)