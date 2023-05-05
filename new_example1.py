def f(x):
    if x == 1:
        return 1

    a = [2, x] == [2, 2]
    return a == x


class MyObject:
    def __eq__(self, other):
        print("Called eq")
        return MyObject()

    def __bool__(self):
        return False


args = [MyObject()]
