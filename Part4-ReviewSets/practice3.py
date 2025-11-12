#1
# 20,8,7

#2
#NEXUS

#3
def game_mvp(players):
    bestplayer = ""
    bestratio = 0.0
    for name, stats in players.items():
        ratio = stats["kills"] / stats["deaths"]
    if ratio > bestratio:
        bestratio = ratio
        bestplayer = name
        return bestplayer