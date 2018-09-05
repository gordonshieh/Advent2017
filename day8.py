import operator

registers = {}

ops = {
    'inc' : operator.add,
    'dec': operator.sub,
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne
}

with open('day8_input.txt', 'r') as f:
    for line in f:
        r1, op1, v1, _, r2, op2, v2 = line.split()
        reg_val1 = registers.get(r1, 0)
        reg_val2 = registers.get(r2, 0)
        if ops[op2](reg_val2, int(v2)):
            reg_val1 = ops[op1](reg_val1, int(v1))
            registers[r1] = reg_val1
            
print(sorted(registers.items(), key=operator.itemgetter(1))[-1][1])
