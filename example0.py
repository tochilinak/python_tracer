def g(y):
    return y

def f(x):
    g(x)
    return x + 1

f(wrap_concrete_object(1, "1", {}, lambda *args: None))
