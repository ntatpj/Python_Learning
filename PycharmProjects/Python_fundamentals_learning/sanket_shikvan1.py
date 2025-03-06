class STUDENTS:
    name = None
    roll_no = None
    age = None
    sex = None
    std = None
    div = None


    ToDo=input("""Enter taskt to be perfromed 
        Type 1: To Enter student detail 
        Type 2: To read detail of student
        Type 3: Update details of a student
        Type 4: To delete all details of student
        """)
    list_of_students=[]


    def Create_Student_details_entry():
        print("I am in creting mode")
        while(True):
            obj=input("Enter student details")
            obj.name = input("Enter student name")
            obj.roll_no = input("Enter student roll no")
            obj.age = input("Enter student age")
            obj.sex = input("Enter student sex")
            obj.std = input("Enter student std")
            stopper = input("to stop press q or Q")
            list_of_students.append(obj)
            if stopper == "q" or "Q":
                break
            else:
                continue
    def To_read_detail_of_student():
        print("OK")

    def Function_to_be_perfromed(arg1):
        switcher:{
            1: Create_Student_details_entry(),
            2: To_read_detail_of_student(),
            3: Update_details_of_a_student(),
            4: To_delete_all_details_of_student()
                } # type: ignore
        
    Function_to_be_perfromed(ToDo)


Object=STUDENTS()
# Neha.name=Neha
# print(Neha.name)