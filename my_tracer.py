import sys
import dis


func_name = sys.argv[1]
started = False

def tracer(frame, event, arg):
    global started

    if event == "call" and frame.f_code.co_name == func_name:
        frame.f_trace_opcodes = True
        frame.f_trace_lines = False
        started = True
        return tracer
    
    elif event == "opcode":
        instr = frame.f_code.co_code[frame.f_lasti]
        print(dis.opname[instr], arg)

    else:
        frame.f_trace_opcodes = False
        frame.f_trace_lines = False
        return tracer


code = sys.stdin.read()
sys.settrace(tracer)
exec(code)
