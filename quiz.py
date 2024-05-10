print("It\'s time for a quiz!")
print("This is a fun quiz for you to hopefully get a good time out of. Respond to the answers with any letter from A to D")
print("Don\'t try to take this so seriously :).\n")
a_count = 0
b_count = 0
c_count = 0
d_count = 0
correct_count = 0
check = False
while check == False:
    first_answer = input("How do you greet a new co-worker in a work setting? \n"
                         "A. Welcome them and accidentally call them your boss \n"
                         "B. \"Yes.\" \n"
                         "C. Greet them and ensure they are comfortable with their new workplace \n"
                         "D. Scream excitedly at their face\n")
    first_answer = first_answer.upper()
# while check == False:
    if first_answer not in ('A', 'B', 'C', 'D'):
        print("No.")
        # first_answer = input("How do you greet a new co-worker in a work setting? \n"
        #                  "A. Welcome them and accidentally call them your boss \n"
        #                  "B. \"Yes.\" \n"
        #                  "C. Greet them and ensure they are comfortable with their new workplace \n"
        #                  "D. Scream excitedly at their face\n")
        # first_answer = first_answer.upper()

    else:
        if first_answer == 'C':
            correct_count += 1
            check = True
        else:
            check = True


check = False
while check == False:
    second_answer = input("Who is the playable character in the classic arcade game Pac-Man? \n(No-one said these were business questions only.)\n"
                          "A. Pac-Man \n"
                          "B. Ghost Hunter \n"
                          "C. Kazuma Kiryu \n"
                          "D. Super Mario \n")
    second_answer = second_answer.upper()
# while check == False:
    if second_answer not in ('A', 'B', 'C', 'D'):
        print("No.")
        # second_answer = input("Who is the playable character in the classic arcade game Pac-Man? \n(No-one said these were business questions only.)\n"
        #                      "A. Pac-Man \n"
        #                      "B. Ghost Hunter \n"
        #                      "C. Kazuma Kiryu \n"
        #                      "D. Super Mario \n")
        # second_answer = second_answer.upper()

    else:
        if second_answer == 'A':
            correct_count += 1
            check = True
        else:
            check = True


check = False
third_answer = input("Doctor Who is a British Science Fiction show that has been around for over how many years? \n"
                      "A. 20 years \n"
                      "B. 60 years \n"
                      "C. 100 years \n"
                      "D. Doctor What \n")
third_answer = third_answer.upper()
while check == False:
    if third_answer not in ('A', 'B', 'C', 'D'):
        print("No.")
        third_answer = input("Doctor Who is a British Science Fiction show that has been around for over how many years?\n"
                             "A. 20 years \n"
                             "B. 60 years \n"
                             "C. 100 years \n"
                             "D. I still don\'t know what you are talking about. \n")
        third_answer = third_answer.upper()
    else:
        if third_answer == 'B':
            correct_count += 1
            check = True
        else:
            check = True
#print(correct_count)

print("Congratulations! You have finished the quiz.\n"
      "Now, let's see how you did!")

if correct_count == 3:
    print("Wow, now there is someone who knows what they\'re talking about. You are a quizzing natural!\n"
          "I mean...unless you got lucky at just those questions.\n"
          "Hmm, well either way you did well! Nice work.")
elif correct_count >= 1:
    print("Hmm, okay, so, there is room for improvement definitely...well to be fair it\'s not like this quiz matters too much.\n"
          "I mean seriously, you don\'t need to know the facts of those last two anyway, so....\n"
          "I would say getting any score at all is fine honestly...so long as you aren\'t serious if you got question 1 wrong.\n"
          "...I hope I am right in thinking that.")
else:
    print("Okaaay, so uh, that was not good. Not good at all. You are seeing this message if you got nothing right.\n"
          "That means you got the co-worker interaction wrong too...I hope you didn\'t pick D.\n"
          "...Please tell me you didn\'t pick D. Oh no....")

print("Your final score is " + str(correct_count) + ". Please consider playing again sometime!")

#def p_ans(p_input, correct):
