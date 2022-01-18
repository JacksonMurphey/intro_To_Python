# doggo = ["jackson", 19, False]
# print(doggo[1])

# # if you get error and you see assigning = assignment 
# # if you get error and you see indices = indexes  


# pizza = {
#     'style': "New York",
#     'slices': 8,
#     'size': 'S',
#     'ingredients': ['crust', 'red sauce', 'cheese','pepperoni']
# }

# #how would we access the number of slices?



# #how would we creat a new key
# pizza['would_reorder'] = True


# #how would we change red sauce to white sauce
# pizza['ingredients'][1] = 'white sauce'

# #add to the list of ingredients
# pizza['ingredients'].append('mushrooms')



#my own practice. 

employees_info = [

    {'first_name': 'Doug', 'last_name': 'Martin', 'age': 33, 'salary': 85000, 'job_title': 'Operations Manager', 'responsiblities': ['Manage office personel', 'Payroll', 'Customer Retention', 'Implement new business strategies']},
    
    {'first_name': 'Sally', 'last_name': 'Summers', 'age': 40, 'salary': 45000, 'job_title': 'Assistant', 'responsiblities': ['Manage daily schedule', 'Take phone calls', 'Handle any duties assigned by boss', 'Schedule appointments']},
    
    {'first_name': 'Steve', 'last_name': 'Martin', 'age': 36, 'salary': 200000, 'job_title': 'CEO', 'responsiblities': 'Make sure the business increases annual revenue, year over year'},
    
    {'first_name': 'Randy', 'last_name': 'Touche', 'age': 24, 'salary': 30000, 'job_title': 'Janitor', 'responsiblities': ['Keep office Clean', 'Keep bathrooms Clean', 'Take out trash', 'Lock the Office'] },

    {'first_name': 'Matt', 'last_name': 'Smith', 'age': 26, 'salary': 50000, 'job_title': 'Office Worker', 'responsiblities': ['Handle daily tasks', 'Ensure customer satisfaction', 'Keep updated customer records', 'Upkeep of company assests'] },

    {'first_name': 'Chad', 'last_name': 'Hadder', 'age': 28, 'salary': 52000, 'job_title': 'Office Worker', 'responsiblities': ['Handle daily tasks', 'Ensure customer satisfaction', 'Keep updated customer records', 'Upkeep of company assests'] },

    {'first_name': 'Ricky', 'last_name': 'Stern', 'age': 30, 'salary': 60000, 'job_title': 'Office Worker', 'responsiblities': ['Handle daily tasks', 'Ensure customer satisfaction', 'Keep updated customer records', 'Upkeep of company assests'] },

    {'first_name': 'Mary', 'last_name': 'Kline', 'age': 30, 'salary': 70000, 'job_title': 'Sales', 'responsiblities': ['Identify new Customers', 'Outside sales', 'Cold calling customers', 'Customer Retention', 'Entertain Customers visiting'] },

]

# president = employees_info[2]
# print(president)
# print(president.items()) #.items(), is a method that will only work with a dictionary. returns: dict_items(['LISTS' each key:value pair within the dictionary for employees_info[2] ])


#So lets try to iterate through our list of dictionaries, to return each employees responsibilites in a string. 
# We are looking in the list of dicts to find the key and then list the values of that key. 

def responsobiltyCheck(key_name, lists):
    # for items in employees_info: #this iterates thru our list of dicts
        # print(items['responsiblities']) this prints each employees job responsibilities, we have 8 employees, 7 have lists, 1 has a string. 
        # print(f'Employee Name: {items["first_name"]} {items["last_name"]} - Responsible for: {items["responsiblities"]}') This f format string, printed what I wanted, (names and responsiblities). however, it printed all employees with a list of responsiblities, in a list. I want just their resp. printed in a string. 
        # print({k: [d.get(k) for d in lists]
        # for k in set().union(*lists)}) #this creates a dictionary, in which it takes the keys and creates a list of all values for that key. ex: {'last_name': ['Martin', 'Summers', etc]}
    # for i, entry in enumerate(lists):
    #     if entry[key_name] == lists[i]['responsiblities']:
    #         print(f"{i+1}: {entry['first_name']} {entry['last_name']} - Job Responsoblities: {entry[str('responsiblities')]}")
            #Ok, so this printed their name but everyones responsibilites were still in a list.
    
    for i, entry in enumerate(lists):
        # for key, values in employees_info[i].items():
        if entry[key_name] == lists[i]['responsiblities']:
                    
                    
            print(f"Job Responsoblities: {entry['responsiblities']}")
        #this is printing what i want, to get the items out of the list, i need to iterate through the list and print the values. 

