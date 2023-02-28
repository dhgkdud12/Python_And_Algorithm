# DFS
# Stack 이용, 재귀 함수 2가지 방법

# 1. 스택 + 인접 행렬 (공간복잡도 높으나, 단방향 그래프인 경우 전치로 방향 전환 유리)

V, E = map(int, input().split())

adj_matrix = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1
    
stack = [1] # 1번 시작
visited = [] # 방문 기록용

while stack:
    current = stack.pop()
    if current not in visited: # 방문하지 않은 곳이라면,
        visited.append(current) # 방문 체크

    for destination in range(V+1):
        if adj_matrix[current][destination] and destination not in visited: # 갈수있고 방문 안했다면
            stack.append(destination) # 다음 갈 곳 Stack에 저장

print('이동경로:', *visited)

# 2. 스택 + 인접 리스트 (공간 복잡도 낮음)

V, E = map(int, input().split())

adj_list = [[] for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)

stack = [1]
visited = []

while stack:
    current = stack.pop()
    if current not in visited:
        visited.append(current)

    for destination in adj_list[current]:
        if destination not in visited: # 갈 수 있고, 방문 안했으면
            stack.append(destination)
print('이동경로:', *visited)