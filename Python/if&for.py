# if
gem1 = [3, 3, 1, 2, 4, 3, 5, 1, 2]

if 1 in gem1:
    print(True)
else:
    print(False)

# for
gem2 = [4, 3, 5, 1, 2, 3, 6, 7, 3, 1]

grade1 = False
for i in gem2:
    if i == 1:
        grade1 = True
        break

print(grade1)

# 각 기록
gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]
grades = {1:0, 2:0, 3:0}

for i in gems:
    grades[i] += 1 # key값이 i인 value 1 증가

print(grades)

result = sum(gems)

if result <= 15:
    print('성공')
elif 15 < result <= 23:
    print('보통')
else:
    print('실패')