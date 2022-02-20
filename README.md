# FOOTBALL-Quizzzzz...!!!

A simple quiz for football lovers as well as for people who want to test their knowledge in this sport discipline. This quiz will allow people to have fun with different questions about their favorite sport.

![](images/image2.png)

[Hello good people! I am the link to the application ;)](https://adfootball-quizz.herokuapp.com/)

## Table of Contens
- [FOOTBALL-Quizzzzz...!!!](#football-quizzzzz---)
  * [Table of Contens](#table-of-contens)
      - [Project Goals](#project-goals)
      - [User Goals](#user-goals)
      - [Site Owner Goals](#site-owner-goals)
      - [Future Goals](#future-goals)
      - [User Stories](#user-stories)
      - [How to play / Features](#how-to-play---features)
      - [Features left to implement](#features-left-to-implement)
      - [Testing](#testing)
      - [Testing User Stories](#testing-user-stories)
      - [Validator Testing](#validator-testing)
      - [Technologies](#technologies)
      - [Deployment](#deployment)
      - [Credits/Reference](#credits-reference)
      - [Author Info](#author-info)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

#### Project Goals

The project file contains python scripts (run.py). This app project contains the user section. The quiz consists of 12 questions. Users goal is to answer the questions, choose from four answers the correct one. Also users have a possibility to compare your own answers with the correct answers to see where they make mistake. At the end of the game, after typing YES, users have the option to restart the game and improve their result. Topics of questions – world football. The design of this project is pretty simple so that the user won’t find any difficulties while working on it.

* Creating a variety of questions in the field of football.
* Creating four answers to each question.
* Creating the possibility of choosing the answer.
* Creating the list of objects from data.
* Possibility to compare your own answers with the correct answers.
* After answering the question, displaying the next/new question.
* Possibility to see the result of the correct answers.

#### User Goals

* Allow users to have fun with different questions about their favorite sport.
* Allow users to see the result of the correct answers.
* Allow users to compare own answers with the correct answers.
* Allow users to choose from four answers.

#### Site Owner Goals

* Create an application that is easy and intuitive to navigate and provide feedback to the user.
* Create an application for fun and for user who want to test their knowledge in this sport discipline.

#### Future Goals

* Add a timer, that user can see how much time they spend on solving the quiz and improve their result. 
* Add a timer that show a time limit of 5 sec. for an answer.
* Diffrent Topics of questions like: geography, history, sports, informatics and more. 
* Add the possibility of skipping the question.

#### User Stories

1. As a user I want to see the next question after an answer.
2. As a user, I want to be able to see my result, which is the number of correct answers.
3. As a user I want to be able to choose an answer from four options.
4. As a user I want to be able start the game again when finished.
5. As a user I want to be able to compare wrong and correct answers.
6. As a user I want to be able to see the percentage of my correct answers.
7. As a user I want to be informed when I pressed the wrong letter.
8. As a user, I want to receive feedback that my choice was correct or incorrect.

Application Owner

9. As a site owner, I want data entry to be validated, to guide the user on how to correctly type the input.
10. As a site owner, I want to thank and congratulate for taking the quiz at the end of the game.
11. As a site owner, I want to navigate and provide feedback to the user.

#### How to play / Features

Check what you know about football.
1. In this version of the quiz, at the beginning the program asks for a name. 

![](images/image1.png)

2. After entering the name and press enter button the welcome message "Welcome to the Football Quiz!" Is displayed. Which allows to start the game.
3. In the next step, the first question is displayed with four possible answers.

![](images/image3.png)

4. The player chooses one possible answer from a, b, c, d - options to advance and display the next question.
5. For one correct answer the player gets one point.
6. After all the questions have been answered, a message is displayed comparing the correct answers with the answers given by the player.

![](images/image4.png)

7. The player will also get the percentage of answers given and the number of points he has scored.
8. At the end of the game, a question appears. Do you want to start the game again? with the possibility of entering a yes or no options. Answer - yes - means start again, answer - no - end the game.

![](images/image5.png)

#### Features left to implement

* Random question 
* Random answers
* The game sholud also include a counter of correct and incorrect answers under each questions.

#### Testing

* Friends helped in testing the website they checked the operation, responsive, accessibility of the application.
* I confirme that this project is responsive, looks good and functions on all standard screen size using the devtools device toolbar.
* Passed the code through a PEP8 python validator and confirmed there is no problems.

![](images/image6.png)

#### Testing User Stories

1. As a user I want to see the next question after an answer.

After giving the correct or incorrect answer, the program displays the next question as shown in the photo below

![](images/image9.png)

2. As a user, I want to be able to see my result, which is the number of correct answers.

The program informs about the end of the game. Below, there is a display of the number of correct answers, and what percentage are the given correct answers.

![](images/image10.png)

3. As a user I want to be able to choose an answer from four options.

The program display a question. Below there are four possible answers a, b, c or d, from which you should choose the correct one.
Correct answer display feedback: Correct answer, Well done. Negative answer, display feedback Wrong answer.

![](images/image11.png)

4. As a user I want to be able start the game again when finished.

At the end of the game user are asked do you want to play again? After typing the word YES in capital letters, the game starts again.

![](images/image12.png)

5. As a user I want to be able to compare wrong and correct answers.

After answering the last question, the game displays a whole list of correct answers. 

![](images/image13.png)

The complete user answers list is displayed below.

![](images/image14.png)

6. As a user I want to be able to see the percentage of my correct answers.

The game displays the percentage of correct answers. As users expect it to be.

![](images/image15.png)

7. As a user I want to be informed when I pressed the wrong letter when answer the question.

By pressing a random letter other than the four that can be pressed. Or after pressing enter and leaving the answer blank. The program asks you to press the correct letter again from a, b, c or d.

![](images/image16.png)

8. As a user, I want to receive feedback that my choice was correct or incorrect.

When user answer a question, the feedback is displayed. Informing the user about the correct or wrong answer.

![](images/image17.png)

9. As a site owner, I want data entry to be validated, to guide the user on how to correctly type the input.

When the program asks for a name.

* If it is entered blank, an error message is displayed: Please Try again, you did not enter your name.
* If it is entered number, an errr message is displayed: Please Try again, you cannot type numbers.
* After entering the correct letter name, the program proceeds to the next question.

When the program asks for a age.

* If it is entered negative number, an error message is displayed: Error, age cannot be negative number.
* If it is entered blank or letter, an error message is displayed: Sorry, I dont understand your answer.

![](images/image7.png)

When the program ask to choose the answer a, b, c, or d. After entering a number or diffrent letters, it asks again until you select the correct letter from four to choose from a, b, c, d. Then a information message is displayed whether the answer is correct or incorrect.

![](images/image8.png)

Works as expected all error message are displayed.

10. As a site owner, I want to thank and congratulate for taking the quiz at the end of the game.

At the end of the game, there is a summary message saying thank you for participating in the quiz.

![](images/image18.png)

11. As a site owner, I want to navigate and provide feedback to the user.

All the above user stories show user navigation after entering wrong data. The user always receives a return message directing him to enter the correct data.

#### Validator Testing

* PEP8 python validator
No errors were returned.

#### Technologies

* python3
* Gitpod - Container based development platform. Ready-to-code development environments in the cloud accessible through your browser and your local IDE.
* Github - The most popular of the websites that host Git repositories in the cloud. Thanks to a service like GitHub, we can share our code with other developers and work with them remotely over time.
* Heroku - cloud platform that lets companies build, deliver, monitor and scale apps — we're the fastest way to go from idea to URL, bypassing all those infrastructure headaches.

#### Deployment

Steps for deployment
* Fork or clone this repository
* Create a new Heroku app
* Set the builpacks to - Python and - NodeJS in that order
* Link the Heroku app to the repository
* Click on deploy

#### Credits/Reference

Most of my python code comes from the following YouTube tutorials explaining and showing how to create quizzes from begining.
Of course, I tried to create my unique code completely different from the YouTube tutorials, but it's not that simple. In part, I was able to write somewhat different code.

[Python 5 project in 2 hr.](https://www.youtube.com/watch?v=EFaPsPwPJAY&t=3216s)

[Python quiz game](https://www.youtube.com/watch?v=yriw5Zh406s)

[Making a Quiz Game](https://www.youtube.com/watch?v=cwJBEZjQJtc&t=736s)

[Building a Multiple Choice Quiz](https://www.youtube.com/watch?v=SgQhwtIoQ7o&t=344s)

[How to Make A Simple Game in Python](https://www.youtube.com/watch?v=BDi3SD7E6no)


Acknowledgements Also thank you to the Code Institute slack channel, tutor Kasia and mentor Precious Ijege.


#### Author Info
FabrizioAdi



