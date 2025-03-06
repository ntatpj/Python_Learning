import subprocess as sp
import os
def Clear_stuck_session():
    print('This will clear  sessions which are older than 2days')

def Forcekillsession_id():
    print(" This will forcefully kill PID")

    #to Dilpay no of active VNC sessions
    VNC_ID = sp.getoutput("ps -ef | grep -i vnc | grep -v auto| awk {'print$ 9'}")
    print(VNC_ID)
    VNC_session_id = input("Enter the VNC session from baove to be killed")
    print( "Session to get killed is", VNC_session_id)

    PID_to_get_killed=sp.getoutput("ps -ef| grep -i vnc | grep " + VNC_session_id + "| awk {'print$2'}")
    print("PID to get killed is",PID_to_get_killed)
    o=sp.getoutput("kill"+ " "  + PID_to_get_killed)
    print(o)
    new_process_list=sp.getoutput("ps -ef | grep -i vnc")
    print(new_process_list)



def Display_ps_ef_VNC_session():
    print("This will print the exsisting displays")
    # to Dilpay no of active VNC sessions
    VNC_ID = sp.getoutput("ps -ef | grep -i vnc | grep -v auto| awk {'print$ 9'}")
    print(VNC_ID)

def choose_options(argument):
    match argument:
            case "clear":
                print ("ok")
                Clear_stuck_session()
            case "abort":
                Forcekillsession_id()
            case "refresh":
                Display_ps_ef_VNC_session()
            case default:
                    print("Usage examples: CheckVncSession.sh  \n  clear     Clear stuck VNC sessions and files \n  refresh   Refresh xpid sessions if killed \n  abort     abort specific Display ID  \n  v         Script version   ")
                    argument = input("Choose one of the options above")
                    head = choose_options(argument)


print("Usage examples: CheckVncSession.sh  \n  clear     Clear stuck VNC sessions and files \n  refresh   Refresh xpid sessions if killed \n  abort     abort specific Display ID  \n  v         Script version   ")
argument=input("Choose one of the options above")
head = choose_options(argument)