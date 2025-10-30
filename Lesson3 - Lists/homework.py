#1

email = "Gabriella.Shaka@Gmail.COM"
standard = email.lower()
username = standard.split("@")[0]
domain = standard.split("@")[1]
print(username, domain)
# (this prints john.smith gmail.com)

#2

text = "The Quick Brown Fox"
words = text.split()
initials = ""
for word in words:
    initals += word[0].lower()
print(initials)
#(this prints tqbf)

#3
def extract_domain(email):
    at_count = email.count("@")
    if at_count != 1:
        return "Invalid"
    parts = email.lower().split("@")
    domain = parts[1]
    return domain

#4 
message = "Hello123World456"
digits = ""
for char in message:
    if char.isdigit():
        digits += char 
print(digits)
# (this prints '123456')

#5 
filename = "my-document.txt"
nameonly = filename.replace(".txt", "")
safename = nameonly.replace("-", "_")
result = safename.upper()
print(result)
#(this prints MY_DOCUMENT)

#6
data = "apple,banana,cherry,date"
items = data.split(",")
longest = items[0]
for item in items:
    if len(item) > len(longest):
        longest = item
    print(longest)
    # (this prints banana)
#7
    def filternum(text):
        result = ""
        for char in text:
            if not char.isdigit():
                result += char
        return result
    
#8 
url = "https://example.com/users/profile"
parts = url.split("/")
protocol = parts[0]
domain = parts[2]
path = "/".join(parts[3:])
print(f"{protocol}//{domain/path}")
#(this prints ???)

#9
letters = 0
digits = 0 
spaces = 0 
def countchartype(text):
 
    for char in text:
        if char.isalpha():
            letters += 1
         elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
        return {
        "letters": letters,
        "digits": digits,
        "spaces": spaces
    }