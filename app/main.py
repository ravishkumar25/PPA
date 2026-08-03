from app.assistant import run_assistant

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    reply = run_assistant(user)
    print("Vexa:", reply)