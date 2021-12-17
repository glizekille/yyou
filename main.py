def sc(i):
    print(i)
    if i <=1:
        return
    else:
        sc(i - 1)
sc(12)
