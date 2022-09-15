from sys import stdin
def myInput():
    return stdin.readline().strip()
input = myInput

def solution():
	N = int(input())
	sort_table = [[] for _ in range(1000001)]
	sort_arr = []
	sort_dict = {}

	for i in range(N):
		v = int(input())
		sort_table[v].append(i)
	for v in sort_table:
		if(v):
			sort_arr += v

	ans = 0

	for i in range(N):
		ans = max(ans, sort_arr[i] - i)
	
	return ans+1
	
if(__name__ == "__main__"):
	print(solution())
