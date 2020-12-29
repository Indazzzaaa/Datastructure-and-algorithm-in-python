def Fact(n):
    if n == 1:
        return 1
    else:
        return n*Fact(n-1)


print(Fact(5))
