def require_sentence():
	name=raw_input("entre the sentence\n")
	return name
out=require_sentence()
print out
print  out[-1],    "  last word of sentence" #print last word
print  out[-5:],   "  last 5 charater of sentence\n",#print last 5 character of the sentence
print  out[1],     "  2nd position charater of sentence\n"  #print 2nd character
print  out[4],     "  5th position charater of sentence\n"  #5th character
new=len(out)/2
mid=out[new]
lmid=out[new-1]
rmid=out[new+1]
print lmid+mid+rmid,    "   midlle char with adjoining charater of the sentence"    #print adjing chracter




