from functools import partial


class Garbage():
    def __init__(self, chars):
        self.chars = chars

    @property
    def size(self):
        return len(self.chars)

    def __str__(self):
        return self.chars


class Group():
    def __init__(self, items=None):
        if not items:
            items = []
        self.items = items

    @property
    def num_groups(self):
        return sum(item.num_groups for item in self.items if isinstance(item, Group)) + 1

    def score(self, depth=1):
        return sum(item.score(depth + 1) + depth for item in self.items if isinstance(item, Group)) + 1

    def garbage_size(self):
        return sum(item.size for item in self.items if isinstance(item, Garbage)) + \
               sum(item.garbage_size() for item in self.items if isinstance(item, Group))

    def __str__(self):
        return str(self.items)


def parse_group(it):
    cur_char = next(it)
    groups = []
    while cur_char != '}':
        if cur_char == '{':
            g = parse_group(it)
            groups.append(g)
            cur_char = next(it)
        elif cur_char == ',':
            cur_char = next(it)
        elif cur_char == '<':
            g = parse_garbage(it)
            groups.append(g)
            cur_char = next(it)
    return Group(groups)


def parse_garbage(it):
    cur_char = next(it)
    s = ""
    while cur_char != '>':
        if cur_char == '!':
            next(it)
        else:
            s += cur_char
        cur_char = next(it)
    return Garbage(s)


with open('day9_input.txt') as f:
    it = iter(partial(f.read, 1), '')
    # skip the first character since it's always an open curly brace
    next(it)
    print(parse_group(it).score())
    print(parse_group(it).garbage_size())


