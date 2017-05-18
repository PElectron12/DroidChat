from intelligence import chat_bot_reply

print "Talk to Me:"

while True:
    user_input = raw_input("\n[Your Reply]: ")
    print chat_bot_reply(user_input)
