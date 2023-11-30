
'''n = int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
'''

##n=int(input("Enter rows"))
##for i in range(1,n+1):
##    a = 97
##    for j in range(1, i+1):
##      print("%c" %(a), end="")
##      a += 1
##    print()


##n = int(input("Enter number of rows: "))
##
##for i in range(1,n+1):
##    a = 97
##    for j in range(1, i+1):
##        print("%c" %(a), end="")
##        a += 1
##    print()
##    

##for i in range(1,15):
##    for j in range(1,i+1):
##        print("*",end=" ")
##    print("\n")

for i in range(1,6):
    for j in range(6,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print("*","\n")
