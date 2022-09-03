from sys import stdin
input = stdin.readline

def solution():
	N = int(input().strip())
	A = {}
	ans = 0
	for n in map(int, input().strip().split()):
		if(n in A):
			A[n] += 1
		else:
			A[n] = 1
	
	S = list(A.keys())
	S.sort()
	
	for k in S:
		l = 0
		r = len(S)-1
		if(A[S[l]]>1 and 2*S[l] == k):
			if(S[l] != k or A[k]>2):
				ans += A[k]
		elif(A[S[r]]>1 and 2*S[r] == k):
			if(S[l] != k or A[k]>2):
				ans += A[k]
		else:
			while(l<r):
				if(S[l]+S[r] < k):
					l += 1
					if(A[S[l]]>1 and 2*S[l] == k):
						if(S[l] != k or A[k]>3):
							ans += A[k]
							break
				elif(S[l]+S[r] > k):
					r -= 1
					if(A[S[r]]>1 and 2*S[r] == k):
						if(S[r] != k or A[k]>3):
							ans += A[k]
							break
				else:
					if((S[l] != k and S[r] != k) or A[k]>1):
						ans += A[k]
						break
					else:
						l += 1
						r -= 1
	return ans

def answer():
	N = int(input().strip())
	if(N<3):
		input()
		return 0
	X = list(map(int, input().strip().split()))
	ans = 0
	X.sort()
	for n in range(N):
		l = 0 if n > 0 else 1
		r = N-1 if n < N-1 else N-2
		while(l<r):
			sum_num = X[l]+X[r]
			if(sum_num < X[n]):
				l += 1
				if(l == n):
					l += 1
			elif(sum_num > X[n]):
				r -= 1
				if(r == n):
					r -= 1
			else:
				ans += 1
				break
	return ans

if(__name__ == "__main__"):
	print(answer())
