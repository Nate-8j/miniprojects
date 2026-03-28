def f(s, n):
    if s >= 91:
        return n%2==0
    if n == 0:
        return 0
    gg = [i for i in range(1,s+1) if s % i == 0]
    h = [f(s + c, n -1) for c in gg]
    return all(h) if n%2==0 else any(h)

print([s for s in range(1, 92) if f(s, 2)])
