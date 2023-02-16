# range (st, ed, step)
for i in range(4):
    print(i, end= ' ')
print()

for j in range(10, 1, -1):
    print(j, end=' ')
print()

# 리스트화
print(list(range(4, 8)))

# zip
# 세로로 자료구조를 찝어서 한 열씩 튜플로 만듦
a = [1, 2, 3]
b = [1, 2, 3]
print(list(zip(a, b))) # 세로로 찝은 결과를 튜플로 만들기 - zip 객체 생성 -> 리스트화

# 만약 길이가 안맞다면 최소 값에 맞춰줌

# 레인지와 리스트를 찝어서 딕셔너리 형태로 제작
print(dict(zip(range(3), [0]*3)))

# enumerate
nums = [2, 4, 5]

# 반복문에서 인덱스 값까지 같이 뽑기
for idx, num in enumerate(nums):
    print(idx, num)

nums = [5, 3, 7, 2, 8, 1]
print(max(nums), min(nums), sum(nums), len(nums))