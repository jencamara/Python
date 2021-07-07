# 1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
updated_x = list (x[1]) 
updated_x[0] = 15
x = list(x)
x[1] = updated_x
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
new_alias = students[0]
new_alias['last_name'] = 'Bryant'
students[0] = new_alias
print(students)


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print (sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print (z)

# 2 Iterate through a list of dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for student in students:
        print(f"first_name - {student['first_name']} , last_name -{student['last_name']}")
iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# 3 Get Values From a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name,some_list):
    for item in some_list:
            print(item[key_name])
iterateDictionary2('first_name',students)
iterateDictionary2('last_name', students)
        

# 4 Iterate Through a dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        list = some_dict[key]
        print(f"{len(list)} {key}")
        for item in list:
            print(item)
        # print(f"{thing['locations']}, {thing['instructors']}")
printInfo(dojo)


# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


