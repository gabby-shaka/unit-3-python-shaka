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