n=int(input("Enter N:"))
while n>0:
    print("Hello")
    n=n-1

'''febonacci'''

n=int(input("Enter N:"))
a,b=0,1
print(a,end=" ")
while b<n:
    print(b,end=" ")
    a,b=b,a+b

'''prime'''

n=int(input("Enter N:"))
if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print(n,"Is Not Prime")
            break
    else:
        print(n,"Is Prime")
else:
    print(n,"Is not Prime")

