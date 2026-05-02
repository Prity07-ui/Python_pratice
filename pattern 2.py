for i in range(1,6):
    for j in range(1,6):
        print(" ", end=" ")
        for k in range(0,i):
            print("*", end=" ")
        for n in range(i,1,-1):
            print("*", end=" ")
        print(" ")