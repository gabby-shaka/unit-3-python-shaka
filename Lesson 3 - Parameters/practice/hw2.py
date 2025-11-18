# 5. 
# 18, 15

#6. 
def make_notification(user, *messages, urgent=False):
    all_messages = ""
    for i in range(len(messages)):
        if i > 0:
            all_messages = all_messages + ", "
        all_messages = all_messages + messages[i]
    output = user + " - " + all_messages
    if urgent == True:
        output = "URGENT: " + output
    return output

#7.
# SELECT name, email FROM users LIMIT 10
# SELECT * FROM logs WHERE level='error' LIMIT 5


#8. 

def log_action(actor, *actions, timestamp=None, **context):
    actions_text = ""
    for i in range(len(actions)):
        if i > 0:
            actions_text = actions_text + ", "
        actions_text = actions_text + actions[i]
    result = actor + ": " + actions_text
    if len(context) > 0:
        context_text = ""
        count = 0
        for key, value in context.items():
            if count > 0:
                context_text = context_text + ", "
            context_text = context_text + key + "=" + value
            count = count + 1
        
        result = result + " | " + context_text
    
    return result