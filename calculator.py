def divide(a, b):
     if b == 0:
          return None
    return a / b  # bug: no division by zero check

def calculate_average(numbers):
    total = sum(numbers)
    if not numbers:
        return 0
    return total / len(numbers)   # bug: crashes on empty list

def process_user_data(user_input):
    query = f"SELECT * FROM users WHERE name = '{user_input}'"  # bug: SQL injection
    return query

def read_config(filename):
    f = open(filename)  # bug: file never closed
    return f.read()

password = "admin123"  # bug: hardcoded credential
API_KEY = "sk-abc123xyz"  # bug: hardcoded secret
#hello
