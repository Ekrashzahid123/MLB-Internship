#find largest number in list
numbers=[10,20,50,9,100,200,300]
lagest=numbers[0]
for i in numbers:
    if i>lagest:
        lagest=i
print("Largest number in the list is:",lagest)

#-------------------------------------------#

#second largest number in list
numbers=[10,20,50,9,100,200,300]
largest=numbers[0]
second=numbers[0]
for i in numbers:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print(second,"is the second largest number in the list")

#-------------------------------------------#
#remove duplicates from list
numbers=[10,20,50,9,100,200,300,10,20,50]
new_list=[]
for i in numbers:
    found=False
    for j in new_list:
        if i==j:
            found=True
    if not found:
        new_list.append(i)
print("List after removing duplicates:",new_list)
#-------------------------------------------#
#reverse  A lsit

numbers=[10,20,50,9,100,200,300]
new_list=[]
i=len(numbers)-1
while i>=0:
    new_list.append(numbers[i])
    i=i-1
print("Reversed list is:",new_list)
#-------------------------------------------3
list1=[10,20,50,9,100,200,300]
list2=[10,20,50,9,100,200,300]
common=[]
for i in list1:
    if i in list2:
        common.append(i)
print("Common elements in both lists are:",common)

