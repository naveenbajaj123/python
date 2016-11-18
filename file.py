import re
import os
import sys
file=sys.argv[1]
filewr=open('newaccept',"w")
filewrnot=open('notaccept',"w")
fileopen = open(file,"r+")
pat=re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
for line in fileopen.readlines():
	test = pat.match(line)
	if test:
		filewr.write(line)
		filewr.write("\n")
	else:
		filewrnot.write(line)
		filewrnot.write("\n")