import paramiko
import sys
import os
#import listdir
from subprocess import Popen, PIPE
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('192.168.90.106', username='root', password='rsqa@')
    print "connection is established"
    old=os.getcwd()
    print old
    os.chdir("//DGlogs//")
    new=os.getcwd()
    print new
   # files = os.listdir(os.curdir)
    
    stdin,stdout,stderr = ssh.exec_command("ls -lrt")
except paramiko.SSHException:
    print "Connection Failed"
    quit()
#stdin,stdout,stderr = ssh.exec_command("ls -lrt")
#print stdout
                           
for line in stdout.readlines():
     print line
ssh.close()
