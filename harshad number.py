num=125
copy=num
sum=0
while num!=0:
    ld=num%10
    sum+=ld
    num//=10
if copy%sum==0:
    print('harshad number')
else:
    print('not harshad number')
