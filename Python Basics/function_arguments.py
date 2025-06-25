# Default arguments

def name(fname, mname = "Jhon", lname = "Whatson"):    #mname and lname have a default value 
    print("Hello,", fname, mname, lname)

name("Amy")


# Keyword arguments

def name(fname, mname, lname):                                 #interpreter recognizes the arguments by the parameter name.
    print("Hello,", fname, mname, lname)                       #Hence, the the order in which the arguments are passed does not matter.

name(mname = "Peter", lname = "Wesker", fname = "Jade")


# Required arguments - number of arguments passed should match with actual function definition.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)    #Here number of arguments passed does not match to the actual function definition.

name("Peter", "Quill")


# Variable-length arguments
# Arbitrary Arguments       
def name(*name):                                     # While creating a function, pass a * before the parameter name while defining the function.
    print("Hello,", name[0], name[1], name[2])       # The function accesses the arguments by processing them in the form of tuple.

name("James", "Buchanan", "Barnes")

# Keyword Arbitrary Arguments:
def name(**name):                                                     # While creating a function, pass a * before the parameter name while defining the function.
    print("Hello,", name["fname"], name["mname"], name["lname"])      # The function accesses the arguments by processing them in the form of dictionary.

name(mname = "Buchanan", lname = "Barnes", fname = "James")


# Return Statemant

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))
