#!/usr/bin/python
def require_table(num):
    i=1
    while i<=10:
    	print num,'*',i,'=', num*i
        i=i+1


def table_digit():
    a=raw_input("Enter the required number for table\n")
    a=int(a)
    return a 
        
user=table_digit()
require_table(user)

