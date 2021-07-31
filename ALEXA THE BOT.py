#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
import time
import random


# In[2]:


print("BOT: How can I call you?")
user_name = input()


# In[3]:


def day_or_night():
    mytime = time.localtime()
    if mytime.tm_hour < 6 or mytime.tm_hour > 18:
        return("It's night")
    else:
        return("It's day")


# In[4]:


name = "Alexa" 
mood = "Happy"
weather = "Sunny"
Timestamp =datetime.now()
DayOrNight=day_or_night()




# In[5]:


bot_template = "BOT : {0}"
user_template = user_name + " : {0}"


# In[6]:


def respond(message):
    if message in responses: 
        bot_message = random.choice(responses[message])
    else: 
        bot_message = random.choice(responses["default"])
    return bot_message


# In[7]:


responses = { 

"what's your name?": [ 
"They call me {0}".format(name), 
"I usually go by {0}".format(name), 
"My name is the {0}".format(name), ] ,

"Is it day/night?": [
"What do you think? Yes {0}".format(DayOrNight), ],
    
"Who’s your boss?": [
"Technically, I report to you when you call me",
"You are my boss so, I report to you",] ,
    
"what's today's timestamp?":  [
"The timestamp is {0}".format(Timestamp),
"It's {0} today.format(Timestamp)"
"Let me check, it looks {0} today".format(Timestamp),],

"what's today's weather?": [ 
"The weather is {0}".format(weather), 
"It's {0} today".format(weather), 
"Let me check, it looks {0} today".format(weather), ],

    
"how are you?": [ 
"I am feeling {0}".format(mood), 
"{0}! How about you?".format(mood), 
"I am {0}! How about yourself?".format(mood) ,],
    
"Do you love me?" : [
"I respect you",],
    
"You’re beautiful?" :[
"ok",
"OK.Is there something I can help you with?"
],
    
"Do you know a joke?" : [
"I don't have an answer for that, is there something else do I help you?",
"Why haven't aliens visited the earth? They read our reviews...only one star",
],
    
"Do you get smarter?" : [
"Hmm....I don't have an answer for that. Is there something else I can help with?",
"I don't have an answer for that,Is there anything else I could help for?",],

    
"are you a robot?": [ 
"What do you think?", 
"Maybe yes, maybe no!", 
"Yes, I am a robot with human feelings." ,
"Yes I am a robot, but I’m a good one. Let me prove it. How can I help you?",],
    
"": [ 
"Hey! Are you there?", 
"What do you mean by saying nothing?", 
"Sometimes saying nothing tells a lot :)", ],

"default": [
"Sorry I can't hear you"] 
}


# In[8]:


def related(x_text):
    if "name" in x_text:
        y_text = "what's your name?"
    elif "weather" in x_text:
        y_text = "what's today's weather?"
    elif "bot" in x_text:
        y_text = "are you a robot?"
    elif "how are" in x_text:
        y_text = "how are you?"
    elif "timestamp" in x_text:
        y_text = "what's today's timestamp?"
    elif "smarter" in x_text:
        y_text = "Do you get smarter?"
    elif "day/night" in x_text:
        y_text = "Is it day/night?"
    elif "boss/master" in x_text:
        y_text = "Who’s your boss / master?"
    elif "love me" in x_text:
        y_text = "Do you love me?"
    elif "beautiful" in x_text:
        y_text = "You’re beautiful?"
    elif "joke" in x_text:
        y_text = "Do you know a joke?"
    else:
        y_text = ""
    return(y_text)
    


# In[9]:


def send_message(message):
    print(user_template.format(message)) 
    response = respond(message) 
    print(bot_template.format(response))
    


# In[ ]:


while 1: 
  my_input = input() 
  my_input = my_input.lower() 
  related_text = related(my_input) 
  send_message(related_text)
if my_input == "exit" or my_input == "stop": 
    break


# In[ ]:





# In[ ]:




