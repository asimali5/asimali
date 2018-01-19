def make_album(a_name,a_title,traces=''):
    if traces=='':
     dict={a_name:a_title}
    else:
     dict = {a_name: a_title}
     dict['traces'] = traces
    return dict
'''
b=make_album('sec','dildil')
c=make_album('third','newone','4')

print(a)
print(b)
print(c)
'''
cust_inp=''
while cust_inp!='quit':
    inp1 = input("Pls enter artist name")
    inp2 = input("Pls enter artist title")
    if cust_inp!='quit':

      f_inp=make_album(inp1,inp2)
    else:
        cust_inp=inp1

print(f_inp)