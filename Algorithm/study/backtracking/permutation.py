arr = ['A', 'B', 'C']

# 순열

# 1. for문 순열
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j != k and k != i:
                print([arr[i], arr[j], arr[k]])

print()

# 2. 재귀순열
arr = ['A', 'B', 'C']
sel = [0, 0, 0]
check = [0, 0, 0] # 뽑을지 말지 결정하는 리스트

def perm(depth):
    if depth == 3:
        print(sel)
        return

    for i in range(3):
        if not check[i]: # check[i]이 0이라면
            check[i] = 1 # 자리 차지 표시
            sel[depth] = arr[i]
            perm(depth+1)
            check[i] = 0 # 다음을 위해 초기화 - 중요


perm(0)