def fibonacci(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    else:
        memo[n]=fibonacci(n-1,memo)+fibonacci(n-2,memo)
        return memo[n]
       
n=66
print(fibonacci(n))
