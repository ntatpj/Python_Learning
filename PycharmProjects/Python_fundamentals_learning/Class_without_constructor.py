class Class_without_constructor:
    name = None
    roll_no = None
    age = None
    sex = None
    std = None
    div = None

list_of_students=[]

def Create_detils_of_student():
    while (True):
        obj=Class_without_constructor()
        obj.name = input("Enter student name")
        obj.roll_no = input("Enter student roll no")
        obj.age = input("Enter student age")
        obj.sex = input("Enter student sex")
        obj.std = input("Enter student std")
        list_of_students.append(obj)
        # print(f"Mulanchi list ahe{list_of_students}")
        stopper = input("to stop press q or Q")
        if stopper == "q":
            break
        # for i in list_of_students:
            # print(f"Name of students whoes details you wanna fetch from below list {i.name}")
            # name_of_Students_whos_datat_to_be_shown=input()
            # print(i.name,i.age,i.sex,i.std,i.roll_no)
        # obj1=input(f"List of all students is{list_of_students}, enter the name of student whoes data you want to fetch")
        # print(obj1.name,obj1.roll_no,obj1.age,obj1.sex,obj1.std)
        # break

def Showdetails_of_student():
    name_of_Students_whos_datat_to_be_shown=input("Enter name of students whoese detail is to be fetched")
    for i in list_of_students:
        if name_of_Students_whos_datat_to_be_shown == i.name :
            print(i.name,i.age,i.sex,i.std,i.roll_no)

def Update_details_of_student():
    print("ok")

def Delete_details_of_student():
    name_of_Students_whos_datat_to_be_shown=input("Enter name of students whoese detail is to be deleted")
    for i in list_of_students:
        if name_of_Students_whos_datat_to_be_shown == i.name :
            list_of_students.remove[i]

Showdetails_of_student()

operation=input("Enet the opertion you want to exceute: Create,View,Update,Delete")
if operation=="Create":
    Create_detils_of_student()
elif operation=="View":
    Showdetails_of_student
elif operation=="Update":
    Update_details_of_student()
elif operation=="Delete":
    Delete_details_of_student()
else:
    print("Enter valid input")
# obj.age=21
# print(obj.age)