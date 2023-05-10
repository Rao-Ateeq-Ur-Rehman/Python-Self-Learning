#This is to use all math functions in python
from math import*


a = 10
print(a)
b = 50
c = a+b
print(c)
#Constants are defined using first capital letter
D = c
print(D)

string =  "Hello world"
print (string)

string = "Hello: "
print (string)

ali, usman, arqam = 10, 20, 30

print(ali, usman, arqam)

name, age = "Ateeq", 20
print(name, age)

#Remember it
print("Waao "+ string + name)

#Boolean
boolean = True
print(boolean)

#String Methods

if boolean:
    #Upper will convert small characters into capitals
    print("kya baat hai bonus ki".upper())

    #isupper(): this will return true/false if all letters are in capital or not
    print("kya baat hai bonus ki".upper().isupper())
else:
    #lower will convert all capital letters to small
    print("bekAaar hAi".lower())

    #islower(): this will return true/false if all letters are in small or not
    print("bekaar hai".islower())

sentance = "All To Hello To All"
#len(var_name): This will tell the length of the string 
print(len(sentance)) 
print(len("sentance"))

#.replace(target, replacement): This will replace the trgeted word in all the places & it's case-sensitive
print(sentance.replace("All", "You"))

#.index(Target): This will return the index of the found word will give error if not found
print(sentance.index("To"))

# \n: this will take the sentence to next line
print("Hello To \n All")


#Number Methods
#NOTE: In python you can't concatenate a number & string
# str(variable_name): this will convert number variable into string
age = 50
print("My age is: " + str(age))

#max(array/numbers): This will return the max number
print("Max Number is: " + str(max(1, 50, 800, 50, 60)))


#min(array/numbers): This will return the min number
print("Min Number is: " + str(min(1, 50, 800, 50, 60)))

#round(Number/variable): This will round the number or varibale
print(round(52.27))

#ceil(): This will always rounds up the value
print(ceil(52.27))

#floor(): This will always rounds down the value
print(floor(52.27))

#input : This will take input from the user and it's in string
#firstNum= input("Enter 1st Number: ")
firstNum= 10
#secondNum= input("Enter 2nd Number: ")
secondNum= 20

#float(variable_name): This will convert string into num
total = float(firstNum) + float(secondNum)
print("Total is :" + str(total)) 

#functions
def add(num1, num2):
    print("Function Total: " + str(num1 + num2))

add(50, 60)

def allDetails():
    name = input("Your Name: ")
    email = input("Your Email: ")
    number = input("Your Number: ")
    return("Your Name is: " + name + " Your email is: " + email + " Your Num is: " + number)
#print(allDetails())

#And , OR in If else

boolean = True
boolean2 = False

#AND
if boolean and boolean2:
    print("Both are true")
else:
     print("One of them or both Not true")

#OR
if (boolean or boolean2):
    print("One of them or both are true")
else:
     print("Both are Not true")

#elif: This is if else-if else 
if(boolean):
    print("Boolean 1 is true")
elif(boolean2):
    print("Boolean 2 is true")
else:
     print("Both booleans are Not true")

#not: This will reverse the condition
print("NOT")
boolean = False
if not (boolean):
    print("Boolean 1 is true")


#list: Its an array in python
list1 = [1, 5, 10, 15, 20]
print(list1)
print(list1[1])

#this the method to get elements of few certain indexes & this will not include last index
print(list1[1:3]) #[5, 10]
print(list1[1:]) #[5, 10, 15, 20]
print(list1[-2:]) #[15, 20]
print(list1[-2:-2]) #[]


list1 = [1, 5, 10, 15, 20]
print(list1)

if(len(list1)>5):
    #This'll insert element at given index
    list1.insert(0,"Good")
else:
    list1.insert(0,"Bad")

#this'll empty the whole list
#list1.clear()
print(list1)

list2 =["ateeq", "usman", True, "usman", "usman"]
#This will merge two lists into one
#list2.extend(list2) This'll repeat the list
list2.extend(list1)
print(list2)

#count: This will count the repeated elements & it's case sensetive
print(list2.count("usman"))


#This concept tells the us the premitive data type
li1 =["a", "b", "c", "d"]
li2 = li1
li2[0] = 1
print(li2)
print(li1)

#copy: this'll not affect any strings
random = li2.copy() + li1.copy()
print(random)

random[0]= "abc"
print(random)

#tuples: these are same as lists but you can't modify them
#this is list
colors = ["red", "green", "blue"]
print(colors)
colors.insert(0,"white")
print(colors)

#this is tupel
colors = ("red", "green", "blue", "yellow")
print(colors)
#colors.insert(0,"white") This'll give error

# dictionary: works like objects in js it's key value pairs

colors = {
    "black" : 222,
    "white" : 1111,
    "green" : 2222,
    "yellow" : 3333
}

#this will get the value & returns none if it doesn't finds the value
print(colors.get("black"))

#this will also get the value & returns second word if it doesn't finds the value
print(colors.get("blacK","Not found"))

#while loop
var1, var2 = 10, 20

while var1 <= var2 : 
    print(var1)
    var1 = var1+1

#For Loop
colors = ("red", "green", "blue", "yellow")
for i in colors:
    print("color is :", i)

#For Loop with string
clr = "Brown"
for i in clr:
    print("Brown color :", i)

#For Loop with string
for i in "Brown":
    print("Brown color :", i)

#For loop in range
for i in range(10, 20):
    print(i, " Number")

#Nested loops
meal = ["pizza", "burger", "sandwich"]
drink = ["water", "cola", "juice"]
desert = ["sweet", "donut", "cake"]

#This'll print all possible combinations    
for m in meal:
    for d in drink:
        for ds in desert:
            print("My meal will be: "+ m + " drink will be: " + d + " & desert will be: " + ds)

#Classes
class Students: 
    def __init__(self, name, rollNo, age):
        self.name = name
        self.rollNo = rollNo
        self.age = age

student1 = Students("Ateeq", "41", "60")

print(student1.age, student1.rollNo)