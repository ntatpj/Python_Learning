global Student={"Neha":{"std":"10th","div":"B","roll_no":"81","age":"19","sex":"female","boyfrnd":"Sanket","color":"Wheatish"},"Riya":{"std":"15th","div":"A","roll_no":"23","age":"24","sex":"male","boyfrnd":"NA","color":"White"}}


class STUDENTS:
    # self.name=input("Enter the name")

    # self.detail=input("enter the detil you want to see from these (std,div,age,roll_no,boyfrnd,color)")

    def __init__(self,name,detail):
        # print("In init")
        if name not in Student:
            print(f"The student with name {name} is not present in our Database;Kindly check and provide appropriate name")
        for Name in Student:
            if Name==name:
                for  Detail in Student[Name]:
                    if detail not in Student[Name]:
                        print("Make sure you are entering from option from listed i.e std,div,age,roll_no,boyfrnd,color only")
                    break 
                    if Detail == detail:
                        print(f"For {Name} the {Detail} is {Student[Name][Detail]}")

    def method2(arg1,arg2):
        print("OK")
Obj1=STUDENTS("Neha","age")