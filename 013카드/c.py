from sys import stdin
def myInput():
    return stdin.readline().strip()
input = myInput

# def solution():
#     deck = [i for i in range(1,int(input())+1)]
#     while(len(deck)>1):
#         deck.pop(0)
#         deck.append(deck.pop(0))
#     return deck[0]
def solution():
    deck = [i for i in range(1,int(input())+1)]
    while(len(deck)>1):
        tmp = [v for i, v in enumerate(deck) if i%2 == 1]
        if len(deck)%2 ==1:
            tmp = [deck[-1]]+tmp
        deck = tmp
    return deck[0]

if(__name__ == "__main__"):
	print(solution())