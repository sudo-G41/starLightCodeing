# 백준[2751](https://www.acmicpc.net/problem/2751)
## 문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
## 입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
## 출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
## 풀이
병합정렬 구현해서 써봤다.  
sort함수가 쪼개고 merge함수가 쪼갠것을 정렬하는 방식이다. 자세한건 인터넷에 많이 돌아다니니까 그거 보면 된다.

```python
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
```

## 잡담
아니 퀵이랑 병합은 구현해야 하는 상황이 오미ㅕㄴ 자주 쓰이는 정렬이라 두 문제 다 구현했는데 한문제는 시간초과 되서 안되고 한문제는 2초 제한인데 7000ms로 통과되고 이거 뭐지??????? 뭐지???????????????????????