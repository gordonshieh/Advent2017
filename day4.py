
def is_valid(line):
    return len(line.split()) == len(frozenset(line.split()))
    
with open('day4_input.txt', 'r') as input:
    print(sum(is_valid(line) for line in input))
    