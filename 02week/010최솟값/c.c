#include<stdio.h>
#define STMAX 10000001

int st[STMAX];
int N, L;

int main(){
	int i, j, l, r, ans;
	scanf("%d%d",&N,&L);
	j = 2*N;
	for(i=N; i<j; i++){
		scanf("%d",&st[i]);
	}
	for(i = N-1; i!=0; i--){
		l = st[i<<1];
		r = st[i<<1|1];
		st[i] = l<r? l: r;
	}
	
	for(r=1, i=N, j=N+1, ans=st[N]; r<=N;){
		if(i!=j){
			if(i&1){
				ans = ans<st[i]? ans: st[i];
				i++;
			}
			if(j&1){
				--j;
				ans = ans<st[j]? ans: st[j];
			}
			i >>= 1;
			j >>= 1;
		}
		else{
			printf("%d ",ans);
			r++;
			i = r-L>0? r-L+N: N;
			j = r+N;
			ans = st[i];
		}
	}

	return 0;
}
