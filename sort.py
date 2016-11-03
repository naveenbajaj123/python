import os
import sys
new=sys.argv[1]
fh=open(new,"r")
for line in sorted(fh):
	print line
