def recursiveMethod(num):
    if num<1:
        print ("I'm less than 1")
    else:
        recursiveMethod(num - 1)
        print (num)

recursiveMethod(4)
