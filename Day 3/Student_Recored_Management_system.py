student=[]
def add_student():
    data={
        "name":input("Enter the name of student:"),
        "Roll Number":input("Enter the Roll Number of student:"),
        "Age":input("Enter the age of student:"),
        "Course":input("Enter the course of student:")

    }
    student.append(data)
    print("Student added Successfully")

def view_student():

    if len(student)==0:
        print("No student record found.")
    else:
        print("All Student Records")
        for student in students:
            print("------------------------------")
            print("Name:",student["name"])
            print("Roll Number:",student["Roll Number"])
            print("Age:",student["Age"])
            print("Course:",student["Course"])
    print("Total number of students:",len(student))