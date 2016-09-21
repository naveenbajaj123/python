def perform_check(output1):
  
    if output1>=10 and output1<=99 :
        print "Enter number is two digit"
    elif output1>=100 and output1<=999 :
    	print "Enter number is three digit"
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
