import sys
def lcm(a):
    if len(a)==1:
        return a[0]
    if len(a)==2:
        return a[0]*a[1]//gcd((a[0],a[1]))
    return lcm((a[0],lcm(a[1:])))

def gcd(a):
    if len(a)==1:
        return a[0]
    if len(a)==2:
        return gcd((a[1],a[0]%a[1])) if a[1]!=0 else a[0] 
    return gcd((a[0],gcd(a[1:])))

input()
count=0
lcm_a = lcm([int(x) for x in input().strip().split()])
gcd_b = gcd([int(x) for x in input().strip().split()])
for x in range(lcm_a,gcd_b+1,lcm_a):
    if gcd_b%x==0:
        count+=1
print(count)