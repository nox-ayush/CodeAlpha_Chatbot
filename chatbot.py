import datetime
import random

def get_current_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_current_date():
    return datetime.datetime.now().strftime("%A, %d %B %Y")

def start_alphabot():
    banner = r"""
 █████╗ ██╗     ██████╗ ██╗  ██╗ █████╗ ██████╗  ██████╗ ████████╗
██╔══██╗██║     ██╔══██╗██║  ██║██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
███████║██║     ██████╔╝███████║███████║██████╔╝██║   ██║   ██║   
██╔══██║██║     ██╔═══╝ ██╔══██║██╔══██║██╔══██╗██║   ██║   ██║   
██║  ██║███████╗██║     ██║  ██║██║  ██║██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝   
"""
    print(banner)
    print("=" * 70)
    print("Bot: Hey there! I'm AlphaBot, your terminal buddy.")
    print("Bot: Let's chat. Type 'help' if you want to see what I can do.")
    print("Bot: Type 'bye' or 'exit' whenever you want to leave.\n")

    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the Python developer get cold? Because they left their Windows open!",
        "There are 10 types of people in the world: those who understand binary, and those who don't."
    ]

    fun_facts = [
        "Python was named after the comedy show 'Monty Python's Flying Circus', not the snake!",
        "The first computer bug was an actual real moth found inside a computer in 1947.",
        "Honey never spoils. Archaeologists have found pots of honey over 3,000 years old that are still good!"
    ]

    user_name = ""

    # Main interaction loop
    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Exiting session. Take care!")
            break

        # Check for empty input
        if not user_input:
            print("Bot: Don't be shy! Type something to talk.")
            continue

        text = user_input.lower()

        # Exit conditions
        if text in ["bye", "exit", "quit", "see ya", "goodbye"]:
            if user_name:
                print(f"Bot: Goodbye {user_name}! It was great talking to you.")
            else:
                print("Bot: Take care! Hope to catch you again soon.")
            break

        # Help menu
        elif text == "help":
            print("\nBot: Here are a few things you can ask me:")
            commands = [
                "Greetings (e.g., 'hello', 'hey')",
                "Share your name (e.g., 'My name is Ayush')",
                "Ask current time or date (e.g., 'what is the time', 'date')",
                "Ask for a joke or fact (e.g., 'tell me a joke', 'fun fact')",
                "About me (e.g., 'who are you', 'who created you')"
            ]
            for cmd in commands:
                print(f"  • {cmd}")
            print()

        # Name saving logic
        elif "my name is" in text:
            name_parts = user_input.split()
            for idx in range(len(name_parts)):
                if name_parts[idx].lower() == "is" and idx + 1 < len(name_parts):
                    user_name = name_parts[idx + 1].capitalize()
                    break

            if user_name:
                print(f"Bot: Awesome to know you, {user_name}! How can I help you today?")
            else:
                print("Bot: I missed your name there, could you tell me again?")

        # Bot identity
        elif "who are you" in text or "your name" in text:
            print("Bot: I'm AlphaBot! A rule-based terminal assistant built for the CodeAlpha internship.")

        elif "who made you" in text or "developer" in text or "creator" in text:
            print("Bot: I was built in Python using pure logic, conditions, and loops without any external APIs!")

        # Well-being queries
        elif "how are you" in text:
            print("Bot: Running at full speed and feeling great! How is your day going?")

        elif "good" in text or "fine" in text or "great" in text:
            print("Bot: That's awesome to hear! Keep that momentum going.")

        # Real-time queries
        elif "time" in text:
            print(f"Bot: The current system time is {get_current_time()}.")

        elif "date" in text or "today" in text or "day" in text:
            print(f"Bot: Today's date is {get_current_date()}.")

        # Fun responses
        elif "joke" in text or "funny" in text:
            print(f"Bot: Haha, check this out:\n\"{random.choice(jokes)}\"")

        elif "fact" in text:
            print(f"Bot: Here's a cool fact:\n\"{random.choice(fun_facts)}\"")

        # Greeting variations check
        elif any(greet in text.split() for greet in ["hi", "hello", "hey", "hola"]):
            if user_name:
                print(f"Bot: Hey {user_name}! What are we working on right now?")
            else:
                print("Bot: Hey there! How can I assist you today?")

        elif "thank" in text:
            print("Bot: Anytime! Always happy to help.")

        # Fallback response
        else:
            print("Bot: I'm not sure how to answer that yet.")
            print("Bot: Type 'help' to see what topics and commands I know!")

# Direct call to start the chatbot
start_alphabot()