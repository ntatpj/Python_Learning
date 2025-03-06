import sys
import subprocess as sp
import os

def Clear_stuck_session():
    Display_ps_ef_VNC_session()
    print('This will clear sessions that are older than 24Hours')
    str_of_Date_PID=sp.getoutput("ps -eo etimes,pid,cmd | grep -i vnc | grep -v grep |grep -v Check_VNC_session_RHEL_new.py| awk '{print $1, $2}'")
    list_of_date_pid=str_of_Date_PID.splitlines()
    for i in list_of_date_pid:
        PID_details=i.split()
    #   if int(PID_details[0]) >= 172800:
        if int(PID_details[0]) >= 500:
            PID=PID_details[1]
            sp.getoutput("kill -9 "+PID)
    print(f"Currently open VNC sessions aftr clearinf stuck sessions are->\n")
    Display_ps_ef_VNC_session()

def Forcekillsession_id():
    print(" This will forcefully kill the VNC session selected. \n Currently open VNC sessions are->")
    #to Dilpay no of active VNC sessions
    Display_ps_ef_VNC_session()
    VNC_ID = sp.getoutput("ps -ef | grep -i vnc | grep -v grep|grep -v Check_VNC_session_RHEL_new.py| awk {'print$ 9'}")
    list_of_sessions=VNC_ID.splitlines()
    while 1:
        VNC_session_id = input("Enter the VNC session from above to be killed OR type q to exit->")
        if VNC_session_id=="q":
            break
        elif VNC_session_id in list_of_sessions:
            print( "Session to get killed is", VNC_session_id)
            PID_to_get_killed=sp.getoutput("ps -ef| grep -i vnc | grep " + VNC_session_id + "| awk {'print$2'}")
            #print("PID to get killed is",PID_to_get_killed)
            sp.getoutput("kill"+ " "  + PID_to_get_killed)
            #print(o)
    print(f"Currently open VNC sessions are->\n")
    Display_ps_ef_VNC_session()

def Display_ps_ef_VNC_session():
    VNC_ID = sp.getoutput("ps -ef | grep -i vnc | grep -v grep |grep -v Check_VNC_session_RHEL_new.py| awk {'print$1,$2,$5,$9'}")
    list_of_sessions=VNC_ID.splitlines()
    #print(list_of_sessions)
    ip_addr=sp.getoutput("ip addr | egrep vmnic | grep brd |awk '{print$2}'")
    list_of_session_splitted_in_list=[]
    for line in list_of_sessions:
        list_of_session_cosmetics=line.split()
        print(f'VNC PID {list_of_session_cosmetics[1]} of Display {list_of_session_cosmetics[3]} is used by IP {ip_addr} and user {list_of_session_cosmetics[0]} started at {list_of_session_cosmetics[2]}')

def choose_options(argument):
    if argument=="clear":
        Clear_stuck_session()
    elif argument=="abort":
        Forcekillsession_id()
    elif argument=="refresh":
        Display_ps_ef_VNC_session()
    elif argument=="v":
        print("v1")

