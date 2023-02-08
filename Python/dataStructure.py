name = 'sandra' # 문자열
age = 14 # 숫자
license = True # boolean

# 할당 연산자 =
# 변수가 할당된 객체의 주솟값을 '가리키게' 됨

# list
user1 = ['sandara', 14, True]

# dictionary
user2 = {'name': 'alex', 'age':3, 'license': True}

# ploblem solving
nums = [3, 1, 4, 2, 9, 6]

# max
max_num = -1
for i in nums :
    if max_num < i :
        max_num = i

print('최댓값:', max_num)

# min
min_num = 9999
for i in nums:
    if min_num > i:
        min_num = i
print('최솟값:', min_num)
