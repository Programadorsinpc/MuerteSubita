import functools 

superpar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
lista= [[9,8,7,6],[5,4,3,2],[1,11,12,13],[14,15,16,17]]


m=list(map(lambda x:[x[0]]+[x[len(x)-1]],lista))
print(m)


r=list(map(int,str(superpar)))
s=list(filter(lambda x: x % 2==0, r))
print(s)


print(functools.reduce(lambda x: x[len(x)-1], lista))
