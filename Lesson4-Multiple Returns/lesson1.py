def search_data(query):
    if query == "":
        return None #no query provided
    if query == "empty":
        return 0 # found zero results
    if query == "error":
        return False #search failed
    return len(query) # Normal case - return cost 

#1 Return Type - None -> "No Value"
#Meaning: Abesense of value, not set, not found
#Use for: Missing Data, search failure, optional parameters
result = None
print(result is None) #True - identity check 
print(result == None) #True - equality check 
print (not result)    #True - falsy check 

#2  Return Type - False = Boolean False
# MEANING: Explicit false condition, validation failure, negative result 
#Use for: Validation result, boolean operations, success/failure status
result = False
print(result is False) #True - identity check 
print(not result) # True - boolean negation 
print(result == 0) #True - falsy check 

#3 Return Zero - A Valid Number 
# Zero is a VALID numeric value, not absense of value!
result = 0
print(result == 0)  #True - numeric equality 
print(not result) #True - (falsey in boolean context)
print(result is None) #False - different object 
print(result is False) #False - different types

# Multiple Returns - python packs multiple returns into a tuple!
def calculate_room(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter      #(Turns into a tuple)


result = calculate_room(10, 5)
print(result)
print(type(result))

print(type((42))) #int
print(type((42,))) #tuple for single item
no_parentheses = 1,2,3
print(type((no_parentheses))) #tuple

#unpacking tuple 
area_result, perimeter_result = calculate_room(20,6)
print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_result}")

# Practice 1
def analyze_grades(grades):
    """Returns Avg, High, Low, Passed
    if no grades, return, 0,0,0 False"""
    if not grades:
        return 0,0,0,False
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    passed = average >= 60
    
    return average, highest, lowest, True/False
    