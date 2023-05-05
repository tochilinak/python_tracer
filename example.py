def f(x):
    if x == 1:
        return 1

    print(dir(x))
    x.attr = 0
    return 2


class A: pass

a = A()
f(a)
