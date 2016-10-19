import paramiko
import sys 
def established(server_name):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(server_name, username='root', password='rsqa@')
    print "connection was established"
except paramiko.SSHException:
    print "Connection Failed"
    quit()

stdin,stdout,stderr = ssh.exec_command("ls")
for line in stdout.readlines():
    print line.strip()
    ssh.close()

def connection():
    ouput = raw_input("Enter the local server name\n")
    return output
server=connection()
established(server)









                          

