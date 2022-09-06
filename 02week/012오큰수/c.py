from sys import stdin
def myInput():
        return stdin.readline().strip()
input = myInput

def solution():
        N = int(input())
        A = list(map(int,input().split()))
        NGE = [0]*N
        s = []
        for i in range(N):
                while(s):
                        if(A[s[-1]] < A[i]):
                                NGE[s.pop()] = A[i]
                        else:
                                break
                s.append(i)
        for i in s:
                NGE[i] = -1
        return NGE

if(__name__ == "__main__"):
        print(" ".join(map(str, solution())))
