megnames=['micheal','Sam','Oliver']
def make_great(megnames):
    a=len(megnames)
    for names in range(a):
        megnames[names]='Great'+' '+megnames[names]
    print(megnames)

make_great(megnames)
print(megnames)