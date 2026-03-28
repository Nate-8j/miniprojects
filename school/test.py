# from itertools import permutations, product

# def f(x, y, z, w):
#     return (y == (not w)) <= (not (w and (x == (x or (w <= z)))))
# for a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 in product([0, 1], repeat=10):
#     h = [
#         (a1, a2, 1, 1, 0),
#         (a3, a4, 1, a5, 0), 
#         (a6, 1, a7, 1, 0),
#         (1, a8, a9, a10, 1)
#     ]
#     if len(h) == len(set(h)):
#         for p in permutations('xyzw', r=4):
#             if all(f(**dict(zip(p, ln))) == ln[-1] for ln in h):
#                 print(p)


# def f(n):
#     s = ''
#     while n != 0:
#         s = s + str(n%3)
#         n //= 3
#     return s
# a = []
# for n in range(1, 10000):
#     n3 = f(n)
#     n3 = ''.join(sorted(n3, reverse=True))
#     n3 = n3 + n3[-1]
#     r = int(n3, 3)
#     if r < 1200:
#         a.append(r)
# print(max(a))

# from turtle import *
# tracer(0)
# screensize(20000, 20000)
# m = 20
# lt(90)
# up()

# fd(10*m)
# down()
# for i in range(6):
#     fd(50*m)
#     rt(90)
#     fd(43*m)
#     rt(90)
# up()
# fd(40*m)
# rt(90)
# fd(40*m)
# down()
# for i in range(9):
#     fd(40*m)
#     lt(90)
#     fd(20*m)
#     lt(90)

# up()
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x*m, y*m)
#         dot(5, 'red')

# done()

# Vor = 640*128*10
# Vp = Vor*100/165
# V = (Vp + Vor)
# for i in range(1, 1000):
#     if V * i <= 10*2**23:
#         print(i)
        

# from itertools import *
# cnt = 0
# for i in product('0123456789ABCD', repeat=5):
#     a = ''.join(i)
#     if a[0] != '0':
#         res = ''
#         for c in a:
#             if c in 'ABCD':
#                 res += 'a'
#             if c in '13579':
#                 res += 'd'
#             else:
#                 res += 'c'
#         if 'ad' not in res and 'da' not in res:
#             cnt += 1
# print(cnt)

# def f(s, n):
#     if s >= 342:
#         return n % 2 == 0
#     if n == 0:
#         return 0
#     h = [f(s+7, n-1), f(s*3, n-1)]
#     return all(h) if n%2==0 else any(h)

# print([s for s in range(1, 301) if not f(s, 2) and f(s, 4)])

'''------------------------------ 48 ------------------------------'''




# from itertools import product, permutations

# def f(x, y, z, w):
#     return (y == (not w)) <= (not (w and (x == (x or (w <= z)))))

# for a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 in product([0,1], repeat=10):

#     arr = [
#         (a1, a2, 1, 1, 0),
#         (a3, a4, 1, a5, 0),
#         (a6, 1, a7, 1, 0),
#         (1, a8, a9, a10, 1)
#     ]
#     if len(arr) == len(set(arr)):
#         for p in permutations('xyzw', r=4):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in arr):
#                 print(p)


# from turtle import *
# screensize(3000, 3000)
# tracer(0)
# lt(90)
# m = 20
# up()

# fd(10*m)
# down()
# for i in range(6):
#     fd(50*m)
#     rt(90)
#     fd(43*m)
#     rt(90)
# up()
# fd(40*m)
# rt(90)
# fd(40*m)
# down()
# for i in range(9):
#     fd(40*m); lt(90); fd(20*m); lt(90)
# up()
# for x in range(-70, 70):
#     for y in range(-70, 70):
#         goto(x*m, y*m)
#         dot(3, 'red')
# done()










# s = 640*128*10
# print((10*2**23)//(s+(s*100/165)))









# from itertools import *

# cnt = 0
# for w in product('0123456789abcd', repeat=5):
#     s = ''.join(w)
#     res = ''
#     if s[0] == '0':
#         continue
#     for c in s:
#         if c in 'abcd':
#             res+='a'
#         elif c in '13579':
#             res += 'b'
#         else:
#             res += 'c'
#     if 'ab' not in res and 'ba' not in res:
#         cnt += 1 

# print(cnt)


# ---------------------------------   43   ----------------------------------

