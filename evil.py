num=12
count=0
while num!=0:
    ld=num%2
    if ld==1:
        count+=1
    num//=2
if count==2:
    print('evil')
else:
    print('odeous')
