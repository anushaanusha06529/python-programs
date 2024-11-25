num=6
res=0
for val in range(1,num):
    if num%val==0:
        res=res+val
if res==num:
    print('perfect number')
else:
    print('not perfect number')
