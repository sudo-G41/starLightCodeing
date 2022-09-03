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
절대값을 기준으로 루트부터 시작하여 현재 노드보다 삽입되는 값의 절대값이 작은 값이면 자신의 왼쪽 서브트리에 삽입을 하고 큰값이면 오른쪽 서브트리에 삽입한다.  
그러면 같은 값이면 어디에 넣어야 할까? 그때는 절대값이 아닌 그 값이 현재 노드보다 작으면 왼쪽 크면 오른쪽서브트리에 넣어주는데 이것조차 같으면 어떻게 해야 하는가?  
이 부분은 사실 어디에 넣어도 상관 없다. 다만 우리가 pop을 할 때 절대값의 최소값을 찾아 pop해주므로 pop을 하기위해 탐색 할 때 더 적은 탐색을 위해 오른쪽에 넣는 방식을 채택하였다. 그 이유는 삭제 부분에서 이야기 하겠다.  
1. 삭제  
우리가 pop하려는 값은 절대값이 가장 작은 수이면서 같은 값일 경우 값이 작은 수이다. 즉 자신보다 작은 수는 왼쪽 서브트리에 있는 수만 확인 하면 된다는 이야기이다. 그러므로 자신의 왼쪽 자식노드가 없다면 그 값이 최소값이 된다.  
여기서 삽입에서 같은 값일 경우 오른쪽에 넣는 이유가 나오는데 왼쪽에 삽입하건 오른쪽에 삽입하건 삽입은 같은 깊이까지 탐색을 해야 하지만 삭제는 왼쪽을 쭉 따라 가므로 같은 값이 오른쪽에 들어 있을 경우 처음 들어온 같은 값에서 삭제 연산을 실행 하지만 왼쪽에 넣을 경우 처음 들어온 같은 값부터 마지막에 들어온 같은 값 까지 전부 확인해야 하는 상황이 발생한다.  
이걸 바꿔 이야기 하면 지우려는 숫자 n이 있고 n이 m개가 있다 하면 할 때 오른쪽에 넣을 경우 x번을 따라가며 찾았다면 하면 왼쪽에 넣을 경우 x+m번을 따라가면 찾아야 한다.  
이제 삭제할 대상을 찾는 것을 알아 봤으니 어떻게 삭제 하는가를 알아보자  
삭제할 최소값인 노드의 부모노드를 기준으로 봤을 때 삭제할 노드를 루트로 가지는 서브트리는 전부 작은 수 즉 왼쪽 서브트리가 된다. 그리고 삭제할 노드는 왼쪽 서브트리가 없으므로 부모노드가 해당 노드의 오른쪽 서브트리를 가리키게 된다면 전체 트리에서 해당 노드는 알 수 없는 즉 삭제와 같은 취급이 되므로 부모노드를 자신의 오른쪽 자식노드를 가리키게 하면 되고 지워진 노드인 자신의 값을 리턴하면 된다.  
그리고 루트노드가 None이면 그냥 0을 리턴 해준다.

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
```

## 잡담