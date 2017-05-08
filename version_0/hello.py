sentence = raw_input("Please Enter Your Message:")

sentence = sentence.lower().strip()
answered = False

first_word = sentence.split(" ")[0]
if first_word[-1] in [",", "!", "."]:
    first_word = first_word[0:-1]

if first_word  in ["hi", "hello", "hey", "ola", "hallo", "wassup", "yo", "hie", "hii"]:
    print "Hey There!"
    answered = True

intro_questions = ["who are you","what are you", "what is your name","what do you do", "what should i call you", "tell me your name"]

for question in intro_questions:
    if question in sentence:
        print "Hey, I am Paras ... How are You?"
        answered = True

if not answered:
	print "I am not in a mood to talk right now!"

