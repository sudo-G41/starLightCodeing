from sys import stdin
input = stdin.readline

N,M = map(int, input().strip().split())
A = list(map(int,input().strip().split()))
C = [0 for _ in range(M)]

A[0] %= M
C[A[0]] += 1
for i in range(1,N):
	A[i] = (A[i]+A[i-1])%M
	C[A[i]] += 1

for i in range(M):
	C[0]+=(C[i]*(C[i]-1))//2

print(C[0])
