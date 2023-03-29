def f(x):
    if x == 1:
        return 1

    return 2


class MyObject:
    def __eq__(self, other):
        return MyObject()

    def __bool__(self):
        return True


f(MyObject())
