from sys import stdin
def myInput():
    return stdin.readline().strip()
input = myInput

tmp = []

def merge(L, l, m, r):
	left = idx = l
	rigth = m
	global tmp
	while(left!=m and rigth!=r):
		if(L[left]>L[rigth]):
			tmp[idx] = L[rigth]
			rigth+=1
		else:
			tmp[idx] = L[left]
			left+=1
		idx+=1
	if(left==m):
		while(rigth<r):
			tmp[idx] = L[rigth]
			rigth+=1
			idx+=1
	else:
		while(left<m):
			tmp[idx] = L[left]
			left+=1
			idx+=1
	while(l<r):
		L[l] = tmp[l]
		l+=1

def sort(L, l, r):
	if(l!=r-1):
		mid = (l+r)//2
		sort(L,l,mid)
		sort(L,mid,r)
		merge(L,l,mid,r)

def solution():
	N = int(input())
	L = [0]*N
	global tmp
	tmp = [0]*N
	for i in range(N):
		L[i] = int(input())
	sort(L,0,N)
	return "\n".join(map(str,L))

if(__name__ == "__main__"):
	print(solution())
