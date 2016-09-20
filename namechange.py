#!/usr/bin/python
def get_username():
        
	 abc=raw_input("enter the user name\n")
         return abc
def say_hello(user):
        
    	print "Hello", user
        
        
# Main starts from below
name = get_username()
say_hello(name)
