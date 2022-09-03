from sys import stdin
input = stdin.readline

def solution():
	S, P = map(int, input().strip().split())
	DNA = input().strip()
	DNA_key = {'A':0, 'C':1, 'G':2, 'T':3}
	patten = list(map(int,input().strip().split()))
	sub_key = [0] * len(patten)
	p = 0
	ans = 0
	start = end = 0
	yes = (1<<(len(patten)))-1
	for i,v in enumerate(patten):
		if(v==0):
			p |= (1<<i)
		
	for s in DNA:
		sub_key[DNA_key[s]] += 1
		if(sub_key[DNA_key[s]]<patten[DNA_key[s]]):
			p &= ~(1<<DNA_key[s])
		else:
			p |= (1<<DNA_key[s])

		if(start-end >= P):
			sub_key[DNA_key[DNA[end]]] -= 1
			if(sub_key[DNA_key[DNA[end]]]<patten[DNA_key[DNA[end]]]):
				p &= ~(1<<DNA_key[DNA[end]])
			else:
				p |= (1<<DNA_key[DNA[end]])
			end += 1
		start += 1
		print(start-end,p,yes)
		if(start-end == P and p==yes):
			ans += 1

	return ans

def solution2():
	def add(sub_key, patten, i, p):
		sub_key[i] += 1
		if(sub_key[i] == patten[i]):
			p += 1
		return p

	def rm(sub_key, patten, i, p):
		if(sub_key[i] == patten[i]):
			p -= 1
		sub_key[i] -= 1
		return p

	S, P = map(int, input().strip().split())
	DNA = input().strip()
	DNA_key = {'A':0, 'C':1, 'G':2, 'T':3}
	patten = list(map(int,input().strip().split()))
	sub_key = [0,0,0,0]
	p = 0
	ans = 0
	for i,v in enumerate(patten):
		if(v==0):
			p += 1
	for i in range(P):
		p = add(sub_key, patten, DNA_key[DNA[i]], p)
		ans += 1 if p == 4 else 0
	for i in range(P,S):
		p = add(sub_key, patten, DNA_key[DNA[i]], p)
		p = rm(sub_key, patten, DNA_key[DNA[i-P]], p)
		ans += 1 if p == 4 else 0
		
	return ans

def solution3():
	def add(sub_key, patten, i, p):
		sub_key[i] += 1
		if(sub_key[i] == patten[i]):
			p |= (1<<i)
		return p

	def rm(sub_key, patten, i, p):
		if(sub_key[i] == patten[i]):
			p &= ~(1<<i)
		sub_key[i] -= 1
		return p

	S, P = map(int, input().strip().split())
	DNA = input().strip()
	DNA_key = {'A':0, 'C':1, 'G':2, 'T':3}
	patten = list(map(int,input().strip().split()))
	sub_key = [0,0,0,0]
	p = 0
	ans = 0
	for i,v in enumerate(patten):
		if(v==0):
			p |= (1<<i)
	for i in range(P):
		p = add(sub_key, patten, DNA_key[DNA[i]], p)
	ans += 1 if p == (1<<len(patten))-1 else 0
	for i in range(P,S):
		p = add(sub_key, patten, DNA_key[DNA[i]], p)
		p = rm(sub_key, patten, DNA_key[DNA[i-P]], p)
		ans += 1 if p == (1<<len(patten))-1 else 0
		
	return ans

if(__name__ == "__main__"):
	print(solution())