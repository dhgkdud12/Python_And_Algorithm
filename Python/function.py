# def

def some_func(param1, param2):
    return [param1, param2]

print(some_func(1, 2))

# Recursion

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(10))

# memoization
memo = [0, 1]

def fibo(n):
    if n >= 2 and n >= len(memo):
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

print(fibo(10))