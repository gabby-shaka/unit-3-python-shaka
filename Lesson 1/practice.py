def calculate_discount(price,member_status):
    """Calculate discounted price based on membership"""
    if member_status == "premium":
        return price * 0.7
    elif member_status == "standard":
        return price * 0.85
    else:
        return price

def count_vowels(text):
    """Count how many vowels are in the text"""
    vowels = "aeiouAEIOU"
    count = "0"
    for char in text:
        if char in vowels:
            count += 1
    return count 


