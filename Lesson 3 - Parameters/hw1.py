# 1. 
def combine_values(*values):
    if not values:
        return 1 
    product = 1
    for v in values:
        product *= v
        return product
    
    
# 2. 
def merge_details(label, **info):
    result = {"label": label}
    result.update(info)
    return result

# 3. 
# 8,10,0

#4
# {'name': 'Alpha', 'x':1, 'y':2, 'count': 2}
# {'name': 'Beta','count': 6}