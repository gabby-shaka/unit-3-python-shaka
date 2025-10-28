def create_username(first_name, last_name):
      username = "first_name" + "_" + "last_name"
      return username.lower()

def create_slug(title):
    slug = title.strip().lowe().replace(" ", "-")
    def check_email(email): 
            email_lower = email.lower()      
            if "@" in email_lower and email_lower.endswith(".com"):
                return True
            return False

     def check_email(email):
                email_lower = email.lower()
                return "@" in email_lower and email_lower.endswith(".com")
    
