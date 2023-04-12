def f(x):
    if x == 1:
        return 1

    return 2


class MyObject:
    def __eq__(self, other):
        print("Called eq")
        return MyObject()

    def __bool__(self):
        return True


f(MyObject())
