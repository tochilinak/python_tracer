### Original interpreter (Python 3.10)

Input:

```
python3 my_tracer.py f < example.py
```

Output:
```
0 LOAD_FAST None
2 LOAD_CONST None
4 COMPARE_OP None
6 POP_JUMP_IF_FALSE None
12 LOAD_CONST None
14 RETURN_VALUE None
```

Input:
```
python3 my_tracer.py f < example1.py
```

Output:
```
0 LOAD_FAST None
2 LOAD_CONST None
4 COMPARE_OP None
6 POP_JUMP_IF_FALSE None
8 LOAD_CONST None
10 RETURN_VALUE None
```


### Hacked interpreter (Python 3.11)

Input:

```
python3 my_tracer.py f < example.py
```

Output:

```
2 LOAD_FAST hello
4 LOAD_CONST hello
6 COMPARE_OP 1
12 POP_JUMP_FORWARD_IF_FALSE False
18 LOAD_CONST hello
20 RETURN_VALUE 2
```

Input:

```
python3 my_tracer.py f < example1.py
```

Output:

```
2 LOAD_FAST <__main__.MyObject object at 0x7f2813c14450>
4 LOAD_CONST <__main__.MyObject object at 0x7f2813c14450>
6 COMPARE_OP 1
12 POP_JUMP_FORWARD_IF_FALSE <__main__.MyObject object at 0x7f2813c14290>
14 LOAD_CONST <__main__.MyObject object at 0x7f2813c14450>
16 RETURN_VALUE 1
```
