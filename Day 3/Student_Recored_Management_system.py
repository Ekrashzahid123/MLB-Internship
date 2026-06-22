student=[]
#-----------------------------------------------------------------------#
def add_student():
    data={
        "name":input("Enter the name of student:"),
        "Roll Number":input("Enter the Roll Number of student:"),
        "Age":input("Enter the age of student:"),
        "Course":input("Enter the course of student:")

    }
    student.append(data)
    print("Student added Successfully")
#-----------------------------------------------------------------------#
def view_student():

    if len(student)==0:
        print("No student record found.")
    else:
        print("All Student Records")
        for s in student:
            print("------------------------------")
            print("Name:",s["name"])
            print("Roll Number:",s["Roll Number"])
            print("Age:",s["Age"])
            print("Course:",s["Course"])
    print("Total number of students:",len(student))
#-------------------------------------------------------------------------#
def find_student():
    roll_number=input("Enter the Roll number of student to find:")
    for s in student:
        if s["Roll Number"]==roll_number:
            print("Student found:")
            print("------------------------------")
            print("Name:",s["name"])
            print("Roll Number:",s["Roll Number"])
            print("Age:",s["Age"])
            print("Course:",s["Course"])
            return s
    print("No student record found with Roll Number:",roll_number)
    return None
#---------------------------------------------------------------------------#
def  update_student():
    found_student=find_student()
    if found_student is not None:
        print("Enter new details for the student:")
        found_student["name"]=input("Enter the name of student:")
        found_student["Roll Number"]=input("Enter the Roll Number of student:")
        found_student["Age"]=input("Enter the age of student:")
        found_student["Course"]=input("Enter the course of student:")
        print("Student record updated successfully.")
    else:
        print("No student record found to update.")
#----------------------------------------------------------------------------#
def delete_student():
    found_student=find_student()
    if found_student is not None:
        student.remove(found_student)
        print("Student record deleted successfully.")
    else:
        print("No student record found to delete.")
#----------------------------------------------------------------------------#
def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Find Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice=input("Enter your choice 1 to 6:")
        if choice=="1":
            add_student()
        elif choice=="2":
            view_student()
        elif choice=="3":
            find_student()
        elif choice=="4":
            update_student()
        elif choice=="5":
            delete_student()
        elif choice=="6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__=="__main__":
    menu()
