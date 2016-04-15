NUM1 = 100  # Global Variable

def foo(NUM2):
    global NUM1
    NUM1 = NUM2
    print("Global NUM1 = %d" % NUM1)  # Global Variable

foo(1)
print("Global NUM1 = {0}".format(NUM1))  # Global Variable