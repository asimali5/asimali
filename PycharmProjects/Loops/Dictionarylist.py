import random
lista=[]
listb=[]
with open('bc.txt')as f_object:
 c = f_object.read()
 for a in c.split():
    lista.append(a)


v=random.choice(lista)
lent=len(v)
with open('bc.txt')as file_object:
 contents = file_object.read()
#print(contents.find(v))
#print(v)
#print(lista)

cont = c[contents.find(v)+lent:]
print(cont.split())
for e in cont.split():
    listb.append(e)
print(v)
print(listb)
print(lent)

# z = random.choice(lista)

# for a in contents.split():
 #    lista.append(a)
 #z=random.choice(lista)
 #search_text=z.index(contents)

 #print(search_text)
 #print(z)
 #print(contents)
 #print(lista)
 #for word in contents.split():


#for b in range(10):
#  aw.update({b:al})
#print(aw.items())
