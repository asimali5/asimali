favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}


ar=['jen','b','c']
for a in ar:
    for b,v in favorite_languages.items():
        #print("value of B is ",b, "value of A is ",a)
        if b==a:
         print("Thanks"+" "+str(b)+" For taking part in pool")
        else:
         print("Dear" + " " + str(b) + " kindly take part in pool")