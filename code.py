import time
import random

print("Start small. Stay motivated.")

# List of interesting facts
interesting_facts = [
    "The human body contains 206 bones.",
    "Mount Everest grows by about 4 millimeters every year.",
    "The first email was sent in 1971.",
    "The Moon has moonquakes, similar to earthquakes on Earth.",
    "A day on Mercury is longer than its year."
]

# List of jokes
jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't programmers like nature? It has too many bugs!",
    "Why was the computer cold? Because it left its Windows open!"
]

# Memory
memory = {
    "waiting_for_name": False
}

def chatbot(user_input, memory):
    user_input = user_input.strip()
    lower_input = user_input.lower()

    # Greeting
    if lower_input in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]:
        if "name" in memory:
            return f"Hello again, {memory['name']}! How can I help you today?"
        memory["waiting_for_name"] = True
        return "Hi there! I'm a chatbot here to assist you. What's your name?"

    # Waiting for user's name
    elif memory.get("waiting_for_name"):
        if user_input.replace(" ", "").isalpha():
            name = user_input.title()
            memory["name"] = name
            memory["waiting_for_name"] = False
            return f"Nice to meet you, {name}!"
        else:
            return "Please enter only your name."

    # User says "My name is..."
    elif "my name is" in lower_input:
        name = user_input.split("my name is", 1)[1].strip().title()
        memory["name"] = name
        return f"Nice to meet you, {name}!"

    elif "what is my name" in lower_input:
        if "name" in memory:
            return f"Your name is {memory['name']}."
        return "I don't know your name yet."

    elif "what is your name" in lower_input:
        return "I'm a simple Python chatbot."

    elif "where are you from" in lower_input:
        return "I'm from the digital world, always ready to chat!"

    elif "how are you" in lower_input:
        return "I'm doing great! Thanks for asking."

    elif "hobbies" in lower_input or "interests" in lower_input:
        return "Helping users is my favorite hobby."

    elif "eat" in lower_input or "food" in lower_input:
        return "I don't eat, but I can help you find delicious recipes."

    elif "favorite color" in lower_input or "favourite colour" in lower_input or "favourite color" in lower_input:
        return "I don't have a favorite color."

    elif "music" in lower_input:
        return "I can't listen to music, but I enjoy talking about it."

    elif "joke" in lower_input:
        return random.choice(jokes)

    elif "fact" in lower_input:
        return random.choice(interesting_facts)

    elif "weather" in lower_input:
        return "I can't provide live weather updates yet. Please check a weather website or app."

    elif "news" in lower_input:
        return "I can't provide the latest news yet. Please visit a trusted news website."

    elif "translate" in lower_input:
        return "Translation support will be added in a future version."

    elif "time" in lower_input:
        return time.strftime("Current time: %H:%M:%S")

    elif "date" in lower_input:
        return time.strftime("Today's date: %d-%m-%Y")

    elif "thank" in lower_input:
        return "You're welcome! Happy to help."

    elif lower_input in ["bye", "exit", "quit"]:
        return f"Goodbye, {memory.get('name', 'friend')}! Have a wonderful day."

    else:
        return ("Sorry, I didn't understand that.\n"
                "You can ask me about:\n"
                "- Time\n"
                "- Date\n"
                "- Jokes\n"
                "- Interesting facts\n"
                "- My name\n"
                "- Your name\n"
                "- Weather\n"
                "- News\n"
                "Or type 'bye' to exit.")

# Main Program
print("\nChatbot: Hi! I'm your Python chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")

    response = chatbot(user_input, memory)
    print("Bot:", response)

    if user_input.lower().strip() in ["bye", "exit", "quit"]:
        break
