# from BinaryTree import Node
from collections import deque
#Swap variable
a = 10
b = 20
print(a, b)
a,b = b,a
print(a, b)

#Scope variable: Local variable is defined inside the function block and global is declared outside the block

var1 = 50

#if we remove global then this will give error because var1 is outside the block 
def test():
    global var1 
    var1 = var1 + 50
    print("var1 inside the block: ", var1)
test()
print("var1 outside the block: ", var1)

#assert: allows us to verify that our code works as our expectations

a= 50

assert a == 50 #work fine 
assert a >= 50 #work fine 
# assert a > 50 will give error

#string formatting:
txt = "For only {price} dollars!"
print(txt.format(price = 49))

#this will tell the type of data
print(type(txt))


# is None: This will check if the var value has value none or not
var = "abc"
print(var is None) #False

var = None
print(var is None) #True

var = "white"
print(var is not "white") #False

var = "white"
print(var is not "green") #True

#for loop
for p in range(1,7):
    print(p)

var = 5
while(var < 10):
    print (var)
    var = var + 1

#Break
for p in "python":
    if(p == "o"):
        break
    print(p)

#Continue
for p in "javascript":
    if(p == "r"):
        continue
    print(p)

#Nested For Loop
for num in range(3):
    for num2 in range(5,7):
        print(num, " , ", num2)


#Nested While Loop
var = 1
var1 = 5

while(var < 5):
    while(var1 < 10):
        print(var, " + ", var1)
        var1= var1+1
    var = var + 1

#Else with loop
var = 1
while(var < 5):
    print("While with else " , var)
    var = var + 1
else:
    print("While Loop completed")

#slicing
str = "Hello world"
s1 = slice(2,9) #llo wor
print(str[s1])
s2 = slice(-7 , -2)
print(str[s2]) #o wor

#append: 
list = [10, 20, 30, 40, 50]
print(list)
list.append(1000)
print(list)

#remove
list.remove(30)
print(list)

print("POP ", list.pop())
print(list)

list1 =["c++", "Js", "dart", "python"]

# for p in range(5):
#    list1.append(float(input("Enter a value: ")))

print(list1)
#print(max(list1))

queue = deque(["c++", "Js", "dart", "python"])
print(queue)
queue.append("php")
print(queue)
queue.appendleft("ruby")
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)


newList = list + list1

print(newList)

#dictonary
dict = { 
    "car" : "BMW",
    "model" : 2020
}
print(dict)

dict2 ={
    "car" : "Ford"
}

#dictionary update
dict.update(dict2)
print(dict)

#dictionary concat
dict3 = {
    "engine" : "Petrol",
    "engine2" : "Petrol",
    "engine3" : "Petrol",
    "color" : "white"
}

dict3.update(dict)
print(dict3)

#delete in dictionary
del dict3["color"]
print(dict3)

#clear: this will empty the whole dictionary
# dict3.clear()
# print(dict3)

#del: this will del the whole dictionary
# del dict3
# print(dict3)

# len() : This will give the length of the dictionary and will not include repeated value
print(len(dict3))

# set : same like lists but doesn't contains repeated values
set1 = set([1, 2, 3, 4, 5, 5, 6, 8])

print(set1)
print(len(set1)) #7

set1.add("Hello")
print(set1)


#pop from dictionary
print(dict3)
dict3.pop("car") #this will remove specified item 
print(dict3)

dict3.popitem() #this will remove the last item from dictionary
print(dict3)

#Nested Loop
list =[[1,2],[3,4],[5,6],[8,9,10]]
print(list)

for l in list:
    for ll in l:
        print(ll)

#Try & Except
try:
    # text= input("Enter some value")
    text= print("Enter some value")
except EOFError:
    print("EOFError")
except ValueError:
    print("ValueError")
else:
    print("worked Fine")
    
# raising exceptions: you can raise exceptions yourself

a = 123
if(type(a) is int):
    print("Good int value")
else:
    raise TypeError("You didn't entered int value")


#try except finally, finally will run in all scenerios 
try:
    print("bb")
