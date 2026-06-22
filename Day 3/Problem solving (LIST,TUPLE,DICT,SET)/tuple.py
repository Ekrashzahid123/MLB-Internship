#----------------------------------------------------------#
#count the elecment in the tuple
t=(1,2,3,4,5,6,7,8,9,10)
element=2
count=0
for i in t:
    if i==element:
        count+=1
print("The element",element,"is found",count,"times in the tuple.")

#--------------------------------------------------#
#tuple to list and list to tuple
t=(1,2,3,4,5,6,7,8,9,10)
list1=list(t)
print("Tuple to list:",list1)
list2=[1,2,3,4,5,6,7,8,9,10]
t2=tuple(list2)
print("List to tuple:",t2)
