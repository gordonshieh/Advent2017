import operator
import sys 
# input = [0, 2, 7, 0]
input = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]

def redist(l):
    index, max_value = max(enumerate(l), key=operator.itemgetter(1))
    
    blocks_to_redist = max(int(max_value / (len(l) - 1)), 1)
    remaining_blocks = max_value
    blocks = list(l)
    blocks[index] = 0
    index = (index + 1) % len(blocks)
    
    while remaining_blocks > blocks_to_redist:
        blocks[index] += blocks_to_redist
        remaining_blocks -= blocks_to_redist
        index = (index + 1) % len(blocks)
    
    # move the last chunk of blocks
    blocks[index] += remaining_blocks
    return blocks
    
def count_redist(l):
    results = []
    count = 0
    result = l
    while True:
        count += 1
        result = redist(result)
        print(result)
        if result in results:
            return count
        
        results.append(result)
    
print(count_redist(input))
