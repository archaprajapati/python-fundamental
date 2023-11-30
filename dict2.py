d1={"A":100,"B":200,"C":300}
d2={"A":100,"B":200,"E":400}
d3={}
for i in d1:
    if i in d2:
        d3[i]=d1[i]
print(d3)



d={}
n=int(input("Enter N: "))
for i in range(1,n+1):
    d[i]=i*i
print(d)
