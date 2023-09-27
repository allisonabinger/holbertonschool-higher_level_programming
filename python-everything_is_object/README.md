Python programming! The following is a review of all of the concepts discussed in this project, going over mutable and immutable objects, as well as object comparison. The first section are factual descriptions, and the second section are more in-depth examples


# Review of 'Everything is Object'


## Functions

### type()
#### Prints the type of an Object.

### id()
#### Prints variable identifier ()

## Objects and Modifications

		>>> a = 89
		>>> b = 100

		a and b do not point to the same object.

		>>> a = 89
		>>> b = 89

		a and b point to the same object

		>>> a = 89
		>>> b = a
		
		a and b point to the same object

		>>> a = 89
		>>> b = a + 1

		a and b do not point to the same object

		>>> s1 = "Best School"
		>>> s2 = s1
		>>> print(s1 == s2)

		True, they are pointing to the same object

		>>> s1 = "Best"
		>>> s2 = s1
		>>> print(s1 is s2)

		True, they are pointing to the same object

		>>> s1 = "Best School"
		>>> s2 = "Best School"
		>>> print(s1 == s2)

		True, the different variables have the same value (strings only)

		>>> s1 = "Best School"
		>>> s2 = "Best School"
		>>> print(s1 is s2)

		True, the different variable have the same value (strings only)

		>>> l1 = [1, 2, 3]
		>>> l2 = [1, 2, 3] 
		>>> print(l1 == l2)

		True, the different lists have the same value [tested with ==] but do not refer to the same object (different from strings)

		>>> l1 = [1, 2, 3]
		>>> l2 = [1, 2, 3] 
		>>> print(l1 is l2)

		False, True, the different lists have the same value [tested with ==] but do not refer [is] to the same object (different from strings)

		>>> l1 = [1, 2, 3]
		>>> l2 = l1
		>>> print(l1 == l2)
		
		True, the second list is now an alias for the same list.
		
		>>> l1 = [1, 2, 3]
		>>>l2 = l1
		>>> print(l1 is l2)

		True, the alias points to the same oject

		l1 = [1, 2, 3]
		l2 = l1
		l1.append(4)
		print(l2)

		[1, 2, 3, 4]

		l1 = [1, 2, 3]
		l2 = l1
		l1 = l1 + [4]
		print(l2)

		[1, 2, 3, 4]

		def increment(n):
 		   n += 1
		a = 1
		increment(a)
		print(a)

		1: integers are immutable, values can't changed after they're created. when increment calls the variable a, it calls a copy of it. 

		def increment(n):
    		n.append(4)
		l = [1, 2, 3]
		increment(l)
		print(l)

		[1, 2, 3, 4] will print because lists in Python are mutable. the list l is being called, not a copy

		def assign_value(n, v):
    		n = v

		l1 = [1, 2, 3]
		l2 = [4, 5, 6]
		assign_value(l1, l2)
		print(l1)

		[1, 2, 3] will print because assign_value is a pure_function, not a modifier, and will not modify the parameters passed to it. 

		Cloning Lists: using slice operator.
			
		a = [1, 2, 3]
		b = a[:]
		print b
			[1, 2, 3]
		b[0] = 5
		print a
			[1, 2, 3]

		Tuples

		Valid tuples:
			a = ()
			a = (1, 2)
			a = (1, )

		Invalid Tuples:
			a = (1)
			a = 1

		Tuples are not the same:
		a = (1, 2)
		b = (1, 2)

		a == b
			True
		a is b
			False
		
		Empty tuples [a = ()] are the same, python makes empty tuples reference
		the same object in memory to save space.

		id() : the id will change if the list is modified, such as a = a + [5],
		however, it will not change in the case of a +=


####################################

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
print(change_int(x, y))
#Output: 30

print(x)
#Output: 5
print(id(x))
#Output: 140430432366792
