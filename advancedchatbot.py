import datetime

print("🤖 Smart Chatbot (type 'bye' to exit)")

name = ""

while True:
    user = input("You: ").lower()

    # Greeting
    if "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?")

    # Name memory
    elif "my name is" in user:
        name = user.split("my name is")[-1].strip()
        print(f"Bot: Nice to meet you, {name}!")

    elif "what is my name" in user:
        if name:
            print(f"Bot: Your name is {name}")
        else:
            print("Bot: I don't know your name yet.")

    # Time
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    # Basic conversation
    elif "how are you" in user:
        print("Bot: I'm doing great! What about you?")

    elif "fine" in user or "good" in user:
        print("Bot: Glad to hear that 😊")

    elif "thanks" in user:
        print("Bot: You're welcome!")

    # Help section
    elif "help" in user:
        print("Bot: You can ask me about time, tell me your name, or just chat!")

    # Exit
    elif "bye" in user:
        print("Bot: Goodbye! Have a great day!")
        break

    # Unknown input
    else:
        print("Bot: Hmm... I didn’t understand that. Try something else.")