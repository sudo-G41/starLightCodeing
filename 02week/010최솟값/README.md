# 백준[11003](https://www.acmicpc.net/problem/11003)
## 문제
$N$ 개의 수 $A_1$ , $A_2$, ... , $A_N$ 과 $L$ 이 주어진다.

$D_i$ = $A_i-L$+1 ~ $A_i$ 중의 최솟값이라고 할 때, $D$ 에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, $i$ ≤ 0 인 $A_i$ 는 무시하고 $D$ 를 구해야 한다.

## 입력
첫째 줄에 N과 L이 주어진다. (1 ≤ $L$ ≤ $N$ ≤ 5,000,000)

둘째 줄에는 N개의 수 Ai가 주어진다. (-10<sup>9</sup> ≤ $A_i$ ≤ 10<sup>9</sup>)


## 출력
첫째 줄에 $D_i$를 공백으로 구분하여 순서대로 출력한다.

## 풀이
나는 이 문제를 $i$ 부터 $j$ 의 구간의 최소값을 묻는 문제라 보고 풀었다.  
특정 구간에 대해 묻는 문제에 사용 하는 자료구조인 Segment tree라는 자료구조가 있어 그 방법으로 접근해 보았다.  
Segment tree는 간단히 설명 하면 이진트리의 하나로 배열 $A$ 가 있을 때 leaf 노드는 집합 $A$ 의 원소들이며 그 외 노드들은 두 자식노드의 관계(합, 차, 최소, 최대 등)에 대한 답을 값으로 가진다.  
이러한 특징에 의해 각 노드들은 자신의 서브트리의 leaf 노드의 구간에 대한 관계의 답을 가지게 되어 해당 원하는 두 구간의 노드의 처음으로 만나는 공통 부모노드를 찾게 되면 구간에 대한 관계의 답을 얻게 되고 이는 최악의 경우에도 트리의 깊이 만큼의 시간이 걸리는데 이 깊이가 최대 $log_2N$ 이어서 $O$( $log_2N$ )의 성능이 보장된다.  
Segment tree는 재귀를 통해 이진트리로 구현도 된다고 하는데 내가 배운 방법은 완전이진트리를 이용한 방법이고 완전이진트리는 배열을 이용하여 표현이 가능하므로 배열을 이용한 완전 이진트리로 구현하는 방법에 대해 이야기 하겠다.  
우선은 집합 $A$ 가 있다고 할 때 집합의 크기를 $N$ 이라 하면 $N$개의 리프노드를 가지는 완전이진트리는 정 이진트리(Full binary tree)의 형태로 했을 경우 최소의 노드로 구현이 가능하고 정 이진트리는 leaf 노드의 수가 전체 노드의 수/2+1 로 구현이 되므로 Segment tree의 전체 크기는 $N$ + $N$ +1이면 되지만 Segment tree의 크기를 2* $N$ 으로 설정하면 루트노드를 인덱스 1로 놓을 수 있어서 탐색이 좀더 쉬워지고 구간을 구하려고 하는 집합을 $A$라 하고 Segment tree 를 $ST$라 하면 $A_i$는 $ST$_i$<sub>+</sub> $_N$위치 시켜 leaf 노드로 만들 수 있다.  
그러면 나머지 $ST_n$ <sub>-1</sub>부터 $ST_1$ 까지는 완전 이진트리의 특징을 이용하여 채워주는데 루트노드가 $ST$ 의 인덱스 1에 위치한다면 모든 노드의 자식노드는 자신의 인덱스/2 와 자신의 인덱스/2+1에 위치하게 되어 $ST_i$ = $ST$ <sub> $i/2$ </sub>와 $ST$ <sub> $i/2+1$ </sub>의 관계에 대한 답을 넣어 주어 구성하면 된다.  
예를 들어 $A$ 가 {1,2,3,4,5}라고 가정하면 $ST$ 를 구간 합에 대하여 구성하면 아래 그림과 같이 구성이 될 것이다.(루트는 인덱스 1)  
![그림1](https://raw.githubusercontent.com/sudo-G41/starLightCodeing/7e70bb63faac494c851ec18c4717c5b811f59500/02week/010%EC%B5%9C%EC%86%9F%EA%B0%92/%EB%AC%B4%EC%A0%9C1_20220904131652.png)  
그림을 보면 [ $i$ , $j$ )라 적혀있는 것을 볼 수 있는데 이는 $i$ < $X$ &le; $j$ 의 구간의 합을 나타낸다는 의미이다.  


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
