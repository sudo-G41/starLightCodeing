# 백준[11003](https://www.acmicpc.net/problem/11003)
## 문제
N개의 수 A1, A2, ..., AN과 L이 주어진다.

Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.

## 입력
첫째 줄에 N과 L이 주어진다. (1 ≤ L ≤ N ≤ 5,000,000)

둘째 줄에는 N개의 수 Ai가 주어진다. (-109 ≤ Ai ≤ 109)


## 출력
첫째 줄에 Di를 공백으로 구분하여 순서대로 출력한다.

## 풀이


```python
def solution():
        N, L = map(int, input().split())
        A = list(map(int, input().split()))
        segment_tree = [0]*(N<<1)
        D = []
        def init(st, a, n):
                for i in range(n):
                        st[i+n] = a[i]
                for i in range(n-1, 0, -1):
                        l = st[i<<1]
                        r = st[i<<1|1]
                        st[i] = l if l<r else r

        def query(st, n, i, j):
                i += n
                j += n
                result = st[i]
                while(i!=j):
                        if(i&1):
                                result = st[i] if st[i] < result else result
                                i += 1
                        if(j&1):
                                j -= 1
                                result = st[j] if st[j] < result else result
                        i >>= 1
                        j >>= 1
                return result

        init(segment_tree, A, N)
        for j in range(1,N+1):
                i = j-L if j-L>0 else 0
                D.append(str(query(segment_tree, N, i, j)))
        return D
```

## 잡담
아니 이거 세그먼트 왜 안됨????? 연산 횟수가 대략 2억개 인건 맞긴 한데 그래도 2.4초인데??????? 너무하네....  
init 할 때 2N이고 하나 query 하나당 최악 logN이니까 전체 탐색이 NlogN인데 그럼 2N+NlogN인데 왜??????인아웃 그리고 출력이 확실히 시간 잡아먹네... ㄱ...