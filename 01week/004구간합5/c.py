from sys import stdin
input = stdin.readline

N, M = map(int, input().strip().split())

A = [[0 for _ in range(N+1)]] + [[0]+list(map(int,input().strip().split())) for _ in range(N)]

x = y = 1
while(y<=N):
	if(x<=N):
		A[y][x] += A[y-1][x]+A[y][x-1]-A[y-1][x-1]
		x+=1
	else:
		y+=1
		x=1

for _ in range(M):
	x1,y1,x2,y2 = map(int, input().strip().split())
	x1-=1
	y1-=1
	print(A[x2][y2]-A[x1][y2]-A[x2][y1]+A[x1][y1])
