import sys


def symbolic_handler(*args):
    print("HANDLER ARGS:", args, flush=True)

    if args[0] == "LOAD_CONST":
        return [f"(|{args[1]}|)"]

    if args[0] == "BUILD_LIST":
        if any(not isinstance(x, str) for x in args[1:]):
            return []
        return ["[" + ",".join(args[1:]) + "]"]

    return f"{args[0]}({args[1:]})"


adapter = ___create_symbolic_adapter___ibmviqhlye(symbolic_handler)


if __name__ == "__main__":
    code = sys.stdin.read()
    func_name = sys.argv[1]
    exec(code)
    args_pairs = []
    for arg in args:
        symb_arg = "(|" + repr(arg) + "|)"
        args_pairs.append((arg, symb_arg))

    result = adapter.run(eval(func_name), *args_pairs)
    print("RESULT:", result)
