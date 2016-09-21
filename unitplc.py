def perform_check(output1):
  
    if output1>=10 and output1<=99 :
        print "Enter number is two digit"
	unit1 = output1**5
	unit2= unit1%10
	print "unit place is two digit number",unit2
    elif output1>=100 and output1<=999 :
    	print "Enter number is three digit"
	output=raw_input("Enter the other number")
        output=int(output)
     	if output!=output1:
		unit3 = output+2
        	print unit3
		sumnew = unit3%10
		print "unit digit of three digit number is",sumnew
        else:
		print "entered new number i also same"
    elif output1<10:
	print  "enter number is first"
	sum= output1+7
	unit = sum%10
	print "unit place for the sigle digit number is",unit
    else:
  	print  "enter number is",output1
    
def get_number():
   
    output1=raw_input("enter the number\n")
    output1=int(output1)
    return output1
    
# Main starts from here
num1 = get_number()
#num2 = get_number()
perform_check(num1)
#perform_check(num2)
