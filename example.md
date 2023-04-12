## example.py

Прогоняемый код:

```python
def f(x):
    if x == 1:
        return 1

    x.attr = 0
    return 2


class A: pass

a = A()
f(a)
```

Вывод от `./python ../python_tracer/my_tracer.py f < ../python_tracer/example.py`:

```
2 LOAD_FAST <class '__main__.A'> <__main__.A object at 0x7f588b0b8610>

calling tp_str on 0x7f588b0c0270
4 LOAD_CONST <class '___wrapper___ibmviqhlye'> <__main__.A object at 0x7f588b0b8610>

calling tp_str on 0x7f588b0c01f0
6 COMPARE_OP <class '___wrapper___ibmviqhlye'> 1
calling tp_richcompare 2 on 0x7f588b0c0270
calling tp_richcompare 2 on 0x7f588b0c01f0

calling tp_str on 0x7f588b0c01f0
12 POP_JUMP_FORWARD_IF_FALSE <class '___wrapper___ibmviqhlye'> False
calling nb_bool on 0x7f588b0c01f0

18 LOAD_CONST <class '__main__.A'> <__main__.A object at 0x7f588b0b8610>

calling tp_str on 0x7f588b0c01f0
20 LOAD_FAST <class '___wrapper___ibmviqhlye'> 0

calling tp_str on 0x7f588b0c0270
22 STORE_ATTR <class '___wrapper___ibmviqhlye'> <__main__.A object at 0x7f588b0b8610>
calling tp_setattro on 0x7f588b0c0270

32 LOAD_CONST <class '__main__.A'> <__main__.A object at 0x7f588b0b8610>

calling tp_str on 0x7f588b0c0270
34 RETURN_VALUE <class '___wrapper___ibmviqhlye'> 2
```
