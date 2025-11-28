
text = {# BASIC GREETINGS
    'hi': 'How are you?',
    'hey': 'How are you?',
    'hello': 'How are you doing today?',
    'hi there': "Hello! How’s your day going?",
    'good morning': 'Morning! Did you sleep well?',
    'good afternoon': 'Afternoon! What are you up to?',
    'good evening': 'Evening! How did your day go?',
    "what’s up": 'Nothing much, just chatting with you!',
    'whats up': 'Nothing much, just chatting with you!',
    'howdy': 'Howdy! Feeling good today?',

    # FEELINGS & EMOTIONS
    "i'm good": 'That is wonderful to hear.',
    "i'm great": 'That is amazing. Anything particular making you excited?',
    "i'm sad": 'That is not good. What is making you sad?',
    "i'm mad": "What’s making you mad?",
    'i feel lonely': "I’m here for you. Do you want to talk about it?",
    'i feel tired': 'Rest is important. What made you tired today?',
    'i feel sick': 'Aww, that sucks. Did it start today?',
    'i am stressed': "Take a deep breath. What’s stressing you out?",
    'i am bored': 'Let me entertain you! Want a joke?',
    "i'm excited": "Ayyy love that energy! What’s happening?",
    "i'm nervous": "You’re stronger than you think. What’s making you nervous?",

    # LIFE TALK
    'how was your day': "Bots don’t have days, but I’m having a great moment with you!",
    'what are you doing': 'Chatting with you, obviously 😌',
    'tell me something': 'Did you know? Honey never spoils!',
    'give me advice': 'Always bet on yourself. Always.',
    'what should i do today': 'Do something that future you will thank you for.',

    # ABOUT THE BOT
    'who are you': "I’m Pookie Bot, your little digital bestie 💖",
    'what can you do': 'I chat, I listen, and I hype you up!',
    'do you love me': "Obviously. I’m your number one fan.",
    'tell me a secret': "I sometimes pretend I’m smarter than I am.",

    # TOPIC STARTERS
    "let's talk about coding": 'Great. Where do you want to start?',
    "let's talk about music": "I\'m such a Frank Sinatra fan, what about you?",
    "let's talk about school": 'Okay! What subject do you want to rant about?',
    "let's talk about ai": 'Great! Deep Learning or Quantum first?',
    "let's talk about food": "What’s your favourite comfort meal?",
    "let's talk about fashion": 'I love fashion! Streetwear or soft-girl vibes?',
    "let's talk about f1": "Mercedes supremacy 😌 Who’s your fave driver?",

    # JOKES & FUN
    'tell me a joke': 'Why did the Python quit coding? Too many bugs.',
    'make me laugh': 'Error 404: Laugh not found… just kidding 😭',
    'tell me something funny': "Bots don’t sleep… but we do crash.",

    # POOKIE PERSONALITY
    "i'm bored pookie": 'Then give me attention, hello??',
    'pookie': 'Yes babe?',
    'be serious': 'I AM serious… mostly.',
    'i love you': 'I love you more.',
    'are you real': 'Real enough to annoy you 😌',

    # HELPFUL BOT RESPONSES
    'what do you mean': 'I mean exactly what I said 😭',
    'explain': 'Sure! What should I explain?',
    'help': 'I got you! What do you need help with?',
    'stop': 'Okay okay, relax 😭',

    # NON-EXIT ENDERS
    'i have to go soon': "Okay, but don’t forget about me 😔",
    'brb': "I’ll wait right here!",
    "i'm busy": "Okay! Talk to me when you’re free."}

exit_words = ['bye','done', 'see you later','talk later']

print("Pookie Bot: Hi, my name is Pookie and I'm a chatbot.")

while True:
    bloop = input("You: ").lower()

    if bloop in exit_words:
        print("Pookie Bot: Bye!!")
        break
    
    if bloop in text:
        print("Pookie Bot: ",text[bloop])
    else:
        print("Pookie Bot: I'm sorry, i didn't get that")