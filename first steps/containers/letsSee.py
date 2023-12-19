name = "Lydia"# variables get saved straight to memory directly with string
list = [24,34,21,76] #creates a var thats a referance to a memory address
list2 = list #creates a copy of the address in memory first, change the first and second changes too.
#in order to have a for this not to happen(splice) the list
list3 = list2[0:3]
print(name, "\n" ,str(list) ,"\n" , str(list2), "\n", str(list3))