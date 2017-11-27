'''
for c in range(11, 0,-1):
    print("first loop",c)

for c in range(1, 11):
     print("first loop", c)'''

#print("|", end="")
#print("|", end="")
'''
for i in range(1,11):
   print(i,"|",end="")'''
#############################
'''
rows=6
for i in range(rows):
#print((' ' * (rows - i - 1) + '*' * (2 * i + 1)))
  #print((' ' * (2 * i + 1)+'*'))
 #print(' ' * (rows-i) + '*' * (2*i+1))
  print(' ' * (rows-i)+'*' *(2*i+1) )
    #print()

'''
#####################################
for i in range(1,5):
   for j in range (1, 5):
       print("|",i*j, "\t", end = "")
       print("|")