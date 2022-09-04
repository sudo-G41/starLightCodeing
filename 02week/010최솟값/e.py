L = [1,2,3,4,5,6,7,8,9,10]
D = [0]
for i in L:
	D.append(i+D[-1])
print(D)

ST = [0]*2*len(L)
for i in range(len(L)):
	ST[i+len(L)] = L[i]
for i in range(len(L)-1, -1, -1):
	ST[i] = ST[i<<1] + ST[i<<1|1]

STa = [0]
for r in range(1,len(L)+1):
	st = 0
	l = len(L)
	r += l
	print(f"start l:{l} r:{r} st:{st}")
	while(l!=r):
		if(l&1):
			print(f"left add {l} {ST[l]}")
			st += ST[l]
			l += 1
		if(r&1):
			r -= 1
			st += ST[r]
			print(f"rigth add {r} {ST[r]}")
		print(f"l:{l} r:{r} st:{st}")
		l = l>>1
		r = r>>1
	print()
	STa.append(st)

print(STa)
