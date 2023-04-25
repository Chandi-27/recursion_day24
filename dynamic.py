f(n){
    if n<=10:
    return
    print(n-1)
    f(n-1)
    print(n-1)
}
#time complexity - linear
#f(13)-->output=12 11 10 10 11 12 

#fibonacci using recursion
def fib(n):
    if n<=0:
        return -1
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))

def fibon(a,b,n):
    if n<=2:
        return
    print(a+b,end=" ")
    c=a+b
    a=b
    b=c
    fibon(a,b,n-1)
print(0,1)
fibon(0,1,10)

#sum of nth fibonacci num
def fibo(n):
    if n<=0:
        return -1
    if n==1:
        return 0
    if n==2:
        return 1
    first,second=0,1
    result=first+second
    for i in range(0,n-2):
        next=first+second
        result+=next
        first=second
        second=next
    print(result)
fibo(10)

arr=[1,2,3,1,4,2,5,3,7,5]
my_set=set(arr) 
print(my_set)
for ele in my_set:
    print(ele,end=" ")
#typecasting an array into set
#set is an unordered so it do not allow duplicate values
my_set.add(50)
my_set.clear()
my_set.copy()

#dictionaries
#creating a dictionary
my_dict={
    "name":"chandi",
    "age":20,
    "occupation":"astronout"
} 
print(my_dict)
print(type(my_dict))
print(my_dict["name"])
#updating the name in a dict
my_dict["name"]="chandi priya"
print(my_dict["name"])
#another method to update name
updated_name={
    "name":"Bhuma Chandi Priya"
}
my_dict.update(updated_name)
print(my_dict["name"])

#object oriented programming
#how to create a class
class Car:
    engineType = "strongest Engine"
    numberOfTyers = 4
    numberOfWindow = 6
    isFridgeAvailable = True
    def getNumberOfWindows(self):
        return self.numberOfWindow
    def getNumberOfTyres(self):
        return self.numberOfTyers
car1=Car()
print(car1.getNumberOfWindows())
print(car1.getNumberOfTyres())
