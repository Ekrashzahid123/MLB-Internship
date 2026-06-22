#----------------------------------------------------#
numbeers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
unique_numbers =[]
for i in numbeers:
    if i not in unique_numbers:
        unique_numbers.append(i)

print("Unique numbers in the set are:", unique_numbers)

#----------------------------------------------------#
set1 = [1,2,3,4]
set2 = [3,4,5,6]

union = []

for i in set1:
    if i not in union:
        union.append(i)

for i in set2:
    if i not in union:
        union.append(i)

print("Union:", union)


# Intersection
intersection = []

for i in set1:
    if i in set2:
        intersection.append(i)

print("Intersection:", intersection)