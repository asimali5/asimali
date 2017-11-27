
def print_word():
    ar=[]
    ar3={}
    with open('bc.txt')as file_object:
     contents=file_object.read()
     for word in contents.split():
        if word in ar:
          continue
        else:
         counter=0
         fl=len(contents.split())
         for word2 in contents.split():
           if word.lower()==word2.lower():
            counter=counter+1
         if word not in ar:
          ar.append(word)
         ar3.update({word.lower():counter})#code append on 11-16-2017 wednesday#
    a3=sorted(ar3.items()) # Printing keys in sorted orders
    for k,v in a3:# Printing keys wise in asc sorted orders ///comment on 11-17
         print(k,v)# Printing keys,values in sorted orders ///comment on 11-17

print_word()