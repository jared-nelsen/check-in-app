import random

generic_questions = [
    "How's it going?",
    "What's up?"
]

elaborativeQuestions = [
    "Really? Tell me more!",
    "Why are interested in this?"
]

def getGenericQuestion():
    return generic_questions[random.randint(0, len(generic_questions) - 1)]

def getElaborativeQuestion():
    return elaborativeQuestions[random.randint(0, len(elaborativeQuestions) - 1)]
