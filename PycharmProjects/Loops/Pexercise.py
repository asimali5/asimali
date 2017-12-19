
##########DOB calc####################
'''
import datetime

age='10/12/1980'
now=datetime.datetime.now()
a=now.year
b=int(age[6:])
curr_age=a-b
if curr_age<100:
    c=100-curr_age
    d=a+c
print("you are ",a-b," years old")
print("you will be 100 years old in year",d)
'''
######################################
#List less than 10
'''
ar2=[]
contents=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for content in contents:
 if content < 10:
     ar2.append(content)
print(ar2)
'''
######################################
#Divisor
'''
ar=[]
a=int(input("Enter the diversor number"))
for b in range(2,100):
 if b % a ==0:
   ar.append(b)
print(ar)
'''
######################################
#common items in 2 lists
'''
ar=[1,1,1,3,4,5,7,9,11]
ar2=[1,3,5,22,1,44]
ar3=[]
for a in ar:
    for b in ar2:
        if b==a and a not in ar3:
         ar3.append(a)
print(ar3)
'''
######################################








