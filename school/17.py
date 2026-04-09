# Если есть ОТРИЦАТЕЛЬНЫЕ цифры- то условия окончания и 
# кол-ва цифр требуют использованания модуля abs()

# пары - идущие подряд эл. [2, -4, 7, 11], 
# то пары - [(2, -4), (-4, 7), (7, 11)]

# ---------------------------------------------

# a = [int(i) for i in open('school/17.txt')]
# res = []
# for i in a:
#     if i%3 == 0 and i%7 !=0 and i%17!=0 and i%19!=0 and i%27!=0:
#         res.append(i)
# print(len(res), max(res))

# ---------------------------------------------

# a = [int(i) for i in open('school/17.txt')]
# res = [x for x in a if (abs(x)%10==5 or abs(x)%10==7) and x%9!=0 and x%11!=0]
# print(len(res), min(res)+max(res))

# ---------------------------------------------

# a = [int(i) for i in open('school/17.txt')]
# res = []
# for i in range(len(a)-1):
#     x, y = a[i], a[i+1] # for x, y in zip(a, a[1:])
#     if x*y>0 and (x+y)%7==0:
#         res.append(x*y)
# print(len(res), min(res))

# ---------------------------------------------