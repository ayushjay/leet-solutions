def hello1():
    hello2()
    print ("Im function 1")

def hello2():
    hello3()
    print ("Im function 2")

def hello3():
    hello4()
    print ("Im function 3")

def hello4():
    print ("Im function 4")


hello1()