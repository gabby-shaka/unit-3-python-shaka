# 1
def rmv_dups(items):
    result = [] 
    for item in items:
        if item not in result:  
            result.append(item)
    return result
# 2
def find_common(list1, list2):
    result = [] 
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result
# 3
def reverse_sublists(data, size):
    result = []  
    for i in range(0, len(data), size):
        chunk = data[i:i+size]
        result.extend(chunk[::-1])
    return result
# 4
def rotate_list(items, positions):
    if len(items) == 0: 
        return []
    positions = positions % len(items)
    return items[-positions:] + items[:-positions]


