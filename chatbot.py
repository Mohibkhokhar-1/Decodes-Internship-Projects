print("=======================================")
print("      Welcome to AI Chatbot")
print("Ask me a question.")
print("Type 'bye' to exit.")
print("=======================================")

responses = {
    "hello": "Hello! Nice to meet you.",
    "hi": "Hi! How can I help you?",
    "hey": "Hey! Welcome.",

    "how are you?": "I am fine. Thank you for asking.",
    "what is your name?": "My name is AI Chatbot.",
    "who created you?": "I was created using Python.",
    "what can you do?": "I can answer simple questions.",

    "what is python?": "Python is a programming language.",
    "why should i learn python?": "Python is easy to learn and widely used in AI and Web Development.",
    "is python easy?": "Yes, Python is one of the easiest programming languages.",

    "what is ai?": "AI stands for Artificial Intelligence.",
    "what is artificial intelligence?": "Artificial Intelligence allows computers to perform tasks that normally require human intelligence.",
    "what is machine learning?": "Machine Learning is a branch of AI that learns from data.",
    "what is deep learning?": "Deep Learning is an advanced field of Machine Learning.",
    "what is a chatbot?": "A chatbot is a computer program that talks with users.",

    "what is programming?": "Programming means writing instructions for a computer.",
    "what is coding?": "Coding is the process of writing computer programs.",
    "what is html?": "HTML is used to create web pages.",
    "what is css?": "CSS is used to design web pages.",
    "what is javascript?": "JavaScript makes websites interactive.",

    "what is a computer?": "A computer is an electronic machine that processes data.",
    "what is the internet?": "The Internet connects computers around the world.",
    "what is technology?": "Technology helps solve problems using scientific knowledge.",

    "can you help me?": "Yes! Ask me any simple question.",
    "are you a human?": "No, I am a rule-based AI chatbot.",
    "where do you live?": "I live inside this Python program.",
    "what is your favorite language?": "My favorite language is Python.",

    "thank you": "You're welcome!",
    "thanks": "Happy to help!",
    "good morning": "Good Morning!",
    "good afternoon": "Good Afternoon!",
    "good evening": "Good Evening!",
    "good night": "Good Night! Have a nice sleep."
}

while True:

    user = input("\nYou: ")
    user = user.lower()

    if user == "bye" or user == "exit" or user == "quit":
        print("Bot: Goodbye! Have a great day.")
        break

    elif user in responses:
        print("Bot:", responses[user])

    else:
        print("Bot: Sorry, I don't understand your question.")