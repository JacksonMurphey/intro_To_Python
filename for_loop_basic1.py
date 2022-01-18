#1) Basic 
#print all intergers 0 to 150

add = 0
while add <= 150:
    print(add)
    add += 1


#2) Multiples of Five
#print all the multiples of 5 to 1,000. 

for x in range(5,1001):
    if x % 5 == 0:
        print(x)

# #OR
count = 5
while count <= 1000:
    if count % 5 == 0:
        print(count)
    count += 1


#3) Counting, the Dojo Way:
#print integers 1 to 100. If divisible by 5, print 'Coding' instead. if divisible by 10, print 'coding dojo'.

# This one will print the integer and Coding/Coding Dojo.. not what I want. 
for x in range(1,101):
    print(x)
    if x % 5 == 0:
        print("Coding")
    if x % 10 == 0:
        print("Coding Dojo")

#OR

# This one will print integers that are divisible by 5, but not the ones divisible by 10. prints coding/coding dojo though. 
x = 1
while x <= 100:
    if x % 5 == 0:
        print("coding")
    
    if x % 10 == 0:
        print("coding dojo")
    else: 
        print(x)
    x += 1
# cannot seem to figure out how to get it to skip printing integers where x % 5 == 0 is true. 


#4) Whoa. That Sucker's huge. 
#add odd integers from 0 to 500,000 and frint final sum
oddsum = 0
for x in range(0, 500001):
    if x % 2 != 0:
        oddsum = oddsum + x

print(oddsum)


#5) Countdown by fours. 
#print positive numbers starting at 2018, counting down by 4

start = 2018
end = 0
while end < start:
    start -= 4
    print(start)
    if start == 2:
        break


#6) Flexible Counter 
#Set 3 variables: lowNum, HighNum, mult. from lowNum thru highNum, print only the integers that are a multiple of mult.

lowNum = 1
highNum = 50
mult = 4
while lowNum <= highNum:
    if lowNum % mult == 0:
        print(lowNum)
    lowNum += 1
