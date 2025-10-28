""" 
Create - [1,2,3]
Add - .append(val
Remove end - .pop()
Insert- .insert(index,val)
Length - len(list)
Slice - [start:end]
Index - [0]
"""

def filter_even(numbers:list):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even 


def list_stats(numbers):
    """Calculatr ,om,max,average of a list"""
    if not numbers:
        return None
    
    minimum = min(numbers)
    maximum = max(numbers)
    average = round(sum(numbers) / len(numbers), 2)
    return [minimum,maximum,average]

