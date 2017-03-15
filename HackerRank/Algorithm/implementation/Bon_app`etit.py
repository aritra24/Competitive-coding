n,k=[int(a) for a in input().split(' ')]
ar=[int(a) for a in input().split(' ')]
val=int(input())
su=sum(ar)//2-ar[k]//2
if su==val:
    print('Bon Appetit')
else:
    print(val-su)