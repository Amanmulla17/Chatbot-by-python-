def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    greetings = ['hi', 'hello', 'hey']
    if any(greet in user_input for greet in greetings):
        return "Hello! How can I help you today?"

    # Working hours
    elif "hours" in user_input or "open" in user_input or "working time" in user_input:
        return "Our working hours are from 9 AM to 6 PM, Monday to Friday."

    # Product inquiry
    elif "product" in user_input or "sell" in user_input or "what do you have" in user_input:
        return "We sell a variety of electronics, including laptops, smartphones, and accessories."

    # Return policy
    elif "return" in user_input or "refund" in user_input:
        return "Our return policy allows returns within 30 days of purchase. Please keep your receipt."

    # Contact info
    elif "contact" in user_input or "phone number" in user_input or "email" in user_input:
        return "You can reach us at support@example.com or call us at (123) 456-7890."

    # Default fallback
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase your question?"

# Main loop to interact with the chatbot
if __name__ == "__main__":
    print("Customer Service Chatbot 🤖 (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Thank you for visiting! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)