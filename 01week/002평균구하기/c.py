from sys import stdin
input = stdin.readline

N = int(input().strip())

l = list(map(int,input().strip().split()))
max_num = max(l)
sum_num = 0
for num in l:
	sum_num+=(num/max_num*100)
print(sum_num/N)
