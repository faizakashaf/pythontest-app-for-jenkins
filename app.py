from datetime import datetime

def get_greeting(name):
    current_hour = datetime.now().hour

    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    return f"{greeting}, {name}! Have a great day! 😊"

# Get user's name
user_name = input("Enter your name: ")
print(get_greeting(user_name))
