# Reading Files
ar=[]
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
       if word==word2:
        counter=counter+1
     if word not in ar:
      ar.append(word)
     print('word repeated ', word, counter)



'''
with open('c:/test/bc.txt')as file_object:
    content = file_object.read()
    print(content)
'''