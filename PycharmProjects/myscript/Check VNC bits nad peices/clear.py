import sys
import subprocess as sp
import os
def Clear_stuck_session():
        print('This will clear stuck sessions')
        str_of_Date_PID=sp.getoutput("ps -eo etimes,pid,cmd | grep -i vnc | grep -v grep| awk '{print $1, $2}'")
        print(str_of_Date_PID)
        list_of_date_pid=str_of_Date_PID.splitlines()
        print(list_of_date_pid)
        for i in list_of_date_pid:
                PID_details=i.split()
                print(PID_details[0])
                if int(PID_details[0]) >= 172800:
                        print("hELLO IST AND OLD PROCESS",PID_details[1])
                        PID=PID_details[1]
                        sp.getoutput("kill -9 "+PID)
                        print(PID)


#        o=sp.getoutput("ps -ef| grep -i vnc | grep -v grep|awk '{print $9}'")
#       print(o)
#        print(f"The open VNC sessions are {o}")




import sys
import subprocess as sp
import os

def Forcekillsession_id():
        print(" This will forcefully kill PID")

#to Dilpay no of active VNC sessions
        VNC_ID = sp.getoutput("ps -ef | grep -i vnc | grep -v auto| awk {'print$ 9'}  ")
        print(VNC_ID)
        VNC_session_id = input("Enter the session ID to be killed")
#   print(VNC_session_id)
        PID_to_get_killed=sp.getoutput("ps -ef| grep -i vnc |grep -v grep| grep VNC_session_id | awk {'print$2'} ")
        print("hee",PID_to_get_killed)

Forcekillsession_id()


Clear_stuck_session()

