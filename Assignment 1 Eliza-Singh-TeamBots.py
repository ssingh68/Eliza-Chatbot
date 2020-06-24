# =============================================================================
# #Programming Assignment 1 - Eliza Chatbot
# 
# #Team Members - Abhishek Shambhu , Jeyamurugan Krishnakumar & Shreyans Singh
#
# #Team Name - Team Bots
#
# #Description - We started by importing the regular expression(re), random, datetime and time library.
# Then we added the dictionary for most used nouns(Noun_reflections) and pronouns(Pronoun_reflections)
# which would help us in word spotting from the questions and transform it according to the answers.
# Then we added the Expressions as in Regular Expressions - using the re library to match the 
# questions or statements given by user as input and then some random answers(using the random
#  library)
#
# #What out Chatbot can do? - We have tried to implement the chatbot using pattern matching techniques - 
# Regular Expressions or Regexes which allows the chatbot to converse with a human by following the rules 
# and directions of the script. 
# This chatbot, in specific, can engage in a conversation based on certain patterns. 
# Although this chatbot does not explictly recognize complex word mathcing, minimal context it attempts
# to present itself in a humane manner since only regexes were used.
#
# =============================================================================
#Importing Regular expressions
import re
#Importing random module to get random responses
import random
#Importing system datatime to greet the user based on time
import datetime
#importing time for time.sleep() functionality so that the responses of ELIZA looks real
import time

#Dictionary where we are replacing some noun words in the user input sentence with its corresponding pair(Word Spotting)
Noun_dict = {
    "crave": "craving",
    "avoid": "avoiding",
    "celebrate": "celebration",
    "resent": "resentment",
    "feel": "feeling",
    "forgive": "forgiveness",
    "smoke": "smoking",
    "arrange": "arrangement",
    "write": "writing",
    "prefer": "preference",
}

#Dictionary where we are replacing most common pronoun words in the user input sentence with its corresponding pair(Word Spotting)
Pronoun_dict = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

#Expressions list containing a two element list i.e. key value pair. 
#The first is the regular expression and the second is a list of responses and
#any of the possible response is selected any shown as output by ELIZA
Expressions = [
#   I want ...       
    [r'(?i)I want (.*)',
     ["Do you really want {0}?",
      "Will it make you happy if you get {0}?",
      "Why do you need {0}?"]],

#   Do you ...?     
    [r'(?i)Do you ([^\?]*)\??',
     ["Yes, I do.",
      "No, I do not {0} because I am a chatbot.",
      "Kinda."]],
 
#   I need ...    
    [r'(?i)I need (.*)',
     ["Will you be fine if you don't get {0}?",
      "Will it make you happy if you get {0}?",
      "Why do you need {0}?"]],
    
#   I don't/dont need ...      
    [r'(?i)I don\'?t need (.*)',
     ["Are you sure you do not need {0}?",
      "But I really think you need {0}.",
      "Do you want my help in getting you {0}?"]],

#   Yes ...    
    [r'(?i)(Y|y)es(.*)',
     ["I am really excited to hear that.",
      "Tell me more about it?"]],     
     
#   No ...
    [r'(?i)(N|n)o(.*)',
     ["Don't be so negative.",
      "You should definetely give it a try!"]],

#   ...tell...joke   
     [r'(?i)tell(.*)joke(.*)',
     ["Friday is my second favourite F word.",
      "If a stranger offers you a piece of candy..take two!!"]], 

#   I am...
    [r'(?i)I am (.*)',
     ["Are you proud that you are {0}?",
      "Are you happy to be {0}?",
      "I am not surprised by that!"]],
 
#   I m...
    [r'(?i)I\'?m(.*)',
     ["How do you feel being {0}?",
      "For how long have you been {0}?",
      "Why do you think you are {0}?"]],

#   Are you... 
    [r'(?i)Are you ([^\?]*)\??',
     ["What would happen if I was not {0}?",
      "I am not sure whether I am {0}. What do you think?"]],

#   I think I...
    [r'(?i)I think I(.*)',
     ["Why don't you tell me more about your {0}?"]],

#   I think I'm...  
    [r'(?i)I think I\'m(.*)',
     ["Why don't you tell me more about your {0}?"]],

#   ...sorry...
    [r'(.*)sorry(.*)',
     ["I am just a chatbot. I do not require any apology.",
      "What feelings do you have when you apologize?",
      "There are many times when no apology is needed."]],

#   What...        
    [r'(?i)What ([^\?]*)\??',
     ["Why do you ask that?",
      "Is this thing really important to you?",
      "What do you think?"]],

#   How...
    [r'(?i)How ([^\?]*)\??',
     ["I am not sure about that.",
      "Just believe in your instincts!",
      "Why do you think that?"]],

#   Because...
    [r'(?i)(b|B)ecause(.*)',
     ["Is this true?",
      "What else crosses your mind?"]],

#   ...I think ...
    [r'(?i)I think (.*)',
     ["Do you really believe so?",
      "Are you sure?"]],

#   ... family ...
    [r'(.*)family(.*)',
     ["Where does your family live?",
      "How many people are there in your family?"]],

#   Is it ...     
    [r'(?i)Is it([^\?]*)\??',
     ["If it were {0}, what would you do?"]],

#   It is... 
    [r'(?i)It is (.*)',
     ["You seem very certain.",
      "If I told you that it probably isn't {0}, what would you feel?"]],

#   Can you... 
    [r'(?i)Can you ([^\?]*)\??',
     ["I am just a chatbot. I am not God!!",
      "What if I could {0}?",
      "Will it make you happy if I could {0}"]],

#   Can I... 
    [r'(?i)Can I ([^\?]*)\??',
     ["I am not pushing you. It is all upto you if you want to {0}",
      "Do you think you could {0}?"]],

#   Question    
     [r'(.*)\?',
     ["I believe you can answer this yourself",
      "Is it really necessary to answer this?",
      "I never thought abut it"]],

#   Statement 
    [r'(.*)',
     ["Can you please elaborate more?",
      "Ohh. I see. Does it make you feel happy?",
      "That is interesting!",
      "What do you mean?",
      "Try explaining more about it"]]
     
]
   
