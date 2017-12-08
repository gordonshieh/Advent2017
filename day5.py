
def escape(l):
    cur_index = 0
    count = 0
    while cur_index < len(l):
        jump = l[cur_index]
        l[cur_index] += 1
        cur_index += jump
        count += 1
    return count

with open('day5_input.txt', 'r') as input:
    nums = [int(item) for item in input]

print(escape(nums))
