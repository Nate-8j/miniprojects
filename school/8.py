# from itertools import combinations, product, permutations
#
# Перестановка
# Каждый символ используется 1 раз, порядок важен
# for i in permutations('ABC', 2):
#     print(i)
# print('---------')
#
# Каждый символ используется любое кол-во раз, порядок важен( BA и AB - разные комбинации)
# for i in product('ABC', repeat=2):
#     print(i)
# print('---------')
#
# Каждый символ используеться 1 раз, понядок НЕ важен
# for i in combinations('ABC', 2):
#     print(i)


"""
!!! для последовательности в АЛФАВИТНОМ порядке передать 
аргумент в ментоде sorted()

!!! В задачах на числа, число не может начинаться с НУЛЯ a[0] not in '0...'
"""

# from itertools import *
# s = set()
# for i in permutations('МАРИНА', 6):
#     a = ''.join(i)
#     if a[0] not in 'АИ':
#         s.add(a)
# print(len(s))

# from itertools import *
# s = set()
# for i in product('012345678', repeat=5):
#     a = ''.join(i)
#     if a[0] not in '01357' and a[-1] not in '18' and a.count('3') <= 1:
#         s.add(a)
# print(len(s))

# !!! для последовательности в АЛФАВИТНОМ порядке передать 
# аргумент в ментоде sorted()
# from itertools import *
# cnt = 0
# for i in product('АПРСУ', repeat=5):
#     a = ''.join(i)
#     cnt += 1
#     if a[0] in 'У' and 'АА' not in a:
#         print(cnt)
#         break

# from itertools import *
# cnt = 0
# for i in permutations(sorted('МОДЕСТ')):
#     cnt += 1
#     if cnt == 377:
#         print(''.join(i))

# from itertools import *
# cnt = 0
# for i in product(sorted('КОМПЬЮТЕР'), repeat=5):
#     cnt += 1
#     a = ''.join(i)
#     if cnt % 2 != 0 and a[0] != 'Ь' and a.count('К') == 2:
#         print(cnt)

# !!! если написано, что буквы в словах не повторяютсья и
# дано слово 'МАМА' - передвать в аргумент 'МА'
# s=set()
# from itertools import *
# for i in permutations('АКАРИДА', 7):
#     a = ''.join(i)
#     res = ''
#     for c in a:
#         if c in 'АИ':
#             res += 'g'
#         else:
#             res += 's'
#     if 'ss' not in res and 'gg' not in res:
#         s.add(a)
# print(len(s))

# from itertools import *
# cnt = 0
# for i in product('кресло', repeat=4):
#     a = ''.join(i)
#     if a[0] in 'крсл' and a[-1] in 'ео':
#         cnt += 1
# print(cnt)  

# from itertools import *

# cnt = 0
# for w in product('01234567', repeat=5):
#     a = list(map(int, w))
#     b = ''.join(w)
#     res = ''
#     for i in a:
#         if i % 2 == 0:
#             res += 'd'
#         else:
#             res += 'n'
#     if b.count('1') == 0 and b[0] != '0' and 'dd' not in res and 'nn' not in res:
#         cnt += 1
# print(cnt)


from itertools import *
cnt = 0

for i in permutations('01234567', r=5):
    a = ''.join(i)
    
    if a[0] != '0' and '1' not in a:
        res = ''
        for j in a:
            if int(j)%2==0:
                res += 'h'
            else:
                res += 'n'
        if 'hh' not in res and 'nn' not in res:
            cnt += 1
            print(a)

print(cnt)
