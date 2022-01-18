num1 = 42 # variable declaration, primitive numbers
num2 = 2.3 # variable declaration, numbers, would possibly need to float to get the decimals at least in python2 
boolean = True # data type primitive, boolean
string = 'Hello World' # date type primitive, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, intialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, intialize dictionary 
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, intialize tuple 
print(type(fruit)) #log statement, composite type check, type = tuple 
print(pizza_toppings[1]) #log statement, composite list, access value
pizza_toppings.append('Mushrooms') # call variable to add value, much like .push()
print(person['name']) #log statement, composite dict.  key name, access value/definition 
person['name'] = 'George' #data type composite, dictionary, access value, chance value
person['eye_color'] = 'blue' #date type compsite, dictionary, add value (key:definition)
print(fruit[2]) #log statement, composite tuple, access value index

if num1 > 45: #conditional if
    print("It's greater") # log statement
else: # conditional else 
    print("It's lower") # log statement 

if len(string) < 5: #conditional if, length check string = 11 
    print("It's a short word!") # log statement 
elif len(string) > 15: # conditional else if, length check sting= 11 
    print("It's a long word!") # log statement 
else: #conditional else
    print("Just right!") # log statement 

for x in range(5): # for loop, stop value 
    print(x) # log statement 
for x in range(2,5): # for loop, start value, stop value 
    print(x) # log statement 
for x in range(2,10,3): # for loop, start value, stop value, step size(increment)
    print(x) # log statement 
x = 0 #variable declaration, primitive number
while(x < 5): # while loop, start, stop
    print(x) # log statement  
    x += 1 # increment 

pizza_toppings.pop() # call variable list to remove last value, composite list delete value 
pizza_toppings.pop(1) # call variable list to remove index value[1]. composite list deliver value index 1 
print(person) # log statement, call person dictionary 
person.pop('eye_color') # call person dictionary to remove key eye_color and its value/def. 
print(person) # log statement 

for topping in pizza_toppings: # for loop call list pizza toppings 
    if topping == 'Pepperoni': # conditional if statement: toppings is equal to pepperoni 
        continue # continue, we can stop the current iteration of the loop, and continue with the next 
    print('After 1st if statement') # log statement 
    if topping == 'Olives': # conditional if statement: toppings equal to olives 
        break # break exit the loop after the above conditional if statement elvalutes to true. 

def print_hello_ten_times(): # def keyword, letting us know we are creating/naming a function. with no parameter set. 
    for num in range(10): # for loop. stop value 10
        print('Hello') # log statement for each iteration 

print_hello_ten_times() # calling our function with no argument given 

def print_hello_x_times(x): # def keyword, naming our funciton. with a parameter x, variable declaration that is not defined yet. 
    for num in range(x): # for loop, stop value = x 
        print('Hello') # log statement 

print_hello_x_times(4) # calling our function, passing the argument that x=4. 

def print_hello_x_or_ten_times(x = 10): # def keyword, naming our function. with a default parameter of x=10, if we call the function without an argument it uses the default value. 
    for num in range(x): # for loop
        print('Hello') # log statement 

print_hello_x_or_ten_times() # calling our function, passing no argument, thus it will use the defualt parameter. 
print_hello_x_or_ten_times(4) # calling our function, passing the argument that x=4. thus it will not use the default parameter. 


""" 
Muiltiline comment 
Bonus section
"""
"""
print(num3) # NameError, num3 is not defined
num3 = 72 # variable dclaration, but since its after we call to print, the above line doesnt print due to nameError. 
fruit[0] = 'cranberry' # TypeError, fruit is a tuple object. tuples are unchangeable, thus it does not support item assignment. 
print(person['favorite_team']) # KeyError, raised when dictionary key is not found within the existing keys. log statement
print(pizza_toppings[7]) # IndexError. sequence index isnt defined/is out of range. log statement. 
 print(boolean) #IndentationError, subclass of SyntaxError. 
fruit.append('raspberry') #A ttributeError, tuple has no attribute for append. tuples are unchangeable.
fruit.pop(1) # AttributeError, tuple has no attribute for pop. tuples are unchangeable. 
"""