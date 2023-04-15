# fibo = {}
# def fibonacci(n):
#     if n in fibo:
#         return fibo[n]
#     if n==0:
#         value= 1
#     if n == 1:
#         value= 1
#     if n>=2:
#         value = fibonacci(n-1)+fibonacci(n-1)
#
#     fibo[n] = value
#     return value
# for i in range(0,101):
#     print(str(i)+ " : " +str(fibonacci(i)))


from functools import lru_cache


@lru_cache(maxsize=2000)
def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n >= 2:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(0,2001):
    print(f"{i} : {fibonacci(i)}")