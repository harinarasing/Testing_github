#list tuple set dictionary

from requests import delete


my_list =["apple", "banana", "cherry"]

print(my_list)

print(my_list[1])
print(my_list[2])
print(my_list[0])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[0].upper())
print("**********************")
#print(my_list[4])
my_list.append("orange")
print(my_list)
#my_list.append("banana")
my_list[0]="lemon"
print(my_list)

print(len(my_list))
print(len(my_list)-7)
print("###############################")

my_data= ["hari", 23, 3.5, "ricky", 25, 4.5]

print(my_data)

my_data[1] = True
print(my_data)  

print(type(my_data))

#The list() Constructor

my_list2 = list(("jam", 25, False))
print(my_list2)
print(type(my_list2))

my_data1= ["hari", 23, 3.5, "ricky", 25, 4.5]

print(len(my_data1))
print(my_data1[2:5]) 
print(my_data1[7:5]) 
print(my_data1[5:2]) 
print(my_data1[:2]) 
print(my_data1[:-2]) 
print(my_data1[2:]) 
print(my_data1[-2:]) 
print(my_data1[-4:-2]) 

if "hari" in my_data1:
  print("Yes, 'hari' is in the list")   

print("**********************")

my_data1[1:3] =["grape","papaya"]
print(my_data1)

my_data1.insert(-2, "kiwi")
print(my_data1)

mylist3 = ['apple', 'banana', 'cherry']
mylist3[0] = 'kiwi'
print(mylist3)
print(mylist3[1])

# append is Used to add an item to the end of the list, and insert is used to add an item at a specified index.
# index is used to add an item at a specified index, and append is used to add an item to the end of the list.
# del is used to remove an item from the list at a specified index, and remove is used to remove an item from the list by value.


del mylist3[1]
print(mylist3)
print("+++++++++++++++++++++++++++++++++++")
print(my_data)
#my_data.extend(["orange", "mango", "grapes"])
my_data.extend(my_data) 
# extend() method adds the specified list elements (or any iterable) to the end of the current list. 
# The extend() method does not have to return any value, it modifies the original list in place.
print(my_data)

my_data.remove("ricky")
my_data.pop(2)
my_data.pop()
del my_data[4]
#del method removes the item at the specified index, and pop() method removes the item at the specified index and returns it.
#pop() method removes the item at the specified index.
#remove() method removes the first matching value, not a specific index.
print(my_data)

my_info = ["hari", "raju"]
print(my_info)

del my_info # delete the list completely

my_info = ["hari", "raju"]
my_info.clear() # clear the list
print(my_info)

#Loop Lists

my_marks=[23, 29,45, 67, 89, 90]

print(my_marks)    



 

for hari_marks in range(len(my_marks)):
    
    print(hari_marks) # index of the list
    print(my_marks[hari_marks]) # value of the list
    print("**********************")

    [print(hari_marks)for hari_marks in my_marks] #List Comprehension
       

print("**********************")

# while loop

i=0
while i < len(my_marks):
    print(my_marks[i])
    i+=1

# create a new list using list comprehension
# newlist = [expression for item in iterable if condition == True]

new_list = [x for x in my_marks if "2" in str(x)]
print(new_list)
print(my_marks)

new_list1 = [x for x in my_marks if "45" not in str(x)]
print(new_list1)









