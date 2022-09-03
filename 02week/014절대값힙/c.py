from sys import stdin
def myInput():
    return stdin.readline().strip()
input = myInput
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

def solution():
    bst = BST()
    # bst.print()
    for _ in range(int(input())):
        x = int(int(input()))
        # print(f"x:{x}")
        if(x == 0):
            print(f"{bst.pop()}")
        else:
            bst.push(x)
        # bst.print()

if(__name__ == "__main__"):
	solution()