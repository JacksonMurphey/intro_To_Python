1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Will return 5. 

# NOTE: my prediction was correct. 

2
def number_of_military_branches():
    return 5 
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Thought initially we would either get an error due to an undefined function, (or a return of 5) 
# Upon seeing Question 9, the answer should be: 8 

# NOTE: I was correct on my initial thought of this returning an Error code. So unlike JS, even though we later define the function(number_of_days_in_a_week_silicon_or_triangle_sides(), Python produces a NameError, and states this function is not defined. 

3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# returns 5. -- a return ends a function or loop. 

# NOTE: my prediction was correct

4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# returns 5. -- print(10) is after the call to return 5, so it doesnt print. 

#NOTE: my prediction was correct

5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# prints 5. we set the function equal to a variable, then print that variable. 

#NOTE: my prediction was correct

6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# prints 8. (do not believe it would print 3 and 5 then add them and then print.)

# NOTE: I was incorrect. The way it is written produces a TypeError: unsupported operand +:'NoneType' and 'NoneType'
# will have to mess around with this to see how we could get it to work.

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# returns "7"

# NOTE: I didnt fully think this one through.. Since we created a string, then added the strings together, we were no longer adding the values together, we were adding the strings. Thus the result is: 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#prints 100, returns 10 (my answer here, makes me look back at ?6...)

# NOTE: my prediction was correct, even though I started to second guess myself. 

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# 7
# 14
# 21
# (upon seeing this question, I am updating my prediction to ?2)

# NOTE: my prediction was correct


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# outcome is 8.  (though, if no arguments are passed, maybe it returns 10 as the default. I am confident the answer is 8 since arguments are passed and since the computer should stop reading once return is called. if no arguments were passed, we would get an error I believe)

#NOTE: my prediction was correct as far as the outcome being 8. will check to see if my assumptions were correct after.


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#print(b) 500
#print(b) 500
#foobar() 300
#print(b) 500

#NOTE: my prediction was correct


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#print(b) 500
#print(b) 500
#foobar(): print(b) 300, returns 300
#print(b): 500

#NOTE: my prediction was correct, but not entirely, I thought it would print b and return b. ( After reviewing the correct answer, I commented out print(b) within the function foobar(). Now when I call the function, even though we set b=300, then said return b, with print(b) commented out, I do not get (return b) printed to my terminal, nor do I get the variable b, nor does it update the value of b when we call to print it after we call the function... interesting. so I guess techincally, its only printing b with its new value in the funtion and not returning... Ill have to look further into this.)
#NOTE: NOTE: so I initially checked my answer in the terminal on VScode. Pretty sure we were told that was not the best way to do this and to instead, use your terminal application(iTerm, on MacOS). So with the confusion I had as to why I was seeing the results I had, I typed out the whole question in iTerm. Sure enough, I got the exact answer I had predicted. Then I commented out print(b) within the function, and It gave me the return b = 300. So I guess the lesson here is, avoid VScode terminal. 



#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#print(b) 500
#print(b) 500
#b=foobar() -- we have now changed the value of variable b to equal the function. 
#print(b) prints 300, returns 300

#NOTE: my prediction was correct (after reviewing the answer to ?12, I am slightly confused as to why i was correct. is it solely due to us setting the value of b equal to the function? now when I comment out print(b) in the function, unlike in ?12, it returns the functions value of b, 300.) NOTE: see note note, on ?12. I am no longer confused. 


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# prints 1
# calls bar() and prints 3
# prints 2

#NOTE: my prediction was correct 


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# prints 1
# x = bar() thus, print(x) = print 3, return 5
# returns 10

#NOTE: my prediction was correct 