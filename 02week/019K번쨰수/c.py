from sys import stdin
def myInput():
    return stdin.readline().strip()
input = myInput

def solution():
	N, K = map(int, input().split())
	L = list(map(int, input().split()))
	L.sort()
	return L[K-1]

if(__name__ == "__main__"):
	print(solution())