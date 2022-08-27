# 백준[11720](https://www.acmicpc.net/problem/11720)
## 문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

## 입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

## 출력
입력으로 주어진 숫자 N개의 합을 출력한다.

## 풀이
공백없이 주어진 숫자를 전부 쪼갠 뒤 sum함수를 이용하여 리스트의 합을 구한다.

```pyhon
from sys import stdin

input = stdin.readline

N = int(input().strip())
print(sum(map(int,list(input().strip()))))

```

## 잡담