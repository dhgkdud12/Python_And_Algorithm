# print

nums = [1, 2, 3, 4, 5]
print(1)
print('5')
print(nums[0])
print(type(3)) # int
print(2, 4)

print(3, end=' ') # 가로 출력
print(4)


# input
num = input()
print(num, type(num)) # string

num2 = input('숫자를 입력하세요: ')

# 공백 기준 분리 후 int로 변경 후 list화
# 1 2 3 -> [1, 2, 3]
nums = list(map(int, input().split()))
print(nums)

# 2차원 리스트 받기
# 1 2
# 3 4
# 5 6
# ->
# [[1,2], [3,4], [5,6]]
nums_matrix = [list(map(int, input().split())) for _ in range(3)]
print(nums_matrix, type(nums_matrix))