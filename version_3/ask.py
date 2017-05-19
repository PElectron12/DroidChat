import os


def write_to_file(text):
    file_writer = open("qa.txt", "a")
    file_writer.write(text)
    file_writer.close()

if os.path.exists("qa.txt"):
    file_reader = open("qa.txt", "r")
else:
    temp = open("qa.txt", "w")
    temp.close()
    file_reader = open("qa.txt", "r")

all_questions = []
all_answers   = []
def load_qas():
    global all_questions, all_answers
    lines = file_reader.readlines()
    index = 0
    for line in lines:
        line = line.strip("\n")
        if index%2 == 0:
            all_questions.append(line)
        else:
            all_answers.append(line)
        index += 1

def register_new_qa(q, a):
    to_write = q + "\n" + a + "\n"
    write_to_file(to_write)
    load_qas()

found_it = False
bot_answered = False

print "Talk to me! (For telling me to calculate something, write 'Calculate: ' and then the expression to be calculated, in numerals.)"
load_qas()
while True:
    user_question = raw_input("User: ")
    user_question = user_question.lower()
    user_question = user_question.replace("!","")
    user_question = user_question.replace("?","")
    user_question = user_question.replace(".","")

    for x in ["hi", "hello", "hi there", "hi, droidchat", "hello, droidchat", "hi there, droidchat"]:
        if (not user_question in all_questions) and x in user_question:
	    print "DroidChat: " + "Hi!"
	    bot_answered = True
	    found_it = True
	    break
    if bot_answered != True:
    	    if user_question in all_questions:
                question_number = all_questions.index(user_question)
	        print "DroidChat: " + all_answers[question_number]
		found_it = True
	    elif "calculate: " in user_question:
	        user_question = user_question.replace("calculate: ", "")
		print "DroidChat: " + user_question + " " + "is equal to" + " " + str(eval(user_question))
		found_it = True
	    else:
	        found_it = False
		for q in all_questions:
	            if user_question in q or q in user_question:
	                question_number = all_questions.index(q)
	                print "DroidChat: " + all_answers[question_number]
	                found_it = True
	                break

    if not found_it:
                ans = raw_input("I don't know, please give me something to tell other users who might ask the same question! ")
		add_q = raw_input("Question forms? (Seperate questions with space) ")
		user_question = add_q
		user_question = user_question.lower()
		if len(ans)>0:
                    register_new_qa(user_question, ans)
                    print "Your response has been added."

