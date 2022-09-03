from sys import stdin

input = stdin.readline

N = int(input().strip())
print(sum(map(int,list(input().strip()))))
