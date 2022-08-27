# 백준[11659](https://www.acmicpc.net/problem/11659)
## 문제
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

## 출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

## 풀이
0~n까지의 합을 구한 배열을 만들어두고 j-(i-1)을 계산하면 j~i사이의 구간의 합을 구할 수 있다.

```pyhon
N,M = map(int,input().strip().split())
l = list(map(int,input().strip().split()))
ll = [l.pop(0)]
idx = 0
while(idx<len(l)):
	ll.append(ll[idx]+l[idx])
	idx += 1

ll = [0]+ll
for _ in range(M):
	i,j = map(int,input().strip().split())
	i -= 1
	print(ll[j]-ll[i])

```

## 잡담
이거 세그먼트 트리 써도 되기는 하는데 구현 귀찮으니 패스 나중에 시간 나면하넌 고려 해보자.