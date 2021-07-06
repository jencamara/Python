for x in range (151):
    print(x)

for x in range (5, 1001, 5):
    print (x)

for x in range (1, 101):
    if x % 10 == 0:
        print ("Coding Dojo")
    if x % 5 == 0:
        print ("Coding")
    else: 
        print (x)

O = 0
for num in range (0, 500,000):
    if (num % 2 != 0):
        O = O + num
print (O)
        
