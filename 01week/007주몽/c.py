from sys import stdin
input = stdin.readline

def merge(arr,tmp,l,mid,r):
	left = l
	rigth = mid
	top = l

	while(left<mid and rigth<r):
		if(arr[left]<arr[rigth]):
			tmp[top] = arr[left]
			left += 1
		else:
			tmp[top] = arr[rigth]
			rigth += 1
		top += 1
	if(left==mid):
		while(rigth<r):
			tmp[top] = arr[rigth]
			top += 1
			rigth += 1
	else:
		while(left<mid):
			tmp[top] = arr[left]
			top += 1
			left += 1

	for i in range(l,r):
		arr[i] = tmp[i]

def msort(arr,tmp,l,r):
	if(l<r-1):
		mid = (l+r)//2
		msort(arr,tmp,l,mid)
		msort(arr,tmp,mid,r)
		merge(arr,tmp,l,mid,r)

def solution():
	N = int(input().strip())
	M = int(input().strip())
	L = list(map(int,input().strip().split()))
	tmp = [0]*len(L)
	l = 0
	r = len(L)-1
	ans = 0

	msort(L,tmp,0,len(L))

	while(l < r):
		if(L[l]+L[r] < M):
			l += 1
		elif(L[l]+L[r] > M):
			r -= 1
		else:
			ans += 1
			l += 1
			r -= 1
	
	return ans

if __name__ == "__main__":
	print(f"{solution()}")
