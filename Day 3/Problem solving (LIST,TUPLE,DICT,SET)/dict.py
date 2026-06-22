student={}
student["Name"]="ALi"
student["Roll Number"]="123"
student["Age"]=20
student["Course"]="Computer Science"
print(student)
#===============================================================#
marks = {
    "Ali":80,
    "Ahmed":70,
    "Sara":90
}

total = 0
count = 0

for key in marks:
    total += marks[key]
    count += 1

average = total / count

print(average)
#--------------------------------------------------------------#
sentence = "python is easy and python is powerful"

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)