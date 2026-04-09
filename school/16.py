### КОЛ-ВО РЕШЕННЫХ ЗАДАЧ = 13
# ============================= 

# f = {}
# for n in range(20):
#     if n < 5:
#         f[n] = 1 + 2*n
#     elif n >= 5 and n%3==0:
#         f[n] = 2*(n+1)*f[n-2]
#     else:
#         f[n] = 2*n + 1 + f[n-1] + 2*f[n-2]
# print(f[15])


# def f(n):
#     if n < 3:
#         return n+1
#     elif n % 2 == 0:
#         return f(n-2) + n -2
#     else:
#         return f(n+2) +n + 2

# cnt = 0
# for i in range(1, 10000):
#     try:
#         if 10000 <= f(i) < 100000:
#             cnt += 1
#     except:
#         pass
# print(cnt)