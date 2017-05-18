import greetings
import common

def normalize(data):
    return data.strip().lower()


def chat_bot_reply(u_data):
    u_data = normalize(u_data)
    words  = u_data.split()

    reply, confidence = greetings.send_reply(words)
    return reply, confidence
