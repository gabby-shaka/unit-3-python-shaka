#1 
# printed: x = {"key_a": "value1", key_b": 150} False

#2 
# printed: 120,60?

#3
def get_user_bio(user): 
    bio = user["bio"]
    return bio

get_user_bio({"username": "coder", "bio": "Python enthusiast"})
get_user_bio({"username": "newbie", "bio": "Beginner coder!"})
get_user_bio({"username": "code.er", "bio": "10 years of Python experience"})  
    

    

# 4 
# 60,160

#5 
# 2

#6
def get_total_engagement(post):
    likes = post.get("likes", 0)
    comments = post.get("comments", 0)
    shares = post.get("shares", 0)
    return likes + comments + shares

#7
# 3,3

#8
# {"key1": "value1", "key2": 200, "key3": 50}
# {"key1": "value1", "key2": 100, "key4" = True}

#9
def find_most_followed(users):
    if not users:
        return None
    
    max_user = users[0]
    for user in users:
        if user["followers"] > max_user["followers"]:
            max_user = user
    
    return max_user["username"]