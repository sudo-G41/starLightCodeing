from sys import stdin
input = stdin.readline

N = int(input().strip())
if(N>2):
	X = (N>>1) + 1

	ans = 1
	sum_num = 0
	l = r = X
	while(r>0):
		if(sum_num<N):
			sum_num += r
			r -= 1
		else:
			ans += 1 if sum_num == N else 0
			sum_num -= l
			l -= 1
	ans += 1 if sum_num == N else 0
	print(ans)
else:
	print(1)