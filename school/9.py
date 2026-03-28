# скопировать таблицу в файл в проекте 9.txt 

# cnt = 0
# for line in open('9.txt'):
#     a = [int(c) for c in line.split()]
#     if max(a) - min(a) > sum(a) - max(a) - min(a):
#         cnt += 1
# print(cnt)
 
# for line in open('9.txt'):
#     a = [int(c) for c in line.split()]
#     n3 = [c for c in a if a.count(c) == 3]
#     n1 = [c for c in a if a.count(c) == 1]
#     if len(n3) == 6 and len(n1) == 2:
#         if a.count(min(a)) == 1:
#             print(sum(a))
#             break

# n = 0
# for line in open('9.txt'):
#     n += 1
#     a = [int(i) for i in line.split()]
#     if len(a) == len(set(a)):
#         if 2*(max(a) + min(a)) == 3*(sum(a)-max(a)-min(a)):
#             print(n)

# cnt = 0
# for lint in open('9.txt'):
#     a = [int(i) for i in lint.split()]
#     n1 = [i for i in a if a.count(i) == 3]
#     n0 = [i for i in a if a.count(i) == 1]
#     if len(n1) == 3 and len(n0) == 3:
#         if 3*n1[0]**2 > sum([i**2 for i in n0]):
#             cnt += 1
# print(cnt)