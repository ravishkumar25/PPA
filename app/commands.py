from datetime import datetime
from skills.greeting import greet


def execute_command(user):

    if user in ["hi", "hello"]:
        return greet()

    elif user == "time":
        return f"Current time is {datetime.now().strftime('%I:%M %p')}"

    elif user == "date":
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}"

    return None