responsobiltyCheck('responsiblities', employees_info)



#OOP (objext orientated programming)


    #1) constructor-function! -- creates the instance of an object.
    #2) self: is a representation of the instance, not the class! 
    #def __init__(self) -> None: -----This is what an initial format looks like
    #    pass

    #3) Coding dojo video preview of a basic layout.. 
# class User:
    # def __init__(self, first_name, last_name, age):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.age = age

#NOTE: practice below
# declare a class and give it name: User  (when creating a class, the name must be capitalized.)
# class User:
#         def __init__(self):
#             self.name = "Michael"
#             self.email = "michael@codingdojo.com"
#             self.account_balance = 0

# #NOTE: INSTANCE ATTRIBUTES 
# # Now we can create INSTANCES of the User:
# User()
# guido = User()
# monty = User()
# #accessing the INSTANCE's attributes
# print(guido.name) # output: Michael
# print(monty.name) # output: Michael

# # We can also set the values for our INSTANCE's attributes:
# guido.name = "Guido"
# print(guido.name) # output: Guido
# monty.name = "Monty"
# print(monty.name) # output: Monty 

# #NOTE: CLASS ATTRIBUTES 
# #Class attributes are defined outside of any instance methods, and is shared among all instances of the class. 
# class User:
#     #Declaring a class attribute:
#         bank_name = "First National Dojo"
#         #Class Attributes are more flexible because we can change them on an instance or the entire class. 
#         def __init__(self):
#             self.name = "Michael"
#             self.email = "michael@codingdojo.com"
#             self.account_balance = 0

# #Ex: Changing them on an instance:
# guido = User()
# monty = User()
# guido.bank_name = "Dojo Credit Union"
# print(guido.bank_name) # output: Dojo Credit Union
# print(monty.bank_name) # output: First National Dojo

# # Ex: changing them on the entire Class:
# User.bank_name = "Bank of Dojo"
# print(guido.bank_name) # output: Bank of Dojo (for whatever reason, on my terminal it still says Dojo Credit union, this could be because, above I specifically changed GUIDO's bank name to Dojo Credit union.)
# print(monty.bank_name) # output: Bank of Dojo

#NOTE: Passing in ARGUMENTS:
#
# class User:
#     #   Class attributes get defined in the class
#         bank_name = "First National Dojo"
#     #   Now our METHOD has 2 parameters!
#         def __init__(self, name, email_address):
#         #   We assign them accordingly 
#             self.name = name
#             self.email = email_address
#         #   The account Balance is set to $0
#             self.account_balance = 0 # here we have no attribute for accountBalance in the paramters, we are essentially stating that everyone's acct will start with $0.00 
# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")
# print(guido.name) # output: Guido van Rossum
# print(monty.name) # output: Monty Python 

#NOTE: METHODS: adding methods to a Class. 
# Methods allow you to basically add some functionality to your Class. 
# Methods are just functions that belong to the class. This means we cannot call these functions independently, as we have previously; Rather, methods must be called from an instance of a class. 
# Following the above Class we have created, lets say a user wants to make a deposit, we would need to call the method from the USER INSTANCE; b/c a specific user is making the deposit. 
# to make such a call, would look like this:
# ------ guido.make_deposit(100) --------
# to be able to call on this method, it needs to exist. 
class User:
    def __init__(self, name, email):
            self.name = name
            self.email = email
            self.account_balance = 0
        # adding the deposit method:
        
    def make_deposit(self, amount): # takes an argument that is the amount of the deposit. 
            self.account_balance += amount #the specific user's account increases by the amount of the value received.

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)

print(guido.account_balance) # output: 300
print(monty.account_balance) # output: 50