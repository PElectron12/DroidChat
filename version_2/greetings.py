from common import *
import random

greetings_list = [
{
syn: ["hi", "hello", "yo", "hey", "hie"],
reply: self,
opt_suf: ["there", "!", "."]
},
{
syn: ["bye", "goodbye", "see you again", "nice to talk to you", "take care", "talk to you later", "need to go", "gtg", "tyl", "tty"],
reply: self,
opt_suf: type_noun(bot),
},
{
sim: ["morning", "evening", "night", "afternoon"],
reply: self,
opt_pre:["good"],
int_algo:figure_time(user),
},
{
    syn: ["nice", "well done", "great", "great work", "wow", "awesome", "nice job", "good", "fine"],
reply: ["thanks", ask(why)],
int_algo: figure_context(conversation)
}

]

def send_reply(words):
    first_word = words[0]
    last_word  = words[-1]
    reply_user = ""
    confidence = 0
    hi_greetings = greetings_list[0][syn]
    for word in hi_greetings:
        if word == first_word:
            confidence += 50
            if len(words)>1:
                if words[1] in greetings_list[0][opt_suf]:
                    confidence += 5
            break
        elif word in first_word:
            confidence += 40
            for word in greetings_list[0][opt_suf]:
                if word in first_word:
                    confidence += 15
                    break
            break
    if greetings_list[0][reply] == self:
        greet_list = greetings_list[0][syn]
        random.shuffle(greet_list)
        reply_user = greet_list[0]
    return reply_user, confidence
