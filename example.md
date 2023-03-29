### Original interpreter

Input:

```
python3 my_tracer.py f < example.py
```

Output:
```
LOAD_FAST None
LOAD_CONST None
COMPARE_OP None
POP_JUMP_IF_FALSE None
LOAD_CONST None
RETURN_VALUE None
```

Input:
```
python3 my_tracer.py f < example1.py
```

Output:
```
LOAD_FAST None
LOAD_CONST None
COMPARE_OP None
POP_JUMP_IF_FALSE None
LOAD_CONST None
RETURN_VALUE None
```


### Hacked interpreter

Input:

```
python3 my_tracer.py f < example.py
```

Output:

```
LOAD_FAST hello
LOAD_CONST hello
COMPARE_OP 1
POP_JUMP_FORWARD_IF_FALSE False
LOAD_CONST hello
RETURN_VALUE 2
```

Input:

```
python3 my_tracer.py f < example1.py
```

Output:

```
LOAD_FAST <__main__.MyObject object at 0x7fc694f64490>
LOAD_CONST <__main__.MyObject object at 0x7fc694f64490>
COMPARE_OP 1
POP_JUMP_FORWARD_IF_FALSE <__main__.MyObject object at 0x7fc694f642d0>
LOAD_CONST <__main__.MyObject object at 0x7fc694f64490>
RETURN_VALUE 1
```
