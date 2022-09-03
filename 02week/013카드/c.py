from sys import stdin
def myInput():
    return stdin.readline().strip()
input = myInput

class Node:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = next

class MyDeck:
    def __init__(self) -> None:
        self.front = None
        self.top = None
        self.size = 0
        self.empty = False
    
    def push(self, val:int) -> None:
        if(not self.empty):
            self.front = self.top = Node(val)
            self.empty = True
        else:
            self.top.next = Node(val)
            self.top = self.top.next
        self.size += 1

    def pop(self) -> bool:
        if(self.size > 2):
            self.top.next = self.front.next
            self.front = self.front.next.next
            self.top = self.top.next
            self.top.next = None
            self.size -= 1
            return True
        ########아주 약간의 성능 향상을 위해....########
        elif(self.size == 2):
            self.front = self.top
            self.top.next = None
            self.size -= 1
            return True

        self.front = None
        self.top = None
        return False

    def print(self) -> None:
        node = self.front
        print("[",end="")
        while(True):
            print(F"{node.val}",end="")
            if(node.next):
                print(F",",end="")
                node = node.next
            else:
                break
        print("]")

class NewDeck:
    def __init__(self) -> None:
        self.front = None
        self.top = None
    
    def push(self, val:int) -> None:
        if(self.top):
            self.top.next = Node(val)
            self.top = self.top.next
        else:
            self.front = self.top = Node(val)

    def pop(self) -> bool:
        if(self.front.next != self.top):
            self.top.next, self.top, self.front = self.front.next, self.front.next, self.front.next.next
            self.top.next = None
            return True
        elif(self.front != self.top):
            self.front = self.top
            self.top.next = None
            return True
        elif(self.front):
            self.front = None
            self.top = None
        return False

    def empty(self):
        return bool(self.front)

    def print(self) -> None:
        node = self.front
        print("[",end="")
        while(True):
            print(F"{node.val}",end="")
            if(node.next):
                print(F",",end="")
                node = node.next
            else:
                break
        print("]")

def solution(deck):
    while(len(deck)>1):
        tmp = [v for i, v in enumerate(deck) if i%2 == 1]
        if len(deck)%2 ==1:
            tmp = [deck[-1]]+tmp
        deck = tmp
    return deck[0]

def solution2(deck):
    my_deck = MyDeck()
    for card in deck:
        my_deck.push(card)
    while(my_deck.size > 1):
        my_deck.pop()
    return my_deck.front.val

def solution3(deck):
    new_deck = NewDeck()
    for card in deck:
        new_deck.push(card)
    while(new_deck.front != new_deck.top):
        new_deck.pop()
    
    return new_deck.front.val

if(__name__ == "__main__"):
    deck = [i for i in range(1,int(input())+1)]
    print(f"solution1 : {solution(deck)}")
    print(f"solution2 : {solution2(deck)}")
    print(f"solution3 : {solution3(deck)}")