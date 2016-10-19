import os
import sys
import fileinput
searchfile = sys.argv[1]
fp=open(searchfile,"r+")
#print "enter the search word"
search=raw_input("enetr the search word\n")
#print "enter the replace word"
replace=raw_input("enetr the replace word\n")
for line in fp.readlines():
	if search in line:
		print "match found"
		break
	else:
		print "notfoud"
        	break
fp.write(line.replace(search,replace))
print "word replaced"
print "again prining in the file"
fp.close()
for output in fp.readlines():
	print fp


