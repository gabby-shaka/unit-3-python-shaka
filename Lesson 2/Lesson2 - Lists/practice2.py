def format_phone_number(phone):
    formatted = phone.replace(" ","").replace("-","")
    replace("(", "").replace(")","")
    
    if len(formatted)== 10:
        