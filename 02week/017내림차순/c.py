from sys import stdin
def myInput():
    return stdin.readline().strip()
input = myInput

def solution():
	sort_table = [0,0,0,0,0,0,0,0,0,0]
	for i in input():
		sort_table[9-int(i)] += 1
	s = ""
	for i, v in enumerate(sort_table):
		if(v>0):
			s += str(9-i)*v
	return s

if(__name__ == "__main__"):
	print(solution())