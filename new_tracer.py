import sys
import dis


def symbolic_handler(*args):
    print("HANDLER ARGS:", args, flush=True)
    if args[0] == "LOAD_CONST":
        return [f"(|{args[1]}|)"]
    if args[0] == "BUILD_LIST":
        return ["[" + ",".join(args[1:]) + "]"]

    return f"{args[0]}({args[1:]})"


adapter = ___create_symbolic_adapter___ibmviqhlye(symbolic_handler)
func_name = ""
started = False


def tracer(frame, event, arg):
    global started, func_name

    if frame.f_code.co_name == func_name:
        started = True

    #if frame.f_code.co_name == "symbolic_handler":
    #    if event == "call":
    #        frame.f_globals["___inside_handler___ibmviqhlye"] = True
    #        frame.f_trace_opcodes = False
    #    elif event == "return":
    #        frame.f_globals["___inside_handler___ibmviqhlye"] = False

    if started and frame.f_code.co_name != "symbolic_handler":
        frame.f_globals["___symbolic___ibmviqhlye"] = frame.f_code
        frame.f_globals["___adapter___ibmviqhlye"] = adapter
        frame.f_trace_opcodes = True

    #if event == "opcode":
    #    instr = frame.f_code.co_code[frame.f_lasti]
    #    print(dis.opname[instr], flush=True)

    return tracer


if __name__ == "__main__":
    code = sys.stdin.read()
    func_name = sys.argv[1]
    exec(code)
    wrapped_args = []
    for arg in args:
        new_arg = ___wrap_concrete_object___ibmviqhlye(arg, "(|" + repr(arg) + "|)", adapter)
        wrapped_args.append(new_arg)

    sys.settrace(tracer)
    result = eval(func_name)(*wrapped_args)
    sys.settrace(None)
    print("RESULT:", result)