#The reflect function takes input and it turns it to lower case, splits it to words and strip the word from both sides.
#Then we do a for loop to check this word with all the words in our noun and pronouns dictionary and if found in dictionary 
#replace that word with its key value pair.

def correspond_words(response_match):
     words = response_match.lower().split()
     for index, word in enumerate(words):
         if word in Pronoun_dict:
             words[index] = Pronoun_dict[word]
         if word in Noun_dict:
             words[index] = Noun_dict[word]
     return ' '.join(words)

def process(user_input):  
    #Here, we are doing for loop to match our input with all the patterns in expressions
    for pattern, responses in Expressions:
        #Here, we compare input statement with the pattern in expressions and see whether it matches.
        match = re.match(pattern, user_input.rstrip(".!"))
        if match:
            #Based on adequate match it will give random responses for that match that was entered and will return a response from the list.
            response_match = random.choice(responses)
            for words in match.groups():
                return response_match.format(*[correspond_words(words)])
            
#This is the main Eliza interface function
def elisa():
    #Print function where Eliza introduces herself and asks for username
    print("ELIZA: Hi, I'm ELIZA a psychotherapist. What is your name?")
    #User entered input is taken in name_sentence variable
    name_sentence = input("USER: ")
    #time.sleep(secs) will pause the execution so that the chatbot's reply looks real 
    time.sleep(2)
    #Here, i am splitting each word from input entered in a list
    sent_split = name_sentence.split()
    #Here, i am taking the last word into name as the user might enter
    #Ex. my name is abhishek or you can call me by abhishek
    #So, considering last word as name and taking that as input
    name = sent_split[-1]
    
    #Here, i wanted to greet the user based on the system time
    currentTime = datetime.datetime.now()
    times = currentTime.hour
    if 5 <= times < 12:
        greet = 'Good Morning.'
    elif 12 <= times < 16:
        greet = 'Good Afternoon.'
    elif 16 <= times < 20:
        greet = 'Good Evening.'
    else:        
        greet = "It's night now."
    
    #Print function where it replies with name and greetings
    print(f"ELIZA: Hi {name}. {greet} What do you want to ask me today?")
    while True:
        #
        exit_list = ("goodbye","Goodbye","Bye","bye","See you later","quit","Quit","Exit","exit")
        user_input=input("USER: ")
        if user_input in exit_list:
            #If input entered is from any of the above list prints ending message and ends the conversation
            print("ELIZA: Have a nice day. Good bye Human!")
            break
        else:
            #time.sleep(secs) will pause the execution so that the chatbot's reply looks real
            time.sleep(2)
            #display matched response after processing based on input entered 
            print("ELIZA: "+process(user_input))
        
if __name__ == "__main__":
  elisa()
        