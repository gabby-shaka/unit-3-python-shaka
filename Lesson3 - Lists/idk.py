def format_course_code(code):  
    trimmed = code.strip()
    print(f"After strip: '{trimmed}' ")
    uppercased = trimmed.upper()
    print(f"After upper: '{uppercased}' ")
    return uppercased

def count_hastags (post):
    words = post.split()
    count = 0
    
    for word in words:
        if word.startswith("#"):
            count = count + 1
            
            return count 
        
