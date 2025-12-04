#15. 
def calculate_average(numbers):
    
    if not numbers:
        return 0

    total = sum(numbers)
    average = total / len(numbers)
    return average

grades = []
result = calculate_average(grades)
print(f"Average: {result}") 

#16. 
# C)

#17. 
text = " Hello Python World "
clean = text.strip()
upper = text.upper()
words = text.strip().split()
length = len(text.strip())

#18. 
def validate_password(password):
    if not password:
        return False,
    
    if len(password) < 8:
        return False,

    return True,

print(validate_password("")) 
print(validate_password("abc")) 
print(validate_password("secure123")) 

#19. 
def create_inventory(item_name, *quantities, location="Warehouse"):
    total = sum(quantities) if quantities else 0
    return {
        "item": item_name,
        "total": total,
        "location": location
}
    
print(create_inventory("Widget", 10, 20, 15))

#20.
def safe_list_access(items, index):
    try:
        value = items[index]
        return value, True
    except IndexError:
            return None, False

print(safe_list_access([10, 20, 30], 1)) 
print(safe_list_access([10, 20, 30], 10)) 
print(safe_list_access([], 0)) 