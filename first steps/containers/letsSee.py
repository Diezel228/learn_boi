name = "Lydia"# variables get saved straight to memory directly with string
list = [24,34,21,76] #creates a var thats a referance to a memory address
list2 = list #creates a copy of the address in memory first, change the first and second changes too.
#in order to have a for this not to happen(splice) the list
list3 = list2[0:3]
print(name, "\n" ,str(list) ,"\n" , str(list2), "\n", str(list3))

print(list[1:])#slice from this index to the end
print(list[:4])#slice up to index (not specifying eg. [:] uses all items)
#you can specify negatives too!!!!
#    ////////print(list[:]) creates copy in memory
del list3 [:2]#modifies og list


#////////////////////////finding 
print(34 in list)
print(99 not in list)#these are opposites.............obviously >:)

matrix = [list, list2, list3]# 2D array or matrix
print(matrix [1:2])# should b list2 element 3 (0-9)
age = matrix[0:3]
print(age)


#3D array: also called que see que.py
