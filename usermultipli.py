def get_number():
    """ This function should fetch the number from user
        This function should return back this number
    """
    number = raw_input("Eter the user number for table\n")
    number = int(number) 
    return number


def print_mtable(num):
    print "Table of",num
    print num*1;
    print num*2;
    print num*3;
    print num*4;
    print num*5;
    print num*6;
    print num*7;
    print num*8;
    print num*9;
    print num*6;
# Main starts from here
inp = get_number()
print_mtable(inp)
