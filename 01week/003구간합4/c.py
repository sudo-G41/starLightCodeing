from sys import stdin
input = stdin.readline

N,M = map(int,input().strip().split())
l = list(map(int,input().strip().split()))
ll = [l.pop(0)]
idx = 0
while(idx<len(l)):
	ll.append(ll[idx]+l[idx])
	idx += 1

ll = [0]+ll
for _ in range(M):
	i,j = map(int,input().strip().split())
	i -= 1
	print(ll[j]-ll[i])
