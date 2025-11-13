# Using keyword arguments
def create_gamer(username, level, xp, rank, online):
    """Create a gamer profile.""" #returns as a dictionary
    return {
        "username": username, 
        "level": level,
        "xp": xp,
        "rank": rank,
        "online": online, 
    }
    
player1 = create_gamer(username= "BTStudent", 
                       level=25
                       rank="Gold"
                       xp=10000
                       online=True)
print(player1) #dictionary with all values will be printed


def send_message(sender, recipient, message, urgent):
    """Send message beteen users"""
    
    return f"{sender} -> {recipient}: {message} (Urgent: {urgent})"

def post_content(username, text, likes=0, retweets=0):
    return f"@{username}: {text} | ❤️ {likes} 🔄️ {retweets}"
  
    
    
# *args - Accept any number of values

def sum_scores{*scores}
"""Sum ANY number of scores"""
total = 0
    for score in scores:
        total += score
    return total