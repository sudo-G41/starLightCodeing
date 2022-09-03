from sys import stdin
def myInput():
    return stdin.readline().strip()
input = myInput

class TreeNode:
    def __init__(self, val, left=None, right=None, height=1):
        self.val = val
        self.left = left
        self.right = right
        self.height = height # 높이를 뜻하는 height 속성 추가 기본값=1
 
 
class AVLtree:
    def __init__(self, val):
        self.root = TreeNode(val)
 
    def insert(self, val):
        self.root = self._insert_node(self.root, val)
 
    def delete(self, val):
        self.root = self._delete_node(self.root, val)
 
    def _insert_node(self, cur, val):
        if not cur:
            return TreeNode(val)
        elif val < cur.val:
            cur.left = self._insert_node(cur.left, val)
        else:
            cur.right = self._insert_node(cur.right, val)
 
        cur.height = 1 + max(self._get_height(cur.left),
                             self._get_height(cur.right))
 
        balance = self._get_balance(cur)
        if balance > 1 and val > cur.left.val: # Left-Right case
            cur.left = self._left_rotate(cur.left)
            cur = self._right_rotate(cur)
 
        elif balance > 1 and val < cur.left.val: # Left-Left case
            cur = self._right_rotate(cur)
 
        elif balance < -1 and val > cur.right.val: # Right-Right case
            cur = self._left_rotate(cur)
 
        elif balance < -1 and val < cur.right.val: # Right-Left case
            cur.right = self._right_rotate(cur.right)
            cur = self._left_rotate(cur)
        return cur
 
    def _delete_node(self, cur, val):
        if not cur:
            return False
        elif cur == self.root and cur.val == val:
            if cur.left and cur.right:
                pre_val = self._find_predecessor(cur.left)
                self._delete_node(cur, pre_val)
                cur.val = pre_val
            elif cur.left or cur.right:
                if cur.left:
                    self.root = cur.left
                elif cur.right:
                    self.root = cur.right
            else:
                self.root = None
 
        elif cur.left and cur.left.val == val:
            if cur.left.left and cur.left.right:
                pre_val = self._find_predecessor(cur.left.left)
                self._delete_node(cur, pre_val)
                cur.left.val = pre_val
                cur.left.height = 1 + \
                    max(self._get_height(cur.left.left),
                        self._get_height(cur.left.right))
            elif cur.left.left or cur.left.right:
                if cur.left.left:
                    cur.left = cur.left.left
                elif cur.left.right:
                    cur.left = cur.left.right
                cur.left.height = 1 + \
                    max(self._get_height(cur.left.left),
                        self._get_height(cur.left.right))
            else:
                cur.left = None
            cur.height = 1 + max(self._get_height(cur.left),
                                 self._get_height(cur.right))
 
        elif cur.right and cur.right.val == val:
            if cur.right.left and cur.right.right:
                pre_val = self._find_predecessor(cur.right.left)
                self._delete_node(cur, pre_val)
                cur.right.val = pre_val
                cur.right.height = 1 + \
                    max(self._get_height(cur.right.left),
                        self._get_height(cur.right.right))
            elif cur.right.left or cur.right.right:
                if cur.right.left:
                    cur.right = cur.right.left
                elif cur.right.right:
                    cur.right = cur.right.right
                cur.right.height = 1 + \
                    max(self._get_height(cur.right.left),
                        self._get_height(cur.right.right))
            else:
                cur.right = None
            cur.height = 1 + max(self._get_height(cur.left),
                                 self._get_height(cur.right))
 
        elif cur.val > val:
            cur.left = self._delete_node(cur.left, val)
 
        elif cur.val < val:
            cur.right = self._delete_node(cur.right, val)
 
        balance = self._get_balance(cur)
        # Left-Left case
        if balance > 1 and self._get_balance(cur.left) >= 0:
            cur = self._right_rotate(cur)
        # Left-Right case
        elif balance > 1 and self._get_balance(cur.left) < 0:
            cur.left = self._left_rotate(cur.left)
            cur = self._right_rotate(cur)
        # Right-Left case
        elif balance < -1 and self._get_balance(cur.right) > 0:
            cur.right = self._right_rotate(cur.right)
            cur = self._left_rotate(cur)
        # Right-Right case
        elif balance < -1 and self._get_balance(cur.right) <= 0:
            cur = self._left_rotate(cur)
        return cur
 
    def _find_predecessor(self, cur):
        if cur.right:
            return self._find_predecessor(cur.right)
        else:
            return cur.val
 
    def _left_rotate(self, cur):
        v = cur
        w = cur.right
        t = w.left
        cur = w
        w.left = v
        v.right = t
        v.height = 1 + max(self._get_height(v.left), self._get_height(v.right))
        w.height = 1 + max(self._get_height(w.left), self._get_height(w.right))
        return cur
 
    def _right_rotate(self, cur):
        v = cur
        w = cur.left
        t2 = w.right
        cur = w
        w.right = v
        v.left = t2
        v.height = 1 + max(self._get_height(v.left), self._get_height(v.right))
        w.height = 1 + max(self._get_height(w.left), self._get_height(w.right))
        return cur
 
    def _get_height(self, cur):
        if not cur:
            return 0
        return cur.height
 
    def _get_balance(self, cur):
        if not cur:
            return 0
        return self._get_height(cur.left) - self._get_height(cur.right)
 
    def traverse(self):
        return self._print(self.root, [])
 
    def _print(self, cur, result):
        if cur:
            self._print(cur.left, result)
            result.append(cur.val)
            self._print(cur.right, result)
        return result

    def mins(self):
        node = self.root
        if not node:
            return int(1e9)+1
        while node.left:
            node = node.left
        return node.val

def solution():
    N, L = map(int, input().split())
    A = list(map(int, input().split()))
    end = 0
    D = []
    bbst = AVLtree(int(1e9+1))
    for start, Ai in enumerate(A):
        bbst.insert(Ai)
        if(start - end == L):
            bbst.delete(A[end])
            end += 1
        print(bbst.traverse())
        D.append(bbst.mins())
        
    return D

if(__name__ == "__main__"):
    print(" ".join(map(str,solution())))
