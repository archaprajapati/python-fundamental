##1 pro.

##n=0
##while n<50:
##    n+=1
##    if n%2==0:
##        print(n,"Number Is Even")
##    else:
##        print(n,"Number Is Odd")


##2 pro.
        
##n=int(input("Enter Number:"))
##for i in range(n+1):
##    
##    if i%2==0:
##        print(i,"Number Is Even")
##
##    else:
##        print(i,"Number Is Odd")

   
##3 pro.

##i=1
##while i<6:
##    print(i)
##    i+=1
##output:- 12345


##4 pro.

##for i in range(1,10,):
##    for j in range(1,i):
##        print(j,end=" ")
##    print("\n")
##
##    output:- 1 12 123 1234

##5 pro.

##for i in range(5,0,-1):
##    for j in range(i,0,-1):
##        print(j,end=" ")
##    print("\n")
##    output:- 54321 4321 321 21 1

##6 pro.

##for i in range(0,6):
##    for j in range(0,i):
##        print(chr(77+j),end=" ")
##    print("\n")
##output:- M MN MNO MNOP MNOPQ

##7 pro.

##n = int(input("Enter number of rows: "))
##
##for i in range(1,n+1):
##    a = 97
##    for j in range(1, i+1):
##        print("%c" %(a), end="")
##        a += 1
##    print()

##output:= a ab abc abcd


##8 pro.

##for i in range(0,6):
##    for j in range(6,i,-1):
##        print(" ",end=" ")
##    for l in range(0,2*i+1):
##        print("*",end=" ")
##    print("\n")


for i in range(0,10):
    for j in range(10,i,-1):
        print(" ",end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print("\n")




    
        
            
    
