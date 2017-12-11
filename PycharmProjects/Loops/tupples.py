dims=(100,300,200)
#for dim in dims:
#    print(dims)

s=("abc","dd")#packing
x=list(s)
x[0]="a"
s=tuple(x)
print(s)
#dims[0]=400
#for dim in dims:
#    print(dims)

#dims=(400,500,600)
#for dim in dims:
#    print(dims)

ar=[]
for dim in dims:
 ar.append(dims)

ar[0]=700
dims=ar


print(dims)


