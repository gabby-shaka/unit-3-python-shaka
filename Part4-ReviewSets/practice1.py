#1 
#2,300

#2
#WOW WOW LFG

#3 

def find_biggest_donation(donation):
    topname = " "
    topdonation = -1
    for name, amount in donation.items():
        if amount > topdonation:
            topdonation = amount
            topname = name
    return