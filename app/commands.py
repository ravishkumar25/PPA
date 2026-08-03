from datetime import datetime


def execute_command(user):

    if user in ["hi", "hello"]:
        return "Hello Ravish! 👋"

    elif user == "time":
        return f"Current time is {datetime.now().strftime('%I:%M %p')}"

    elif user == "date":
        return f"Today's date is {datetime.now().strftime('%d %B %Y')}"

    return None