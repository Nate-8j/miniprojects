# Что спрашивают ДЛИНУ или КОЛ-ВО

# краями конечного списка будут числа из краев условия

# в задачи на DEL(n, m) брать огромный диапазон 100000 пример

### ВСЕГДА ПИСАТЬ КОД ТАК, И ПРОВЕРЯТЬ НА ГРАНИЦАХ      ЕСТЬ ЛИ РАЗРЫВ
# p = [x/10 for x in range(1010, 1430 + 1)]
# q = [x/10 for x in range(1440, 1990 +1)]
# a = [x/10 for x in range(1010, 2000)]

# for x0 in range(1010, 2000):
#     x = x0/10
#     if ((x in a) <= ((x in p) or (x in q))) == 0:
#         a.remove(x)
# print(a)


"""1"""

# def f(n, m):
#     return n % m == 0

# for a in range(1, 10000):
#     for x in range(1, 10000):
#         if ((not(f(x, a))) <= ((not(f(x, 18))) or (not(f(x, 42))))) == 0:
#             break
#     else:
#         print(a)


# def f(x, a):
#     return ((not(x%a==0)) <= ((not(x%18==0)) or (not(x%42==0))))

# for a in range(1, 10000):
#     if all(f(x, a) for x in range(1, 10000)):
#         print(a)


# ----------------------------------

# def f(x, a):
#     return ((x & 34 != 0) <= ((x&41 == 0) <= (x&a != 0)))

# for a in range(1, 10000):
#     if all(f(x, a) for x in range(1, 10000)):
#         print(a)
#         break

# ----------------------------------


# def f(x, y, a):
#     return ((((y + 5*x) != 31) or (a > (x-2))) and (a <(y+37)))

# for a in range(1, 1000):
#     if all(f(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
#         print(a, 1)
#         break

# for a in range(1, 10000):
#     for x in range(1, 10000):
#         for y in range(1, 10000):
#             if f(x, y, a) == 0:
#                 break
#         if f(x, y, a) == 0:
#             break
#     else:
#         print(a)
#         break

# ----------------------------------

""" 2 """

# R = list(range(12, 32))
# Q = list(range(6, 17))
# P = list(range(17, 24))
# A = []

# for x in range(1, 100):
#     if (((x in A) or (x in P)) or ((x in Q) <= (x in R))) == 0:
#         A.append(x)
# print(A) # [6, 7, 8, 9, 10, 11]
# # 6 есть в условии - берем
# # 11 есть в условии? нет. увеличиваем на 1, и по кругу


# q = list(range(8, 18))
# p = list(range(3, 12))
# a = list(range(1, 100))

# for x in range(1, 100):
#     if (((x in a) <= (x in p)) or (x in q)) == 0:
#         a.remove(x)
# print(a)
# print(17-3)

# ----------------------------------

""" 3 """

# def f(x, a):
#     return (((x + 40 < a) or (x+a <40)) <= (x%a==0))

# for a in range(1, 1000):
#     if all(f(x, a) for x in range(1, 1000)):
#         print(a)


# ============================
### кол-во решенных задач: 14
# ============================


def f(x, a):
    return ((x%4 != 3) or (x%6!=1)) <= (x%36!=a)

for a in range(1, 100000):
    if all(f(x, a) for x in range(1, 100000)):
        print(a)
        break