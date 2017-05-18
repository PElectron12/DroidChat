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


print "Talk to me"
load_qas()
while True:
    print all_questions, all_answers
    user_question = raw_input("User: ")
    if user_question in all_questions:
        question_number = all_questions.index(user_question)
        print all_answers[question_number]
    else:
        ans = raw_input("I don't know, please give me an ans for this!")
        if len(ans)>0:
            register_new_qa(user_question, ans)
            print "Thank You!"
        
