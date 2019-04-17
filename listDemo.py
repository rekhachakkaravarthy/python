#Creating a list
listFruits=["Apple","Mango", "Banana", "Orange"]
print(listFruits)
# Empty list
list1=[]
print(list1)
# Adding elements
list1.insert(0,"roses")
list1.insert(1, "jasmine")
list1.insert(-1,"lillies")
print(list1)
list1.insert(6,"pansies")
print(list1[0])
print(list1[-1])
print(list1)
#Appending elements
fru_flow=listFruits+list1
print(fru_flow)
# Removing Elements
list1.pop(1)
print(list1)
list2=["hello", "how", " ", "are", "you"]
print(list2)
print(list2[-5])
# Slicing elements
slicedFruit=listFruits[1:3]
print(slicedFruit)