import sys
import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

answers = {}

def ask_questions(questions):
    for type, question in questions.iteritems():
        print question
        x = raw_input()
        if x =='yes' or x =='y' or x =='Y' or x=='YES': 
            answers[type] = True
        else:
            answers[type] = False
    return answers
        
def make_drink(answers):
    drink = []
    for type, answer in answers.iteritems():
        if answers[type] == True:
            drink.append(random.choice(ingredients[type]))
        
    print "Your drink contains a {}.".format(', '.join(map(str, drink)))
    
if __name__ == '__main__':
    ask_questions(questions)
    make_drink(answers)