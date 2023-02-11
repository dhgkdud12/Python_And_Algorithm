# list
# 인덱스 값을 활용해 O(1)시간 안에 접근
# 인덱스 0부터

nums = [1, 2, 3, 4, 5]
print(nums[0]) # 1
nums[1] = 7
print(nums)
# nums[8] = 9 #IndexError

# 리스트 안에는 다양한 자료형 가능, 길이 가변적
list = ['banana', True, [1, 2, 3], {'name': 'alex'}, {7, 6}, (4, 5, 6)]

# 요소 추가 - 리스트 맨 뒤
nums.append(6)
print(nums)

# 요소 추출 후 반환
print(nums.pop(2)) # 2번째 인덱스 뽑기
print(nums.pop()) # 맨 뒤
print(nums.pop(0)) # 맨 앞

# 정렬, key 옵션으로 기준 선택
nums.sort()
print(nums)

# 역순 정렬 - key 옵션, 익명함수 lamda 활용
nums.sort(key=lambda x: -x)
print(nums)

# sorted() 함수: 정렬한 새로운 리스트를 만듦
new_nums = sorted(nums)
print(nums, new_nums)

# 리스트를 반대로 뒤집음(정렬과 관계 없음)
nums.reverse()
print(nums) # [7, 5, 4] -> [4, 5, 7]

# reversed() 함수: reversed object를 만듦
new_nums2 = reversed(nums)
# print(nums, new_nums2) # reversed는 list()로 한 번 더 감싸줘야 활용 가능
# print(list(new_nums2))

# insert(인덱스 위치, 값)
# 인덱스 위치에 값 추가
nums.insert(1, 8)
print(nums)

# 리스트 끝에 여러개의 값 추가
nums.extend([1, 2, 3])
print(nums)

str = ['a', 'p', 'p', 'l', 'e']
str.extend('grape')
print(str)

# 리스트 합치기
nums2 = [1, 2, 3, 4, 5] + [6, 7, 8]
print(nums2)

# count(n): n의 갯수 반환
print(nums2.count(5)) # 1

# index(n): n의 인덱스 값 반환
print(nums2.index(1)) # 1의 인덱스는 0

## list slicing
nums = [3, 5, 1, 4, 2]
slice_nums = nums[2:4]
print(nums, slice_nums)

print(nums[:2])
print(nums[1:])

# 인덱스 값 초과해도 에러가 나지 않음
print(nums[2:100])

# 리스트 카피, 얕은 복사
nums2 = nums # 같은 객체를 가리키어 id 값이 동일함

copied_nums = nums[:]
print(copied_nums)
reserved_nums = nums[::-1]
print(reserved_nums)

# 얕은 복사 시에는 id 값이 분리되므로 변경 시, 영향을 주지 않음
nums[0] = 100
print(nums, copied_nums)
print(nums2)

# 슬라이싱 삽입
nums[1:2] = [9, 10, 11]
print(nums)

# 특정 부분 깔끔하게 도려냄
nums[2:4] = []
print(nums)