import subprocess as sp
import os
dates_of_pid=sp.getoutput("ps -ef | grep -i vnc | awk {'print $5'}")
list_of_pid_dates=dates_of_pid.split("\n")
#for i in dates_of_pid:

