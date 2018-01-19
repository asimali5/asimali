pet1={'animal type':'monkey','owner':'Mr.A'}
pet2={'animal type':'cat','owner':'Mr.B'}
pet3={'animal type':'dog','owner':'Mr.C'}
ar=[pet1,pet2,pet3]
'''for a in ar:
    print(a)
    for key,value in a.items():
        print("The pet "+a['animal type']+" belongs to "+a['owner'])
'''
for a in ar:
    print("what i know about ",a['animal type'])
    for key, value in a.items():
        print("\t",key, value)