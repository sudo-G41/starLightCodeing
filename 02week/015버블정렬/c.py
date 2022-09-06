from sys import stdin
def myInput():
    return stdin.readline().strip()
input = myInput

def solution():
    N = int(input())
    L = [int(input()) for i in range(N)]
    for i in range(N):
        j = 1
        while(j<N-i):
            L[j], L[j-1] = (L[j-1], L[j]) if(L[j]<L[j-1]) else (L[j], L[j-1])
            j += 1
    return L

if(__name__ == "__main__"):
	print("\n".join(map(str,solution())))
