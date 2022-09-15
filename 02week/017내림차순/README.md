# 백준[2750](https://www.acmicpc.net/problem/2750)
## 문제
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
## 입력
첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
## 출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
## 풀이
책에서는 삽입정렬을 원하지만 그냥 기수정렬 때려버렸다.  
기수정렬 인터넷에 많으니 그냥 인터넷 보는게 좋을겁니다...

```python
def solution():
	sort_table = [0,0,0,0,0,0,0,0,0,0]
	for i in input():
		sort_table[9-int(i)] += 1
	s = ""
	for i, v in enumerate(sort_table):
		if(v>0):
			s += str(9-i)*v
	return s
```

## 잡담
이거 sorted쓰는게 빠르던데 아무래도 O( $N$ )의 N이 10밖에 안되서 내 방식은 20인데 sorted는 10 * $log$ 10이라서 더 빠른듯?
sorted 안 쓸거면 그냥 이진탐색 섞어서 삽입정렬 할 걸 잘못했나? 대충
``` python
def solution2():
	st = list(input())
	L = [st.pop()]
	for r, v in enumerate(st):
		l = 0
		r += 1
		while(l!=r):
			mid = l+(r-l)//2
			if(v>L[mid]):
				r = mid
			else:
				l = mid+1
		if(l<len(L)):
			L.insert(l, v)
		else:
			L.append(v)
	return "".join(L)
```
느낌으로?