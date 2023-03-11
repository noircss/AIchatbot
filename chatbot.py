import random

# Define some possible user inputs and corresponding chatbot responses
greetings = ["hello", "hi", "hey", "greetings", "hi there"]
greeting_responses = ["Hello! How can I help you today?", "Hi there! What can I assist you with?", "Hey! How can I be of service?"]

goodbyes = ["bye", "goodbye", "see you later", "cya"]
goodbye_responses = ["Goodbye! Have a great day.", "See you later!", "Until next time!"]

thanks = ["thanks", "thank you", "thanks a lot", "thank you very much"]
thankyou_responses = ["You're welcome!", "No problem!", "Glad I could help."]

unknown_responses = ["I'm sorry, I didn't understand. Can you please rephrase that?", "I'm not sure what you mean. Can you please clarify?", "I'm having trouble understanding. Can you please try again?"]

# Define a function to get a response from the chatbot
def get_response(user_input):
    if user_input.lower() in greetings:
        return random.choice(greeting_responses)
    elif user_input.lower() in goodbyes:
        return random.choice(goodbye_responses)
    elif user_input.lower() in thanks:
        return random.choice(thankyou_responses)
    else:
        return random.choice(unknown_responses)

# Start the chatbot
print("Hi, I'm a chatbot. How can I assist you?")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        break
    response = get_response(user_input)
    print(response)
