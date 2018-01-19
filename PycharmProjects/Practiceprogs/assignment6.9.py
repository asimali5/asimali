favorite_places={'my first':'KHI','my sec':'ISB','my third':'LHR'}
f1=''
while f1!='exit':
    f1 = input("enter 1 fav place ")
    if f1=='exit':
     break
    else:
     f2=input("enter 2 fav place ")
     f3=input("enter 3 fav place ")
     favorite_places['friend first']=f1
     favorite_places['friend sec']=f2
     favorite_places['friend third']=f3

print(favorite_places)