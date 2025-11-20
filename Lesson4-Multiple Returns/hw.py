#1
def search_user_database(query):
    if not query or query.strip() == "":
        return (None, "No search query", False)
    
    if not query.isalpha():
        return (False, "Invalid characters", False)

    if query == "john":
        count = 3
        return (count, f"Found {count} users", True)
    else:
        return (0, "No users found", True)

# TESTS 
print("=" * 50)
print("QUESTION 1: User Search Tests")
print("=" * 50)

print("\nTEST 1: Empty string")
result, message, success = search_user_database("")
print(f"Result: {result}")      # None
print(f"Message: {message}")    # "No search query"
print(f"Success: {success}")    # False

print("\nTEST 2: Whitespace only")
result, message, success = search_user_database("   ")
print(f"Result: {result}")      # None
print(f"Message: {message}")    # "No search query"
print(f"Success: {success}")    # False

print("\nTEST 3: Has numbers")
result, message, success = search_user_database("user123")
print(f"Result: {result}")      # False
print(f"Message: {message}")    # "Invalid characters"
print(f"Success: {success}")    # False

print("\nTEST 4: Has special characters")
result, message, success = search_user_database("user@email")
print(f"Result: {result}")      # False
print(f"Message: {message}")    # "Invalid characters"
print(f"Success: {success}")    # False

print("\nTEST 5: Valid query, no results")
result, message, success = search_user_database("admin")
print(f"Result: {result}")      # 0
print(f"Message: {message}")    # "No users found"
print(f"Success: {success}")    # True

print("\nTEST 6: Valid query with results")
result, message, success = search_user_database("john")
print(f"Result: {result}")      # 3
print(f"Message: {message}")    # "Found 3 users"
print(f"Success: {success}")    # True

# 2.
def analyze_book_pages(page_counts):
    if not page_counts:
        return (0, 0, 0.0, False)
    
    total_books = len(page_counts)
    total_pages = sum(page_counts)
    average_pages = total_pages / total_books 
    
    
    has_long_book = max(page_counts) > 500
    return (total_books, total_pages, average_pages, has_long_book)



print("\n" + "=" * 50)
print("QUESTION 2: Book Collection Tests")
print("=" * 50)

# TEST 1: Mixed collection with one long book
print("\nTEST 1: Mixed collection with long book")
count, total, avg, has_long = analyze_book_pages([250, 180, 620, 310])
print(f"Count: {count}")        # 4
print(f"Total: {total}")        # 1360
print(f"Average: {avg}")        # 340.0
print(f"Has long: {has_long}")  # True

# TEST 2: No long books
print("\nTEST 2: No long books")
count, total, avg, has_long = analyze_book_pages([200, 150, 300])
print(f"Count: {count}")        # 3
print(f"Total: {total}")        # 650
print(f"Average: {avg:.2f}")    # 216.67
print(f"Has long: {has_long}")  # False

# TEST 3: Empty list - EDGE CASE!
print("\nTEST 3: Empty list")
count, total, avg, has_long = analyze_book_pages([])
print(f"Count: {count}")        # 0
print(f"Total: {total}")        # 0
print(f"Average: {avg}")        # 0.0
print(f"Has long: {has_long}")  # False

# TEST 4: Exactly 500 pages - TRICKY!
print("\nTEST 4: Exactly 500 pages (NOT long)")
count, total, avg, has_long = analyze_book_pages([500, 400, 300])
print(f"Has long: {has_long}")  # False (500 is NOT > 500)

# TEST 5: Exactly 501 pages
print("\nTEST 5: Exactly 501 pages (IS long)")
count, total, avg, has_long = analyze_book_pages([501, 400, 300])
print(f"Has long: {has_long}")  # True (501 IS > 500)

print("\n" + "=" * 50)
print("All tests completed!")
print("=" * 50)