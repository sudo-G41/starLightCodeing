# 백준[11286](https://www.acmicpc.net/problem/11286)
## 문제

절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

    배열에 정수 x (x ≠ 0)를 넣는다.
    배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.

프로그램은 처음에 비어있는 배열에서 시작하게 된다.

## 입력
첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 정수는 -231보다 크고, 231보다 작다.

## 출력
입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

## 풀이
사실 Python에 heapq나 Priority_Queue라는 라이브러리가 이 문제를 구현해 준다. 하지만 공부 하는 마음으로 BST를 이용하여 비슷하게 구현해 보았다.(사실 구현 해도 최소 힙 구현 해야 하는데 그냥 BST로 구현 해봤다... BBST 하고 싶다...)  
BST특징은 이진트리의 자식 노드가 특정 규칙으로 형성되어 있는데 한쪽은 자신보다 큰 수 한쪽은 자신보다 작은 수로 구현 되어 있다는 점이다.  
즉 자신의 서브트리가 전부 자기보다 크거나 또는 작은 숫자로만 구성 되어있다는 점이다.  
여기서 나는 왼쪽 서브트리를 작은 수들로만 오른쪽 서브트리를 큰 수로만 형성 되도록 구현했다.   

우선 트리의 노드 구성을 보면

    val : 값
    abs : 절대값( 이걸 기준으로 정렬)
    left : 왼쪽 자식 노드
    rigth : 오늘쪽 자식 노드

로 구성되어 있다.

다음으로 BST를 설명하자면

1. 삽입  


```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.abs = val if val>0 else -val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def push(self, val)->None:
        def _push(node, val, abs):
            if(node.abs == abs):
                if(node.val>val):
                    if node.left:
                        _push(node.left, val, abs)
                    else:
                        node.left = Node(val)
                else:
                    if node.right:
                        _push(node.right, val, abs)
                    else:
                        node.right = Node(val)
            elif(node.abs > abs):
                if node.left:
                    _push(node.left, val, abs)
                else:
                    node.left = Node(val)
            else:
                if node.right:
                    _push(node.right, val, abs)
                else:
                    node.right = Node(val)

        if(not self.root):
            self.root = Node(val)
        else:
            _push(self.root, val, val if val>0 else -val)

    def pop(self)->int:
        if(not self.root):
            return 0
        node = self.root
        parent = None
        while(node.left):
            parent = node
            node = node.left
        if(node == self.root):
            self.root = node.right
        else:
            parent.left = node.right
        return node.val

    def print(self):
        def _print(node:Node):
            if(node.left):
                _print(node.left)
                print(", ",end="")

            print(f"{node.val}",end="")

            if(node.right):
                print(", ",end="")
                _print(node.right)
        print("[",end="")
        if(self.root):
            _print(self.root)
        print("]")
```

## 잡담