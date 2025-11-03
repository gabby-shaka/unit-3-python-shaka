# 2
def find_top_players(players, min_score):
   top_players = []
   for player in players:
       if player ["score"] >= min_score:
           top_players.append(player["username"])
           return top_players

players = [
    {"username": "DragonSlayer", "score": 8500}
    {"username": "NinjaWarrior", "score": 6200}
    {"username": "MageKing", "score": 9100}
    {"username": "ShadowAssassin", "score": 5800}
    ]
result = find_top_players(players<7000)
print(result)

# question 3

# 9
# EYE OF THE TIGER 
# BLINDING LIGHTS