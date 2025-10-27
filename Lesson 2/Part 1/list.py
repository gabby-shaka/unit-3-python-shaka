""" 
Create - [1,2,3]
Add - .append(val
Remove end - .pop()
Insert- .insert(index,val)
Length - len(list)
Slice - [start:end]
Index - [0]

"""

# Creating lists
daily_likes = [500, 600, 750, 400]
usernames = ["@nasa","@tswift","@netflix"]
mixed_data = [500,"likes", "@user123", True]
# Accessing elements 
first_day = daily_likes[0]   #500
last_day = daily_likes[-1]   # 400 (neg. indexing)
third_day = daily_likes[2]
# Slicing (like JavaScript slice())
first_three = daily_likes[0:3]  #[500, 600, 750]
last_two = daily_likes[-2:]     #[750, 400]

# len, max, min, sum 


#code along - post analyzer
def analyze_posts(likes_list):
    if likes_list:
        total = sum(likes_list)
        average = total / len(likes_list)
        best_day = max(likes_list)
        return (average, best_day)
    return "The list is empty!" #no else or elif

def format_usernames(handles):
    formatted = []
    for username in handles:
        formatted.append("@" + username)
    return formatted

def format_username(handles):
    """ Add @ prefix to all usernames."""
    formatted = []
    for handle in handles:
        formatted.append("@" + handle)
    return formatted
result = format_usernames(["nasa","tswift", "netflix"])
print(result)


def trending_post(likes_list):
    """Return posts with over 1000 likes"""
    trending = []
    for likes in likes_list:
        if likes > 1000:
            trending.append(likes)
    return trending