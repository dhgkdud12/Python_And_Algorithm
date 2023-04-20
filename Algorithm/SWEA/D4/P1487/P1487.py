import sys
sys.stdin = open("input.txt", "r")

def dfs(n, sm):
    global cnt

    if sm > S:
        return

    if n == N: # 종료조건
        if sm == S:
            cnt += 1
            return
        return

    # 사용 O
    dfs(n+1, sm+lst[n])

    # 사용 X
    dfs(n+1, sm)


T = int(input())
for i in range(1, T+1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))

    v = [0] * N
    sm = 0
    cnt = 0

    dfs(0, 0)

    print(f'#{i} {cnt}')
