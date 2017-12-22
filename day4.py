def is_valid(line):
    return len(line.split()) == len(frozenset(line.split()))


def has_anagram(line):
    words = line.split()
    letter_sets = [frozenset(item) for item in words]
    return len(frozenset(letter_sets)) != len(letter_sets)


with open('day4_input.txt', 'r') as input:
    print(sum(is_valid(line) for line in input))

with open('day4_input.txt', 'r') as input:
    print(sum(not has_anagram(line) for line in input))
