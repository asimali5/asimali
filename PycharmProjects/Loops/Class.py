#find odd

'''
def findodd(a):
  if a % 2==0:
     print(a)
  else:
    print ("not odd")


findodd(5)
'''
############################################3

def findprime(b):
 d =b+1
 for c in range(2,d):
   '''
   print("first loop")
   print("value of variable C",c)
   e=False
   '''
   g=0
   for f in range(2,d):
     '''
     print ("sec loop")
     print("value of F & D",f,d)
     print("value of variable C", c)
     print(c/f)
     '''
     if c % f==0:
      g = g + 1
     if(c/f==1 and g==1):
      print("Prime number",f)
      print("###########")


findprime(10)




