def require_sentence():
	name=raw_input("entre the sentence\n")
	return name
out=require_sentence()
print out
print out[-1] #print last word
print out[-5:]#print last 5 character of the sentence
print out[2]  #print 2nd character
print out[5]  #5th character
new=len(out)/2
mid=out[new]
lmid=out[new-1]
rmid=out[new+1]
print lmid+mid+rmid#print adjing chracter




