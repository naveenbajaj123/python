import paramiko
import sys
import socket
import os

#input=raw_input("enter the server name")
#hosts = open('/etc/hosts','r')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
new=raw_input("enter the input\n")
try:    
    if(new == 'ps1'):
        out1= socket.gethostbyname('ps1')
        print out1
        ssh.connect(out1, username='root', password='rsqa@')
        print "poc1 connefctipon established",out1
        stdin,stdout,stderr = ssh.exec_command ("ls -ltr /DGlogs/ | grep PrSipAdaptor* | tail -1")
        for line in stdout.readlines():
            print line
    elif(new == 'ps1rr'):
        outg=socket.gethostbyname('ps1rr')
        print outg
        ssh.connect(outg, username='root', password='rsqa@')
        print "poc1 connefctipon established",outg
        stdin,stdout,stderr = ssh.exec_command ("ls -ltr /DGlogs/ | grep PrSipAdaptor* | tail -1")
        for line in stdout.readlines():
                print line

    elif(new == 'ps2'):
        out2= socket.gethostbyname('ps2')
        ssh.connect(out2, username='root', password='rsqa@')
        print "poc2 connefctipon established",out2
        stdin,stdout,stderr = ssh.exec_command ("ls -ltr /DGlogs/ | grep PrSipAdaptor* | tail -1")
        for line in stdout.readlines():
            print line
    elif(new == 'ps7'):
        out3= socket.gethostbyname('ps7')
        ssh.connect(out3, username='root', password='rsqa@')
        print "poc7 connefctipon established",out3
        stdin,stdout,stderr = ssh.exec_command ("ls -ltr /DGlogs/ | grep PrSipAdaptor* | tail -1")
        for line in stdout.readlines():
            print line
    elif(new == 'ps10'):
        out4= socket.gethostbyname('ps7')
        ssh.connect(out4, username='root', password='rsqa@')
        print "poc10 connefctipon established",out4
        stdin,stdout,stderr = ssh.exec_command ("ls -ltr /DGlogs/ | grep PrSipAdaptor* | tail -1")
        for line in stdout.readlines():
            print line

    else:
        print "server name doesnt matc with host file"
except paramiko.SSHException:
    print "Connection Failed"
    quit()
#for line in stdout.readlines():
    #print line
#for line in hosts:
   # print line.split()[0:]
    #if (input == 'ps1'):
        #out=str.replace(input,line[0])
        #print out

