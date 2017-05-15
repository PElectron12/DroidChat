
from espeak import espeak

greetings = ["hi", "hello", "hey", "ola", "hallo", "wassup", "yo", "hie", "hii"]
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
    espeak.synth ("Hey There!")
    answered = True

for question in intro_questions:
    if question in sentence:
        espeak.synth("Hey, I am DroidChat.")
        answered = True

for question in birthQs:
	if question in sentence:
		espeak.synth("Paras created me.")
		answered = True

for question in birthD:
	if question in sentence:
		espeak.synth("I was born on 8 May 2017.")
		answered = True

if not answered:
	espeak.synth ("I don't talk to people who don't know English!")

while espeak.is_playing:
	pass
