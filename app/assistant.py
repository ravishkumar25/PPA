from commands import execute_command


def run_assistant():
    print("PPA is online 🚀")

    while True:
        user = input("You: ").lower().strip()

        if user == "exit":
            print("PPA shutting down...")
            break

        response = execute_command(user)

        if response:
            print("PPA:", response)
        else:
            print("PPA: Sorry, I don't know that command yet.")