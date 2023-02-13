# SET
# unhashable type은 추가할 수 없음
# 변형이 불가능한(immutable) 값이어야 함.

# 리스트는 변형 가능한 타입
# 튜플은 한 번 정의되면 변형이 불가능한 타입

# 원소 추가
country = {'Korea', 'Japan', 'China'}
country.add('USA')
print(country)

# 원소 삭제
country.remove('Korea')
country.discard('France')

# 여러개 추가
country.update(['France', 'Canada'])
print(country)

# 랜덤 원소 1개 제거
country.pop()
print(country)

