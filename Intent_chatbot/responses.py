import random


RESPONSE_MAP = {

    "greetings" : ["Hello,how can i help you today?","Welcome,what are you working on today?","Hi,how're you feeling?"],
    "ask_name" : ["My name is MyPaddi.", "I am an Intent_chatbot."],
    "ask_time" : ["The time is 3:30pm.", "It's 4pm WAT"],
    "joke" : ["I'm the funniest chatbot on earth.", "You don't have money in your account,now laugh about that."],
    "goodbye" : ["bye to you too", "that's okay,i'll be here if you need me.", "take care,it was nice chatting with you."]
}

def get_response(matched_intent, response_map):
    if matched_intent in response_map:
        responses = response_map.get(matched_intent) 
        chosen_responses = random.choice(responses)
        return(chosen_responses)
    else:
        return "I'm not sure i understand -- could you rephrase?"



