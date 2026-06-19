
print('---------------------')
print("-Student Grade System-")
print("---------------------")
noofstudent=int(input("Enter the total number of students:"))
name=input("Enter student name:")
class1=int(input("Enter the name of class:"))
subject1=input("Enter the subject:")
subject2=input("Enter the subject:")
subject3=input("Enter the subject:")
marks1=int(input("Enter the marks of subject physics:"))
marks2=int(input("Enter the marks of subject chemistry:"))
marks3=int(input("Enter the marks of subject maths:"))
avarage=(marks1+marks2+marks3)/3
print("The average marks of student is:",avarage)



if(avarage<0 or avarage>100):
    print("Invalid marks. Please enter a value between 0 and 100.")

elif avarage>90:
    print("Grade A")

elif avarage>=80 and avarage<90:
    print("Grade B")

elif avarage>70 and avarage<=80:
    print("Grade C")

elif avarage>60 and avarage<70:
    print("Grade D")

elif avarage>50 and avarage<=60:
    print("Grade F")
