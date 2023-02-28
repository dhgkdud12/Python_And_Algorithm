# 조합
# 1. for문 조합
# 조합 2개 뽑기
arr = ['A', 'B', 'C']
for i in range(3):
    for j in range(i+1, 3):
        print(arr[i], arr[j])

print()

# 중복조합 2개 뽑기
arr = ['A', 'B', 'C']
for i in range(3):
    for j in range(i, 3):
        print(arr[i], arr[j])

print()

# 2. 재귀 조합
# 5C3
arr = ['A', 'B', 'C', 'D', 'E']
sel = [0, 0, 0]

def combination(idx, sidx):
    if sidx == 3: # sel 확정
        print(sel)
        return

    if idx == 5:
        return

    sel[sidx] = arr[idx]
    combination(idx+1, sidx+1) # 1. 두 개의 화살표가 동시에 오른쪽
    combination(idx+1, sidx) # 2. arr 쪽 화살표만 혼자

combination(0, 0)
print()

# 중복 조합 (재귀)
def combi_rep(idx, sidx):
    if sidx == m:
        print(*sel)
        return

    if idx == n:
        return

    sel[sidx] = arr[idx]
    combi_rep(idx, sidx+1)
    combi_rep(idx+1, sidx)

n, m = map(int, input().split())
arr = list(range(1, n+1))
sel = [0]*m
combi_rep(0, 0)