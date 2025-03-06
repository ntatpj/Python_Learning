import subprocess as sp
import os


str_of_Date_PID="401616 1821048 \n67989 1948990"
list_of_date_pid=str_of_Date_PID.splitlines()
print(list_of_date_pid)
for i in list_of_date_pid:
        PID_details=i.split()
        print(PID_details[0])
        if int(PID_details[0]) >= 172800:
                print("hELLO IST AND OLD PROCESS",PID_details[1])
                PID=PID_details[1]
                print(PID)
                sp.getoutput("pkill "+PID)

print("The remiaing proecess are")
sp.getoutput("ps -ef| grep -i vnc | grep -v grep")
