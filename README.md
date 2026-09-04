# Pookie Bot — Python Chatbot

> A simple rule-based chatbot built with Python using predefined conversational responses.

## Overview

Pookie Bot is a beginner-friendly command-line chatbot that responds to user messages using a predefined collection of phrases and responses.

The chatbot matches the user's input against a dictionary of recognized messages and returns the corresponding response. If the input is not recognized, it provides a default response.

The project was built as an introduction to conversational programming and rule-based systems.

## Features

* Interactive command-line conversation
* Predefined responses for common phrases
* Basic greetings and small talk
* Responses to feelings and emotions
* Topic-based conversation starters
* Jokes and casual interactions
* Simple bot personality
* Exit commands
* Default response for unrecognized input

## How It Works

```text
User enters a message
        ↓
Convert input to lowercase
        ↓
Check for an exit command
        ↓
Search the response dictionary
        ↓
Return matching response
        ↓
If no match exists → Return default response
```

The chatbot does not use machine learning or natural language processing. It relies on exact phrase matching using a Python dictionary.

## Example

```text
Pookie Bot: Hi, my name is Pookie and I'm a chatbot.

You: hello
Pookie Bot: How are you doing today?

You: i'm excited
Pookie Bot: Ayyy love that energy! What’s happening?

You: let's talk about coding
Pookie Bot: Great. Where do you want to start?

You: bye
Pookie Bot: Bye!!
```

## Built With

* **Python 3**
* Python dictionaries
* Conditional statements
* `while` loops
* User input

## Concepts Practiced

This project helped me practice:

* Dictionaries and key-value pairs
* String manipulation
* User input
* Conditional logic
* `while` loops
* Program flow
* Functions and reusable logic
* Building a simple rule-based conversational system

## Running the Chatbot

Clone the repository and run:

```bash
python chatbot.py
```

Enter messages in the terminal to interact with Pookie Bot.

Type one of the supported exit commands to end the conversation:

```text
bye
done
see you later
talk later
```

## Limitations

Because Pookie Bot uses exact phrase matching, it can only respond to messages that have been explicitly defined in its response dictionary.

For example, if the bot recognizes:

```text
how are you
```

a variation such as:

```text
how are you doing
```

may not be recognized unless it has also been added to the dictionary.

This makes the project intentionally simple and provides a foundation for experimenting with more advanced conversational systems.

## Project Status

**Completed**

This is an early Python project exploring the fundamentals of conversational interfaces and rule-based chatbots.

## Author

**Ruvarashe Nemaramba**

Artificial Intelligence Student & Developer
