#!/usr/bin/python3



#Create two different objects with the same value.
a = 5
b = 5

print(id(a))
#Output: 139632869241032
print(id(b))
#Output: 139632869241032
print(a is b)
#Output: True
print(a == b)
#Output: True

#The id of each object will be the same because   the objects are of the same value. For this   reason, id () should not be used for   comparison purposes.





#This is also true if you assign one as an alias   to another. 
c = 'OOP'
d = c


print(id(c))
#Output: 140564447114928
print(id(d))
#Output: 140564447114928
print(c is d)
#Output: True
print(c == d)
#Output: True


#This is not the case for lists. 

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(id(list1))
#Output: 140062063514560
print(id(list2))
#Output: 140062063531264

#The id of each list is different, which means      that list1 and list2 are not referring to       the same object regardless of their matching values. We can also prove this using    comparison operators:

print(list1 == list2)
#Output: True
print(list1 is list2)
#Output: False


#We can, however, allow two variables for a list refer to the same object if we make an alias.

list3 = list2

print(list3 is list2)
#Output: True


#We can also clone a list using the slice [:] operator to create a new list.

list4 = list1[:]

print(list4 is list1)
#Output: False
print(list4 == list1)
#Output: True



#Define lists for manipulation
listA = [1, 2, 3]
listB = [4, 5, 6]

print(id(listA))
#Output: 140591671200832

listB = listB + [4]

print(listB)
#Output: [1, 2, 3, 4]
print(id(listB))
#Output: 140591671203520

listA = [1, 2, 3, 4]
print(id(listA))
#Output: 140591671217536

listA.append(7)

print(listA)
#Output: [1, 2, 3, 4]
print(id(listA))
#Output: 140591671217536


#Create an immutable object: integer
x = 5

print(id(x))
#Output:140248377397448

x = x + 1

print(id(x))
#Output: 140248377397480

#Define function to change a mutable object.
def change_list(some_list, n):
    some_list.append(n)

#Create new list and call function
my_list = [2, 4, 6]
print(id(my_list))
#Output: 140336671001472
change_list(my_list, 8)

print(my_list)
#Output: [2, 4, 6, 8]
print(id(my_list))
#Output: 140336671001472


#Define function to change an immutable object.
def mult_ints(a, b):
   return x * y
    
#Create new integers, call id()
x = 5
y = 6

print(id(x))
#Output: 140430432366792

#Call function
print(mult_ints(x, y))
#Output: 30

print(x)
#Output: 5
print(id(x))
#Output: 140430432366792
