from datetime import datetime

def greet():
    current_hour = datetime.now().hour

    if current_hour < 12:
        return "Good morning! ☀️"
    elif current_hour < 18:
        return "Good afternoon! 🌤️"
    else:
        return "Good evening! 🌙"

print(greet())
