from sys import stdin
def myInput():
    return stdin.readline().strip()
input = myInput
N = int(input())
L = list(map(int, input().split()))
tmp = [0]*N
def list_merge(i,m,j):
  global L
  global tmp
  l = idx = i
  r = m
  ans = 0
  while(l!=m and r!=j):
    if(L[l]>L[r]):
      tmp[idx] = L[r]
      r+=1
    else:
      tmp[idx] = L[l]
      ans += (r-m)
      l+=1
    idx+=1
  if(l!=m):
    while(l!=m):
      ans += (r-m)
      tmp[idx] = L[l]
      l+=1
      idx+=1
  else:
    while(r!=j):
      tmp[idx] = L[r]
      r+=1
      idx+=1
  for x in range(i,j):
    L[x] = tmp[x]
  return ans

def list_split(l,r):
  ans = 0
  if(l!=r-1):
    m = (l+r)//2
    ans += list_split(l,m)
    ans += list_split(m,r)
    ans += list_merge(l,m,r)
  return ans

if(__name__ == "__main__"):
  print(list_split(0,N))
