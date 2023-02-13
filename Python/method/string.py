# String

# 변경하고자 하는 문자를 지정한 문자로 변경 후 반환
word = 'hello world'
new_word = word.replace('o', 'bbbbb')
# new_word = word.replace('o', 'bbbbb', 1) # 2개의 'o' 중 1개만 변경
print(word)
print(new_word)

# 문자열 특정 기준으로 나누어 리스트로 반환, 지정하지 않을 시 공백
email = 'dhgkdud12@github.com'
split_email = email.split('@')
print(email)
print(split_email)

nums = "1 2 3 4 5"
print(nums.split())

# 반복 가능한(iterable) 객체를 특정 기준으로 이어붙인 문자열 반환
# 스트링 그 자체거나 리스트의 원소가 스트링이어야 가능
word = 'algorithm'
print('-'.join(word))

word = ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm']
print('*'.join(word))

# 문자열 탐색 및 탐색 결과의 맨 첫번째 인덱스 반환
# find - 미존재 시 -1 반환
# index - 미존재 시 오류

word = 'algorithm'
print(word.find('t'))
print(word.index('t'))