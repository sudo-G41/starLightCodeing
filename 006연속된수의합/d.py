from sys import stdin
input = stdin.readline

N = int(input().strip())
m = 1
sigma = (m-1)*m//2
ans = 0

while(N>sigma):
	ans += 1 if not (N-sigma)%m else 0
	m += 1
	sigma = (m-1)*m//2
print(ans)
