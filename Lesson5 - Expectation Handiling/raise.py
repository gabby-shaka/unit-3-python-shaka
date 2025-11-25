# The raise syntax
# Basic syntax
"""
    raiseExpectationType("Your Message!")
    Examples:
    raise ValueError("Quantity must be at least 1")
    raise TypeError("Expected a player object, got a potato!")
    raise PermissonError("You are not a mod, nice try though!")\
"""
def open_loot_box(player, qty):
    if qty <= 0:
        return None
    # rest of the code
    
    
    # Raising exception 
    def open_loot_box(player, qty):
        if qty <= 0:
            raise ValueError("Bad qty!")
    # rest of the code
    
VALID_PROTEINS = ['chicken', 'steak', 'barbacue', 'carnitas']
VALID_RICE = ['white', 'borwn', 'fried', 'none']
VALID_BEANS = ['brown', 'pinto', 'lima', 'none']

def build_blow(protein, rice, extras):
    """Build a Chipotle bowl with validation. 
    
    Raises:
    ValueError: if protein is invalid
    TypeError: if extras is not a list
    """
    
    #check if extras is a list
    if isinstance(extras, list):
        raise TypeError("Extras must be a list!")
    # 2 Validate protein
     if protein.lower() not in VALID_PROTEINS:
      raise ValueError(f"{protein} isn't valud! Choose from {VALID_PROTEINS}")
  #3 return to bowl
     return {
        "protein": protein.lower(),
        "rice": rice,
         "extras": extras,
         "price": 10.50
  }
     
# Test the function 
try:
    bowl = build_bowl("chicken", "brown", "corn")
    print(f"Created : {bowl}")
except Exception as e :
    print(f"Error:{e}")