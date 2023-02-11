# dictionary
# { key : value }
# key 값으로 접근해 value 값 얻음, 해쉬 자료구조로 탐색이 O(1)로 매우 빠름

info = {'name' : 'lena'}
print(info['name'])

# 추가 및 수정
info = dict()
info['name'] = 'mina'
print(info)

# 키 값, 없을 시 반환 값 지정
print(info.get('name'))
print(info.get('age', '발견하지 못함'))

# key, value 쌍 추가, 동일한 키 값이 있다면 덮어씌워짐
dict1 = {'name' : 'sungmin', 'age' : 7}
dict2 = {'name' : 'moana', 'age' : 10, 'address' : 'California'}
dict1.update(dict2) # 덮어씌워짐
print(dict1)

# key 존재 시 제거 후 value 값 반환, 미존재 시 반환 값 설정
dict1 = {'name' : 'sungmin', 'age' : 7}
print(dict1.pop('name'))
print(dict1)

# del : 키값 미 존재 시 에러 발생
del dict2['name']
print(dict2)
# del dict2['license'] # 에러 발생

# key, value들의 모임 생성
dict1 = {'name' : 'sungmin', 'age' : 7}

for key in dict1.keys():
    print(key)


for value in dict1.values():
    print(value)


for key, value in dict1.items():
    print(key, value)