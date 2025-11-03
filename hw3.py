def sanitize_filename(filename):
    clean = filename.lower().replace(" ", "_")
    safe = ""
    for char in clean:
        if char.isalnum() or char in ".-_":
            safe += char
    if not safe.endswith(".txt"):
        if "." in safe:
            safe = safe[:safe.rfind(".")]
        safe += ".txt"
    if len(safe) > 50:
        safe = safe[:46] + ".txt"  # 46 + 4 = 50
    return safe
