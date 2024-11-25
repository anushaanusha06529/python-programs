num=19
factcount=0
for val in range(1,num+1):
    if num%val==0:
        factcount+=1
if factcount!=2:
    print('composite')
else:
    print('not composite')
