ar=[]
customer_inp=''

while customer_inp!='quit':
    toppings=input("Please enter toppings")
    if toppings!='quit':
     ar.append(toppings)
    else:
     customer_inp=toppings
a=0
print(ar)
leng=len(ar)
for p_toppings in ar:
    if a==(leng-1):
        print("sorry we are out of",p_toppings)
    else:
        print("yes we can provide this topping", p_toppings)
    a=a+1
print(ar)
print(a)
