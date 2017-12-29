import re

# this solution only works if insertion order is preserved in Python dictionaries!!!

class Node:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
        self.children_nodes = []

prog_name_structure = re.compile('(\w+) \((\d+)\)((?: \-\> )(.+)|\n)')

def init_nodes():
    nodes = {}
    with open('day7_input.txt', 'r') as input:
        for line in input:
            match = prog_name_structure.search(line)
            name = match.group(1)
            weight = int(match.group(2))
            
            if match.group(4):
                children = match.group(4).split(', ')
            else:
                children = []
            nodes[name] = Node(name, weight, children)
    return nodes
    
def part1(nodes):
    children = []
    for node in nodes.values():
        for i, n in enumerate(node.children):
            children.append(n)
    names = [node.name for node in nodes.values()]
    return frozenset(names) - frozenset(children)


def get_weight(node):
    if len(node.children_nodes) == 0:
        return node.weight
    else:
        return node.weight + sum(get_weight(n) for n in node.children_nodes)


def get_unbalanced_node(root, nodes):
    children_weights = {child.name: get_weight(child) for child in nodes[root].children_nodes}
    if len(frozenset(children_weights.values())) == 1:
        return root
    max_weight = max(children_weights.values())
    max_child = [k for k, v in children_weights.items() if v == max_weight][0]
    return get_unbalanced_node(max_child, nodes)
        
    


def part2(root, nodes):
    for node in nodes.values():
        node.children_nodes = [nodes[c] for c in node.children]
    unbalanced_node = get_unbalanced_node(root, nodes)
    weights = [get_weight(child) for child in nodes[root].children_nodes]
    return nodes[unbalanced_node].weight - (max(weights) - min(weights))
            

if __name__ == '__main__':
    nodes = init_nodes()
    root = list(part1(nodes))[0]
    print(root)
    print(part2(root, nodes))
        

