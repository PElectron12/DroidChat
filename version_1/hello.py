import os
from gtts import gTTS

def say(text):
	tts = gTTS(text = str(text), lang = "en")
	tts.save("myfile.mp3")
	os.system("mpg321 myfile.mp3")

greetings = ["hi", "hello", "hey", "wassup", "yo"]
intro_questions = ["who are you","what are you", "what is your name","what do you do", "what should i call you", "tell me your name"]
birthQs = ["who created you", "how were you created", "how were you born", "who is your father"]
birthD = ["when is your birthday?", "when were you born?", "how old are you"]

sentence = raw_input("Please Enter Your Message:")

sentence = sentence.lower().strip()
answered = False

first_word = sentence.split(" ")[0]
if first_word[-1] in [",", "!", "."]:
    first_word = first_word[0:-1]

if first_word  in greetings:
    say("Hey There!")
    answered = True

for question in intro_questions:
    if question in sentence:
        say("Hey, I am DroidChat.")
        answered = True

for question in birthQs:
	if question in sentence:
		say("Paras created me.")
		answered = True

for question in birthD:
	if question in sentence:
		say("I was born on 8 May 2017.")
		answered = True

if not answered:
	say("I don't talk to people who don't know English!")


