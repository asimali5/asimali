def print_word():
    ar=[]
    ar3={}
    with open('bc.txt')as file_object:
     contents=file_object.read()
     for word in contents.split():
        if word in ar:
           # print(ar)
            continue
        else:
         counter=0
         fl=len(contents.split())
        #print(fl)
         for word2 in contents.split():
           if word.lower()==word2.lower():
            counter=counter+1
         if word not in ar:
          ar.append(word)
     #    print('word repeated ', word, counter)
         ar3.update({word.lower():counter})#code append on 11-16-2017 wednesday#
         #print(ar3)


    a3=sorted(ar3.items()) # Printing keys in sorted orders
    g=len(ar3) # Input from method, variable define to check how many rows to print
    f=0 # variable define to check how many rows to print
    for k,v in a3:# Printing keys in sorted orders
         print(k,v)# Printing keys in sorted orders
    print('*****************************')

print_word()