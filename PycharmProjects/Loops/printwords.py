
def print_words(n):
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
         for word2 in contents.split():
           if word.lower()==word2.lower():
            counter=counter+1
         if word not in ar:
          ar.append(word)
         #print('word repeated ', word, counter)
         ar3.update({word.lower():counter})#code append on 11-16-2017 wednesday#
    a3=sorted(ar3.items()) # Printing keys in sorted orders
    g=n#len(ar3)#input variable from user
    f=0 # variable define to check how many rows to print
    a1_sorted_keys = sorted(ar3, key=ar3.get, reverse=True)  # Printing in Reverse orders, it is working fine
    for r in a1_sorted_keys:  # Printing in Reverse orders, it is working fine
        for k, v in a3:
            if f == g:
             break
            else:
             print(r, ar3[r])  # Printing in Reverse orders, it is working fine
             f=f+1
             break
    print('*****************************')

print_words(2)