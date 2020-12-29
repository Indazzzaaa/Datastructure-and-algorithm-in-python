import time as t


def sum(n):
    if n == 1:
        return 1
    else:
        return n+sum(n-1)


start = t.time()
print(sum(800))
end = t.time()
print(end-start)
