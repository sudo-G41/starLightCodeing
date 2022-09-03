from sys import stdin
def myInput():
    return stdin.readline().strip()
input = myInput

def solution():
    n = int(input())
    stack = []
    answer = []
    arr = []
    for i in range(n):
        arr.append(int(input()))
    i = 1
    while i < n+2:
        if stack and stack[-1] == arr[0]:
            answer.append('-')
            stack.pop()
            arr.pop(0)
        else:
            stack.append(i)
            i += 1
            answer.append('+')
    stack.pop()
    answer.pop()
    if stack:
        print('NO')
    else:
        for val in answer:
            print(val)

if(__name__ == "__main__"):
	solution()

