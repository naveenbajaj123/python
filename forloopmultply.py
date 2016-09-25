def require_table(num):
    for i in range(1,11):
    	#for j in range(1,11):
        print num,'*',i,'=',num*i


def table_digit():
    a=raw_input("Enter the required number for table\n")
    a=int(a)
    return a 
        
user=table_digit()
require_table(user)

