def make_album(a_name,a_title,traces=''):
    if traces=='':
     dict={a_name:a_title}
    else:
     dict = {a_name: a_title}
     dict['traces'] = traces
    return dict

a=make_album('first','def')
b=make_album('sec','dildil')
c=make_album('third','newone','4')

print(a)
print(b)
print(c)

