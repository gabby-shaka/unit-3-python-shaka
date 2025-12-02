# SCOPE - the visibility of variables, where it can be seen & used
# GLOBAL - outside all functions
# LOCAL - inside the function(only visible there)

# THE BUG - CRASHES(UnboundLocalError)
def add_bonus():
    score = score + 100 # = -> python thinks it's local 

score = 500
add_bonus()

