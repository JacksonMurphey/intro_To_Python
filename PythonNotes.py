print("Hello World!")
x = "Hello Python"
print(x)
y = 42
print(y)


import random

print('Welcome to Python!')

print('This is a loop printing 5 times')
for x in range(1, 6):
    print(f'x is: {x}')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays)

print(f'Today is: {day}')

if day == 'Monday':
    print('It will be a long week!')
elif(day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')

int_to_float = float(35) # output is 35.0
float_to_int = int(44.9) # output is 44 /// when we convert a float to an int. it rounds down even from 44.9
int_to_complex = complex(35)  # output becomes (35+0j)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

import random
print(random.randint(2,5)) # prints a random integer between 2 and 5.
print(random.randint(0,10))
print(random.randrange(10))

name = 3
print("my name is", name)
# print("my name is " + name) #this will give you a TypeError becasue the cannot concatenate a string with an integer. 
# to fixed the aboce error, see below
print("my name is " + str(name))


#---String interpolation---
# F-strings 
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables # combines both lists into one list. 
print(fruits_and_vegetables)
salad = 3 * vegetables # will create a list, that repeats the vegetables list 3 times, in one new list. 
print(salad)

# this is a function to return the circumference and area of a circle, given the radius (r). 
def get_circle_area(r):
    c = 2 * 3.14 * r
    a = 3.14 * r * r
    return (c, a)
print(get_circle_area(5))


# ---Creating dictionaries---

weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

# Accessing values from dictionaries via their key.
print(weekend["Sun"])
print(capitals["svk"])

#removing values from dictionaries 
value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
del capitals['dnk'] # will delete the key, and not return anything

#Nesting Dictionaries: Dictionaries may contain lists and tuples 
context = {
    'questions': [
        { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer'},
        { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
        { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
        { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
} # Here we have a dictionary, nested inside it is a list, within the list is a dictionary.. 
print(context['questions'])
print(len(context))
print(str(context))
print(type(context))
print(weekend.values())


#---Conditional Statements in Python---
# if, elif, else 
# Operators: ==, !=, <=, >=, <, >, and, or, not

x = 12
if x > 50:
	print("bigger than 50")
else:
	print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute
    
x = 55
if x > 10:
	print("bigger than 10")
elif x > 50:
	print("bigger than 50")
else:
	print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

if x < 10:
	print("smaller than 10")
# nothing happens, because the statement is false   


#---For Loops in Python ---

#range(5) -- Stop
#default start: 0 :: 5-exclusize stop
#output: 0, 1, 2, 3, 4

#range(5,10) -- Start, Stop
#inclusive start: 5 :: 10-exclusive stop
#output: 5, 6, 7, 8, 9

#range(5,10,2) -- Start, Stop, Step(incrementing value)
#inclusive start: 5 :: 10-exclusive stop
#output: 5, 7, 9 (note: it is incrementing by 2. default step amount is 1.)

for i in range(0,20,2):
    print(i)

for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

#---For Loops through Strings---
for x in 'Hello':
    print(x)

#---For Loops through Lists---    
# if we want to iterate through a list, we could use the range function and send the length of the list as the stopping value, but if we are not interested in the index values and want to just see the values of each item in the list, in order, we can actually loop to get the values out fo the list directly. 

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i]) 
    #output: 0 abc, 1 123, 2 xyz
# OR
for v in my_list:      #note: v is used here to notate that we only want the values of each item. 
    print(v)
    #output: abc, 123, xyz

#---For Loops through Tuples---
#we can iterate through Tuples the same way we can iterate through a list. 

dog = ("Canis Familiaris", "dog", "carnivore", 12)
for data in dog:
    print(data)
    # output will be each value within the Tuple.

#---For Loops through Dictionaries--- 
#when we iterate through a dictionary, the iterator is each of the KEYS of the dictionary. 

my_dict = {"name": "Jackson", "language": "Python"}
for k in my_dict:
    print(k)
    #output: name, language 

# the above produces the KEY names of our dict. if we instead want the values, we could do something like... 
for k in my_dict:
    print(my_dict[k])
    #output: Jackson, Python 

#Dicts. also have a few additional methods that allow us to iterate through them and have the keys and/or values as the iterator. 

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}

# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia

#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond

#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc


#---While Loops---
#while loops are another way of looping, WHILE a certain condition is true.

#below is a for loop. 
for count in range(0,5):
    print("looping =", count)

#We can rewrite it as a WHILE loop:
count = 0
while count <= 5:  #since we have put count <= 5, five is included. whereas above 5 is an exclusive stop point. 
    print("looping - ", count)
    count += 1

# While Loop - With an Else statement. 
#there are certain conditions we give for every loop, but what if the condition was not met and we still would like to do somthing if that happens? We can use an ELSE statement with our WHILE loop. 

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")
    # output: 3, 2, 1, Final else Statement

    #NOTE: this else code is only executed if the WHILE loop runs normally and its conditional is false. If the WHILE loop is exited prematurely, b/c of a break or a return statement, then the else code block will never run. 

#---LOOP Control(flow)---
#when you want finer control over your loops, use the following statements to do so. 

#--Break statement--
#Break statement exits the current loop prematurely, resuming execution at the first post-loop statement. can be used for both FOR and WHILE loops. 
#The most common use for break is when some external condition is triggered, requiring a hasty exit from the loop. 
#When a loop is nested, a break will only exit from the innermost loop. 

for val in "string":
    if val == "i":
        break
    print(val)
    #output: s, t, r 
    #NOTE: When the loop got to the letter "i", the loop stopped. 

#--Continue statement-- 
#Continue statement immediately returns control to the beginning of the loop. In other words, the continue statement rejects, or skips, all the remaining statement in the current iteration of the loop, and continues normal execution at the top of the loop. 
#NOTE:Continue is very useful when you want to skip specific iteration(s), but still keep looping to the end. 

for val in "string":
    if val == "i":
        continue
    print(val)
    #output: s, t, r, n, g
    #NOTE: there is no "i" in the output, but the loop continued after the "i" as opposed to when we used BREAK. 

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:           # only executes on a clean exit from the while loop(i.e. not a break)
    print("Final else statement")
    #output: 3, 2, 1  --since the if statement became true, it executed the break statement and thus never ran else statement. 


#---Functions---
# function format:
# def <name of function> (parameters): parameters are our inputs.   
#           {instructions or logic in/for our function}
#           return --- this is what will be given back or "returned" once you call the function. 
#<function name>(arguments) --- now we are outside the function and calling/invoking it. 

# example:
def add(a,b):  # def lets the computer know we are about to create a function. <add> is the name of the function.        # (a,b) these are the parameters of our function, that can later be replaced when we call the function. 
    x = a + b  # this is what we want the function to do when its called. 
    return x   # this is what we want given back/returned to us after the function is called. 

add(3,4)    # this is us calling the function, and passing thru the arguments (3,4) to the parameters of the function. 
# when called, if will return x, which is the sum of a + b. 

#***Important***
#It is very important to remember the following: 
#a function call is equal to whatever that function returns.
# declaration | name | parameter | code block | return
def be_cheerful(name="Mr. Nibbles", repeat=2):
    print(f"Good morning {name}\n" * repeat) # \n is syntax for it to create a new line, when repeating..?

be_cheerful("Jackson")
be_cheerful()
be_cheerful(repeat =4, name="Benny Bob") #here, are arguments do not match the order or our parameters. To fix this, we stated what our arguments are, so that the computer knows which parameters they coorelate to. 
be_cheerful("benny bob", 4) # on this example, I simply made it so our arguments align with the order of our paramters and, boom. produces the same result. 


#---Learning to Debug---- 
def multiply(num_list, num):
    print(num_list, num) #1st step in debugging is to insert a call to print. doing this lets us know what values, if any, that are being passed to the function. upon printing we see the list and num are passed: [2,4,10,16] 5
    for x in num_list:
        #print(x) #2nd step: we want to confirm we have entered the loop, and that "x" contains the value we expext. upon printing to the terminal, we get: 2 4 10 16
        x *= num
        #print(x) #3rd step: lets check if we are successfully changing our x value. output is: num_list = num_list * 5.
        #print(num_list) #4th step: comment out above line and check to see if our list is changing when we expect it to. CHAN-CHING! We have identified where there is an error. X is a pointer to the value but its not updating our list. So how do we solve this. search google? "unable to modify list value in for loop python"  
    return num_list  #we want our return to update our list value. how do we do this? We need to update how we are applying our function to x and the values of the list. See below. 
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# [2,4,10,16] 5
# [2,4,10,16]


def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
#[10,20,50,80]



