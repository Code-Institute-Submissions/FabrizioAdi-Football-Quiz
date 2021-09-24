# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


def run_game():
    choices = []
    correct_choices = 0
    question_number = 1
    
    for key in questions:
        print("********************QUESTION********************")
        print(key)
        for i in answers[question_number-1]:
            print(i)
        choice = input("Choose the correct answer(a, b, c or d):")
        choices.append(choice)

        check_answer(questions get(key),choice)

        question_number += 1


def check_answer(answer, choice):

    if answer == choice:
        print("CORRECT ANSWER! WELL DONE!")
        return 1

# Question section

questions = {
    "Who is the winner of Premier League (England) 2020/21?":"a",
    "Which international club does Lionel Messi play for?":"c",
    "Who broke Gerd Müller's record for the most goals scored in a single Bundesliga season?":"a",
    "What international team play in Wembley?":"a",
    "Which of these teams is from Turin?":"d",
    "How long is a game of professional football?":"b",
    "How many times have Brazil won the World Cup?":"d",
    "Which international club does Robert Lewandowski play for?":"a",

}
# Answers sections with choices
answers = [["a. Manchester City", "b. Manchester United", "c. Chelsea London", "d. Leicester City"],
["a. Italy", "b. Uruguay", "c. Argentina", "d. USA"],
["a. Robert Lewandowski (Pol)", "b. Gerd Muller (Ger)", "c. Cristiano Ronaldo (Por)", "d. Thomas Muller (Ger)"],
["a. England", "b. Denmark", "c. Sweden", "d. Scotland"],
["a. AC Milan", "b. SSC Napoli", "c. Atletico", "d. Juventus"],
["a. 60 minutes", "b. 90 minutes", "c. 75 minutes", "d. 45 minutes"],
["a. Three times", "b. Four times", "c. Six times", "d. Five times"],
["a. Poland", "b. Russia", "c. Italy", "d. France"]]

# ********************
# ********************

run_game()