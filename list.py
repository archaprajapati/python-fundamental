##     0    1      2     3     4         5   6     7   8    9     10         11  12 13   14   15      
l=["Hello",123,"Python",6.7,"firstlist",654,False,True,5.5,1225,"Newlist","Start",6,54,35.45,"Done"]
##   16     15  14      13     12        11  10    9    8   7      6         5    4  3   2     1


print(l)
##l.clear()
##print(l)
l.append(1111)
print(l)

l1=l.copy()
print(l1)
l1.append(2222)
print(l)
print(l1)

l2=l1
print(l2)
l2.append(3333)
print(l2)
print(l1)


print(l.count(1))

l3=[100,200,300,400]
l.extend(l3)
print(l)

print(l.index(1225))
l.insert(9,2512)
print(l)

l.pop()
print(l)
l.pop(11)
print(l)
l.remove(654)
print(l)
l.reverse()
print(l)

for i in l:
    print(i)
print(1225 in l)
    
##print(l[4:11:3])
##print(l[:13:6])
##print(l[::3])
##print(l[2::2])
##print(l[2:15:3])
##print(l[2:])
##print(l[-15:-2])
##print(l[-14:])
##print(l[-15:-4:2])
##print(l[::-1])
##print(l[::-3])


##1.  firstlist true newlist
##2.  hello false 6
##3.  hello 6.7  false 1225  6
##4.  python firstlist false  5.5  newlist  6  35.45
##5.  python 654  5.5  start 35.45
##6.  python 6.7  firstlist  654  false  true  5.5  1225  newlist  start 6 54 35.45
##7.  123  Python  6.7  firstlist  654 False True 5.5  1225 Newlist  Start  6 54
##8.  Python",6.7,"firstlist",654,False,True,5.5,1225,"Newlist","Start",6,54,35.45
##9.  123,6.7,  654  true  1225  start
##10.  Hello",123,"Python",6.7,"firstlist",654,False,True,5.5,1225,"Newlist","Start",6,54,35.45,"Done
##11. done 6  1225  false  6.7

##['firstlist', True, 'Newlist']
##['Hello', False, 6]
##['Hello', 6.7, False, 1225, 6, 'Done']
##['Python', 'firstlist', False, 5.5, 'Newlist', 6, 35.45]
##['Python', 654, 5.5, 'Start', 35.45]
##['Python', 6.7, 'firstlist', 654, False, True, 5.5, 1225, 'Newlist', 'Start', 6, 54, 35.45, 'Done']
##[123, 'Python', 6.7, 'firstlist', 654, False, True, 5.5, 1225, 'Newlist', 'Start', 6, 54]
##['Python', 6.7, 'firstlist', 654, False, True, 5.5, 1225, 'Newlist', 'Start', 6, 54, 35.45, 'Done']
##[123, 6.7, 654, True, 1225, 'Start']
##['Done', 35.45, 54, 6, 'Start', 'Newlist', 1225, 5.5, True, False, 654, 'firstlist', 6.7, 'Python', 123, 'Hello']
##['Done', 6, 1225, False, 6.7, 'Hello']
