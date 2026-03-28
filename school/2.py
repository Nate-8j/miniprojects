from itertools import product, permutations

def f(x, y, z, w):
    return (x == (w or y)) or ((w <= z) and (y <= w))

for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    arr = [(1, a1, a2, 1), (a3, a4, a5, 1), (1, a6, 1, a7)]
    if len(arr) == len(set(arr)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, ln))) == 0 for ln in arr):
                print(p)

















# from itertools import product, permutations

# def f(x, y, z, w):
#     return (not(x<=z)) or (y==w) or y

# for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
#     arr = [(1, 0, a1, a2, 0), (a3, 1, 0, a4, 0), (0, a5, a6, a7, 0)]
#     if len(arr) == len(set(arr)):
#         for p in permutations('xyzw', r=4):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in arr):
#                 print(p)