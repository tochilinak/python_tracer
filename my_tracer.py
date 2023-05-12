import sys
import dis
import builtins

def symbolic_handler(*args):
    #print("ARGS:", args, flush=True)
    return None


silent = "--silent" in sys.argv
started = False
root = "/"
tab = ""
adapter = None
if "___create_symbolic_adapter___ibmviqhlye" in dir(builtins):
    adapter = ___create_symbolic_adapter___ibmviqhlye(symbolic_handler)

def tracer(frame, event, arg):
    global started, tab

    if frame.f_code.co_name != "symbolic_handler":
        frame.f_globals["___symbolic___ibmviqhlye"] = frame.f_code
        frame.f_globals["___adapter___ibmviqhlye"] = adapter

    if event == "call": 
        #frame.f_trace_opcodes = True
        frame.f_trace_lines = False
        started = True

        if frame.f_code.co_filename == "<string>":
            tab += " "
            if not silent:
                print(tab, "CALL", frame.f_code.co_name)#, frame.f_code.co_filename)

        return tracer

    elif event == "opcode":
        instr = frame.f_code.co_code[frame.f_lasti]
        #print()
        #print(tab, dis.opname[instr], frame.f_code.co_code[frame.f_lasti + 1], type(arg), getattr(arg, "___concrete___ibmviqhlye", None), frame.f_globals["___symbolic___ibmviqhlye"], frame.f_code.co_cellvars, flush=True)

    elif event == "return":
        if frame.f_code.co_filename == "<string>":
            if not silent:
                print(tab, "RETURN", repr(arg))
            tab = tab[:-1]

    elif event == "exception":
        if not silent:
            print()
            print("EXCEPTION")#, arg)#, arg[1])
        frame.f_globals["___symbolic___ibmviqhlye"] = None
        if not silent:
            print()

    else:
        frame.f_trace_opcodes = False
        frame.f_trace_lines = False
        frame.f_trace = None
        return None


code = sys.stdin.read()
sys.settrace(tracer)
exec(code)
