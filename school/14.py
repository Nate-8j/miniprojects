# из 10 в любую до 10
# def f(x, y):
#     s = ''
#     while x > 0:
#         s = str(s%y) + s
#         x //= y
#     return s

# из 10 в любую до 36
# c = '0123456789abcdefghijklmnopqrstuvwxyz'
# def f(x, y):
#     s = ''
#     while x > 0:
#         s = c[x%y] + s
#         x //= y
#     return s

# print(f(1866, 16))


"""Задача 1"""
# c = '0123456789abcdefghijklmnopqrstuvwxyz'
# for x in c[:22][::-1]:
#     a = int(f'12313{x}57', 22)
#     b = int(f'1{x}34561', 22)
#     if (a+b)%21 == 0:
#         print((a+b)//21)
#         break

""" Задача 2 """
# a = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 65
# cnt = 0
# while a > 0:
#     if a%27 > 9:
#         cnt += 1
#     a //= 27
# print(cnt)


""" Задача 3 """
# arr = []
# gg = 6**2030 + 6**100
# for x in range(1, 2031):
#     a = gg - x
#     cnt = 0
#     while a > 0:
#         if a%6 == 0:
#             cnt += 1
#         a //= 6
#     arr.append(cnt)
# print(min(arr))


# -----------------------------------------------------------------

s = '0123456789abcdefghijklmnopqrstuvwxyz'
for x in s[:15]:
    for y in s[:17]:
        a = int(f'123{x}5', 15) + int(f'67{y}9', 17)
        if a%131 == 0:
            if y < x:
                print(a//131)