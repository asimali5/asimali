'''
Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.
'''

megnames=['micheal','Sam','Oliver']

def show_magicians(megicians):
    for mname in megicians:
        print(mname)

def make_great(megnames):
    for names in range(len(megnames)):
        megnames[names]='Great'+' '+megnames[names]
    show_magicians(megnames)

make_great(megnames)

#show_magicians(megnames)