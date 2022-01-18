# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Jackson"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 11
print("Hello,", name, "is my favorite number")	# with a comma
print("Hello, " + str(name) + " is my favorite number")	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "ramen"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

print (len(fave_food2))
print (fave_food2.capitalize())
print (fave_food2.find("z"))
fave_foods = fave_food1 +" and "+ fave_food2
print(fave_foods)
num = 25
num1 = "25"
total = num + int(num1)
print(total)