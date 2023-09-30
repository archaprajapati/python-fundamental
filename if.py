''' 1 if elif'''
'''
a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))
if a>b:
    if a>c:
        print("A is Max")
    else:
        print("C is Max")
elif b>c:
        print("B is Max")
else:
    print("C is Max")'''



''' 2 simple if'''
'''
a=int(input("Enter age"))
if a>18:
    print("You are aligible for votting")
elif a<18:
    print("You are not aligible for votting")
else:
    print("Enter Valid age")
'''

''' 3 leap year'''
'''
year=int(input("Enter a Year"))
if (year%400==0 and year%100!=00) or (year%4==0):
    print("Year is Leap")
else:
    print("Year is not Leap")'''

''' 4 tax'''
'''
income=int(input("Enter Your Income"))
if income <=50000:
    total =income*5/100
    print("Your Payable tax is:",total)
elif income > 50000:
    total= income*10/100
    print("Payable tax is", total)'''

    


