available_sandwitch=['tuna_sandwitch','chicken_sandwitch']
finished_sandwitch=[]

cus_inp=''
while cus_inp!='quit':
    order=input('what is your order')
    if order!='quit':
        finished_sandwitch.append(order)
        available_sandwitch.remove(order)
    else:
        cus_inp=order

print(finished_sandwitch)
print(available_sandwitch)