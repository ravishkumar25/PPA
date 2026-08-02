from datetime import datetime


def run_assistant():
    print("PPA is online 🚀")

    while True:
        user = input("You: ").lower().strip()

        if user == "exit":
            print("PPA shutting down...")
            break

        elif user == "hi" or user == "hello":
            print("PPA: Hello Ravish! 👋")

        elif user == "time":
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"PPA: Current time is {current_time}")

        elif user == "date":
            current_date = datetime.now().strftime("%d %B %Y")
            print(f"PPA: Today's date is {current_date}")

        else:
            print("PPA: Sorry, I don't know that command yet.")