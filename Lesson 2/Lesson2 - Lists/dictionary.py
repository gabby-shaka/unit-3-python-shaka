"""
Python Dictionaries - Student Starter Code
Unit 3, Lesson 2
"""

# =============================================================================
# PART 1: Creating and Accessing Dictionaries
# =============================================================================

# TODO: Create a user dictionary with username, followers, and verified keys


# TODO: Access the followers value


# TODO: Add a new key "posts" with value 120


# TODO: Delete the "verified" key



# =============================================================================
# PART 2: Dictionary Methods
# =============================================================================

# TODO: Use .get() to safely access a key that might not exist


# TODO: Loop through all keys in the dictionary


# TODO: Loop through all values in the dictionary


# TODO: Loop through all key-value pairs using .items()



# =============================================================================
# PART 3: Dictionaries in Functions
# =============================================================================

def get_display_name(user):
    """Return the display name from a user dictionary."""
    # TODO: Return user["name"] if it exists, otherwise return "Anonymous"
    pass


def update_score(player, points):
    """Add points to a player's score."""
    # TODO: Add the points to player["score"]
    pass


# =============================================================================
# CHALLENGE: Engagement Calculator
# =============================================================================

def analyze_post(post):
    """
    Calculate total and average engagement for a post.
    
    Parameters:
        post (dict): Dictionary with "likes", "comments", and "shares" keys
    
    Returns:
        dict: Dictionary with "total" and "average" keys
    """
    # TODO: Calculate total engagement (likes + comments + shares)
    
    # TODO: Calculate average engagement (total / 3)
    
    # TODO: Return a dictionary with total and average (rounded to 2 decimals)
    pass


# Test your function
if __name__ == "__main__":
    post = {"likes": 100, "comments": 20, "shares": 10}
    result = analyze_post(post)
    print(result)
    # Expected output: {"total": 130, "average": 43.33}
    
    
    """
Python Dictionaries - Student Starter Code
Unit 3, Lesson 2 Part3
"""

# =============================================================================
# PART 1: Creating and Accessing Dictionaries
# =============================================================================

# Creating a dictionary
user = {
    "username": "nasa",
    "followers": 50000,
    "verified": True
}

# Accessing values
count = user["followers"]  # 50000

# Adding a new key-value pair
user["posts"] = 120

# Deleting a key
del user["verified"]

# Dictionary after modifications:
# {"username": "nasa", "followers": 50000, "posts": 120}


# =============================================================================
# PART 2: Dictionary Methods
# =============================================================================

# .get() method - safe access (avoids KeyError)
bio = user.get("bio", "No bio available")  # Returns default if key doesn't exist

# .keys() - get all keys
for key in user.keys():
    print(key)

# .values() - get all values
for value in user.values():
    print(value)

# .items() - get all key-value pairs
for key, value in user.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "username" in user:
    print(user["username"])

# Copy a dictionary
user_copy = user.copy()


# =============================================================================
# PART 3: Dictionaries in Functions
# =============================================================================

# EXAMPLE 1: Passing dictionaries to functions
def get_display_name(user):
    """Return the display name from a user dictionary."""
    return user.get("name", "Anonymous")

# EXAMPLE 2: Modifying dictionaries in functions
def update_score(player, points):
    """Add points to a player's score."""
    player["score"] += points  # Modifies original dictionary

# EXAMPLE 3: Returning dictionaries from functions
def create_product(name, price):
    """Create and return a product dictionary."""
    return {
        "name": name,
        "price": price,
        "in_stock": True
    }


# =============================================================================
# LOOPING PATTERNS
# =============================================================================

# Pattern 1: Loop through keys only
for key in user:
    print(key)

# Pattern 2: Loop through keys and values
for key, value in user.items():
    print(f"{key}: {value}")

# Pattern 3: Loop through values only
for value in user.values():
    print(value)
