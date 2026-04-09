# Что спрашивают ДЛИНУ или КОЛ-ВО

# краями конечного списка будут числа из краев условия

# в задачи на DEL(n, m) брать огромный диапазон 100000 пример


"""1"""


# def f(x, y, a):
#     return ((((y + 5*x) != 31) or (a > (x-2))) and (a <(y+37)))

# for a in range(1, 1000):
#     if all(f(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
#         print(a, 1)
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

### Лучше ПИСАТЬ КОД ТАК, И ПРОВЕРЯТЬ НА ГРАНИЦАХ, ЕСТЬ ЛИ РАЗРЫВ
# p = [x/10 for x in range(1010, 1430 + 1)]
# q = [x/10 for x in range(1440, 1990 +1)]
# a = [x/10 for x in range(1010, 2000)]

# for x0 in range(1010, 2000):
#     x = x0/10
#     if ((x in a) <= ((x in p) or (x in q))) == 0:
#         a.remove(x)
# print(a)

# ----------------------------------


### ЭТОТ АЛГОС ЛУЧШЕ

# def f(x):
#     p = 10<=x<=29
#     q = 13<=x<=18
#     a = a1<=x<=a2
#     return (a<=p) or q

# d = [y for x in (10, 29, 13, 18) for y in (x, x+0.1, x-0.1)]
# r = []

# for a1 in d:
#     for a2 in d:
#         if a2>=a1 and all(f(x) for x in d):
#             r.append(a2-a1)
# print(max(r))

# ah = []
# def f(x):
#     p = x in list(range(2, 21, 2))
#     q = x in list(range(3, 31, 3))
#     a = x in ah
#     return (p<=a) or ((not a) <= (not q))

# for x in range(1, 10000):
#     if f(x) == 0:
#         ah.append(x)
# print(ah)

# ============================
### кол-во решенных задач: 30
# ============================