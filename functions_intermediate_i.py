#1) Update Values in Dictionaries and Lists 

x = [ [5,2,3]   ,  [10,8,9] ] 
students = [
    {'first_name' :  'Michael', 'last_name' : 'Jordan'}   , 
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

# Change the last_name of the first student from 'Jordan' to 'Bryant'

# In the sports_directory, change 'Messi' to 'Andres'

# # Change the value 20 in z to 30

# def run_the_track():

#     x[1][0] = 15
#     print(x) 
    # students[0] ['last_name'] = 'Bryant'
#     print(students)
#     sports_directory['soccer'][0] = 'Andres'
#     print(sports_directory)
#     z[0]['y'] = 30
#     print(z)

# run_the_track()



# 2) Iterate Through a List of Dictionaries 
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
    {'first_name' :  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(lists):
#     for dic in students:
#         print(dic["first_name"], dic["last_name"])
#         # for key, value in dic.items(): --- line 46 and 47 werent needed though it did ultimately allow us to pull the key and the value. The above, line 45, was a quicker way to essentially do the same thing. 
#         #     print(f"{key} - {value}")
#             #(struggling to figure out how to get this to print both first and last on same line. I should review question 1, even though I was just printing the list of dict. it printed them on the same line. also, review question 4 since that too, is a dictionary with a list of keys and values. ) 
# iterateDictionary(students) 


#3) Get Values From a List of Dictionaries
#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 

# def iterateDictionary2(key_name, lists):
#     # return{k: [d.get(k) for d in lists]
#     # for k in set().union(*lists)} -----this will create a dictionary with a list of all values for each key. this only works for a list of dictionaries. 
#     for i, entry in enumerate(lists):
#         print (f"{i + 1}: {entry['first_name']}")  #(decided to make this a numbered list of names after i got the answer. enumerate gives back two loop variables, count and value. (for i, entry in enumerate(lists, start=1) this would have started i at 1 istead of zero. So I could have put start=1 instead of i+1 in print. )

#     # for i in range(0, len(list)):
#     #     for key, value in list[i].item():
#     #         if key == key_name:
#     #             print(value)

    
    

students = [
    {'first_name' :  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary2(key_name, lists):
#     for i, entry in enumerate(lists):
#         # print(lists[i]['first_name'])
#         if entry[key_name] == lists[i]['first_name']:
#             print (f"{i + 1}: {entry['first_name']}") 
#         else:
#             print (f"{i + 1}: {entry['last_name']}") 
        
# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

# initially I just had the for loop and print, which would only print the specific argument that was specifically called in the function to print. if the argument changed, I would have to then change this value in the function. So for question 3, you can see in the first function for the answer was how I originally did it prior to realizing my mistake. (i went back and added an if/else statement, where depending on the argument that we were requesting, we would get the desired result. )


#4) Iterate Through a Dictionary with List Values
#Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon'],
    "principle": "Terry"
}
michael = value[0] = "michael"
def printInfo(some_dict):
    # for i, entry in enumerate(dojo):
    #     print (entry) # (this will print locations and instructors. how do i go about printing list..)
    for key, values in dojo.items():
        print(len(values), key) #this will print the length of the list and capitalize all the letters in my key
        if(isinstance(values, list)): #this if statement checks to see if the values are a list, if they are then i have it run a loop thru each value in the list and print it. if we were to add a 3rd key, that had a sigular value, then we jump to the else statement. 
            for value in values:
                print(value)
        else:
            print(values)
        

    for key, value in dojo.items():
        print(f" {len(value)} {key.upper()}")
        for i in range(0, len(value)):
            print(value[i])


printInfo(dojo)