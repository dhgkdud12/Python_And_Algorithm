# 회문(뒤집어도 똑같은 단어) 검사

# 1. 파이써닉 코드
word = input('단어를 입력하세요: ')
if word == word[::-1]:
    print('회문입니다.')
else:
    print('회문이 아닙니다.')

# 2. 반복문 사용
word = input('단어를 입력하세요: ')

reversed_word = ''
for i in word:
    reversed_word = i + reversed_word

if word == reversed_word:
    print('회문입니다.')
else:
    print('회문이 아닙니다.')

# 3. two pointer 활용
word = input('단어를 입력하세요: ')

left = 0 # 시작 인덱스
right = len(word - 1) # 마지막 인덱스

is_palindrome = True
while left < right:
    if word[left] == word[right]:
        left += 1
        right -= 1
        continue
    else:
        is_palindrome = False
        break

print(is_palindrome)