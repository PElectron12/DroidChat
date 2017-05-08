text = raw_input("Please Enter Your Message:")

text = text.lower()
text = text.strip()

if text  in ["hi", "hello", "hey", "ola", "hallo", "wassup", "yo", "hie"]:
    print "Hey, I am Paras ... How are You?"
elif text in ["who are you?", "who are you", "what are you?", "what are you", "what is your name?", "what is your name",
 "what do you do?", "what do you do", "what should i call you", "what should i call you?", "tell me your name?", "tell me your named"]:
	print "I am DroidChat, a ChatBot."
else:
	print "I am not in a mood to talk right now!"
 
