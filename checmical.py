def do_action(present, redmark, bluemark):
    if present >= redmark:
    	print "send sms to guys to stop the valve"
    elif present <= bluemark:
	print "shut the valve"
    else:
	print "normal level"
	


def get_current_level():
    present=raw_input("Enter the quanity")
    present=int(present)
    return present

# Main starts from here
capacity = 900
high = capacity+capacity*20/100
low = capacity-capacity*20/100
level = get_current_level()
do_action(level, high, low)


