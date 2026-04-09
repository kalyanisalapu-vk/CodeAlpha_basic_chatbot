def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "your name" in user_input:
        return "I am a simple chatbot!"
    elif "time" in user_input:
        return "I don't know the time now 😅"
    elif "thanks" in user_input:
        return "You're welcome!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day 😊"
    else:
        return "I'm sorry, I don't understand that."
def start_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_message = input("You: ")
        response = get_bot_response(user_message)
        print(f"Chatbot: {response}")
        
        if "bye" in user_message.lower():
            break
if __name__ == "__main__":
    start_chatbot()