except:
    print("something isn't good")
finally:
    print("I'll run anyway")

#zerodivision error
try:
    # a = int(input("enter a numenator "))
    a = 10
    # b = int(input("enter a denumenator "))
    b = 2
    print(a/b)
except:
    print("Enter a valid number")


#OOOPPP
# class
class car:
    company = "Honda"
    model = 2013

#object of class
c = car()
print("company ", c.company," model ",c.model)

#another example
class bike:
    def __init__(self, company, model, engine):
        self.company = company
        self.model = model
        self.engine = engine

# this is object of the bike class
newBike = bike("honda", 2020, 700)

print("Company: ",newBike.company, ", model: ",newBike.model," , engine: ", newBike.engine)

newBike = bike("yamaha", 2022, 1700)

print("Company: ",newBike.company, ", model: ",newBike.model," , engine: ", newBike.engine)

#pass: this allows to create an empty class for later usage

class animal: 
    pass

lion = animal()
lion.age = 10
lion.color = "brown"
lion.weight = 80

print(lion.age , lion.color, lion.weight)

#instance method
class student:
    def __init__(self, fname, lname, rollno, clas):
        self.fname = fname
        self.lname = lname
        self.rollno = rollno
        self.clas = clas

    #this is instance method
    def details(self):
        print("Name: ",self.fname+" "+self.lname,", Roll Num: ",self.rollno, ", class: ",self.clas)
    
student1 = student("Ali","usman", 30, "9th")
student1.details()

student2 = student("salman", "ali", 60, "10th")
print(student2.fname , student2.lname, student2.clas, student2.rollno)

student2.details()
#this will delete the element in object
del(student2.fname)
# student2.details() this will give error 
# print(student2.fname , student2.lname, student2.clas, student2.rollno) now this'll give error

#get attribute : this'll get the attribute
print(getattr(student2,"lname"))

# has attribute : this'll return true/false if attribute exists or not
print(hasattr(student2,"fname")) #false
print(hasattr(student2,"lname")) #true

# set attribute : this'll set the attribute if it doesn't exits and will update it if it founds the element
print(setattr(student2,"fname","sallu"))
print(getattr(student2,"fname"))

# delete attribute : this'll delete the attribute
delattr(student2,"fname" ) 
# print(getattr(student2,"fname"))


#INHERITANCE
# parent class
class parent:
    nameParent = ""
    ageparent = ""

    def show(self):
        print("Parent: ", self.nameParent, " ", self.ageparent, "child is: ")

class child(parent):
    nameChild =""
    def showChild(self):
        print("Child: ",self.nameChild, " Parents: " , self.ageparent," ",self.nameParent)

c =child()
c.nameParent = "GOGA"
c.ageparent = 50
c.nameChild = "albela"
c.show()
c.showChild()


x = 5
print (x)

y = int(5)
print(y)

x = " Hello "
x.strip()
print(x)


#Method Overriding: we can create 2 functions with same name but they will perform different tasks
class cars: #Parent Class
    def __init__(self):
        self.carName = "BMW"
    def prin(self):
        print(self.carName)

class bmw(cars):
    def __init__(self):
        self.carValue = "BMW CAR VALUE"
    def prin(self):
        print(self.carValue)

c = cars()
c.prin()

c1 =bmw()
c1.prin()


# Getter & Setter
class employee():
    def __init__(self) :
        self.job = "none"
    def getJob(self):
        return self.job
    
    def setJob(self,job):
        self.job = job
    
firstEmployee = employee()

print(firstEmployee.getJob())

firstEmployee.setJob("Designer")

print(firstEmployee.job)


#super: Allows you to call method of super/parent class into child class
class A:
    def method(self):
        print("I am super/parent class")

class B(A):
    def method2(self):
        print("I am child class")
        super().method()    

objectOfClass = B()
objectOfClass.method2()

# lambda : This is method of writing short function
a = lambda b: print("Ek ka double, ", b+b)

a(50)


#filter
# def abc(a):
#     if a>5:
#         return a

# c = filter(abc,(5,2,10,1))
# print(list(c))