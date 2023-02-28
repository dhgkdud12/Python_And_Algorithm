# 1. for문을 이용하여 최대공약수 & 최대공배수 구하기
import math

a = 10
b = 12

# GCD (Greatest Common Divisor)
# 최대공약수 구하기
for i in range(min(a, b), 0, -1):
    if a%i == 0 and b%i == 0:
        print(i) # 2
        break

# LCM (Least Common Multiple)
# 최소공배수 구하기
for i in range(max(a,b), a*b-1):
    if i%a == 0 and i%b == 0:
        print(i) # 60
        break
        
        
        
# 2. 유클리드 호제법
# x와 y의 최대공약수 == y와 r의 최대공약수

# 최대공약수 구하기
def GCD(x, y):
    while(y): # y가 자연수일 때(a%b != 0)
        x, y = y, x%y
    return x

print(GCD(3, 4))

# 최소공배수 구하기
def LCM(x, y):
    return (x*y)//GCD(x,y)

print(LCM(3, 4))

# 3. Math 함수 이용
print(math.gcd(3, 4)) # 최대공약수
print(math.lcm(10, 12)) # 최소공배수