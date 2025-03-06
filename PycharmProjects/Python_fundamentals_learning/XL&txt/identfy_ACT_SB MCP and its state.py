f =open("C:/Users/ntatpuj/Desktop/scripts_small/MCP_ACT_SB.txt")
PA = "PA -F"
# print(help(open("C:/Users/ntatpuj/Desktop/scripts_small/MCP_ACT_SB.txt")))
print(f.tell())
while True:
    line = f.readline()
    if PA in line:
        words_in_line = next(f).split()
        print(words_in_line)
        if words_in_line[2] == "C1":
            if words_in_line[-1].strip() == "Act":
                if words_in_line[4].strip()=="CardOk":
                    print("C1 is act and in Cardok State")
                elif words_in_line[4].strip()!="CardOk":
                    print("C1 is act and in but NOT IN Cardok State")
                else:
                    print("Some other issue with C1")
            elif words_in_line[-1].strip() == "Sb":
                if words_in_line[4].strip()=="CardOk":
                    print("C1 is standby and in Cardok state")
                elif words_in_line[4].strip()=="Ueq":
                    print("C1 is standby and HW not detected in shelf")
                elif words_in_line[4].strip()=="Failed":
                    print("C1 is standby and HW in Failed State")
                elif words_in_line[4].strip() == "PeriodProbe":
                    print("C1is standby and HW in booting or stuck")
                else:
                    print("Some other issue with C1")
        elif words_in_line[2] == "C2":
            print("in second line")
            if words_in_line[-1].strip() == "Act":
                if words_in_line[4].strip()=="CardOk":
                    print("C2 is act and in Cardok State")
                elif words_in_line[4].strip()!="CardOk":
                    print("C2 is act and in but NOT IN Cardok State")
                else:
                    print("Some other issue with C1")
            elif words_in_line[-1].strip() == "Sb":
                if words_in_line[4].strip()=="CardOk":
                    print("C2 is standby and in Cardok state")
                elif words_in_line[4].strip()=="Ueq":
                    print("C2 is standby and HW not detected in shelf")
                elif words_in_line[4].strip()=="Failed":
                    print("C2 is standby and HW in Failed State")
                elif words_in_line[4].strip() == "PeriodProbe":
                    print("C2is standby and HW in booting or stuck")
                else:
                    print("Some other issue with C2")



