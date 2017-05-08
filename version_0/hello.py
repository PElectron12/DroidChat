text = raw_input("Please Enter Your Message:")

text = text.lower()
text = text.strip()

if text  in ["hi", "hello", "hey", "ola", "hallo", "wassup", "yo", "hie"]:
    print "Hey, I am Paras ... How are You?"
else:
    print "I am not in a mood to talk right now!"
