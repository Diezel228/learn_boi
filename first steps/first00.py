'''
print("hello, world!!") ### this be a string mon
x = "this a variable mon!"
print (x + "\n now. \nlets get started!!!!")

# an 'f' string
#print(f"hello, " + x) # so the f didn't actually do anything in this example.... idk.
print(f"Hello, {x}") # I believe this is named for a function being inside the string.

name = "tommy"
print (name[2]) # query/parse speicfic characters 
food=input("what is your favorite food?")
hobby=input("what is your favorite hobby?")

print(f"{food} and {hobby}" + " are the things!!!!" + "\nThats an 'f'string in action!")  

age=int(input("how old are you? "))
if age <= 5:
    print("you are a kid!")
elif age <= 15:
    print("your a big kid!!!!!!")
elif age <= 50:
    print("bigger kid")
else:
    print("biggest kidDDSJAGKDSLAJF!!!!")

word = "space"
for e in word:
    print (e)
'''
myList = [432,4321,4,3,687]# elements are scalars, each element has an index.
for i in myList:
    print("number: " + str(i))


on = True
z = 1
while on:
    var = input("continue looP? y or n: ")
    z += 0
    print (z)
    if var == "n":
        on = False