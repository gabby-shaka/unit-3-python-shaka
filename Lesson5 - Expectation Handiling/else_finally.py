try:
    # try something risky
    score = int(input("Enter score: "))
except ValueError:
    #Runs if it FAILED
    print("Invalid score!")
else: 
    print(f"Score recorded: {score}")
    



def parse_command(message):
    """Parse a Discord command like: !ban PlayerName 7 days"""
    try:
        parts = message.split()
        command = parts[0]
        target = parts[1]
        duration = parts [2]
    except IndexError:
        print("Invalid Command Format - Missing parts")
        return None
    else:
        print("Command parsed successfully!")
        if command.startswith("!"):
            print(f"Executing: {command}")
        return command, target, duration 
    finally: #runs no matter what
        print("This block runs regardless!")
        
result = parse_command("!ban PlayerName 7 days")
print(result)
result2 = parse_command("!ban")
print(result2)