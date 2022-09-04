from sys import stdin
def myInput():
        return stdin.readline().strip()
input = myInput

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

if(__name__ == "__main__"):
        print(" ".join(solution()))