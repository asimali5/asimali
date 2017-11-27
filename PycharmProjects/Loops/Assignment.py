def fix_start(s):
    a=s[0]
    b=s[1:]
    #print(a+ b.replace(a,"*"))
   # s=a+ b.replace(a,"*")
    c=b.replace(a,"*")
    print(c)

fix_start('bubbles')