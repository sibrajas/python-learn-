# edit the functions prototype and implementation
def foo(a, b, c, *rest):
    print("Rest is %s" % list(rest))
    return len(list(rest))
    pass

def bar(a, b, c, **arg):
    if (arg.get("magicnumber")==7):
        return True
    else:
        return False
    pass


# test code
if foo(1,2,3,4) == 1:
    print "Good."
if foo(1,2,3,4,5) == 2:
    print "Better."
if bar(1,2,3,magicnumber = 6) == False:
    print "Great."
if bar(1,2,3,magicnumber = 7) == True:
    print "Awesome!"
