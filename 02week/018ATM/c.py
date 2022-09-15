from sys import stdin
n = stdin.readline()
l = list(map(int,stdin.readline().split()))
l.sort()
n=0
for idx, var in enumerate(l[::-1]):
    n+=(idx+1)*var
print(n)