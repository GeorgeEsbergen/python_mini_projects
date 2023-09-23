quiz = {
    "Question 1":{
        "question" :"What is the Capital of Egypt ? ",
        "answer" : "Cairo"
    },
    "Question 2":{
        "question" :"How Many bits in an int in c++ ? ",
        "answer" : "32"
    },
    "Question 3":{
        "question" :" Does flutter has null safety ?",
        "answer" : "Yes"
    },
    "Question 4":{
        "question" :" Python has array ? ",
        "answer" : "No"
    },
    "Question 5":{
        "question" :" python have Dictionary ? ",
        "answer" : "Yes"
    },
    "Question 6":{
        "question" :" Where Ronaldo play ? ",
        "answer" : "Elnasr"
    },
    "Question 7":{
        "question" :"What is the Capital of France ? ",
        "answer" : "Paris"
    },
    "Question 8":{
        "question" :"What is the Capital of England ? ",
        "answer" : "London"
    },
    "Question 9":{
        "question" :"What is the Capital of USA ? ",
        "answer" : "Washinton"
    },
    "Question 10":{
        "question" :"What is the Capital of China ? ",
        "answer" : "bla"
    },
}


score = 0 ; 


for key ,value in quiz.items():
    print(f'{value["question"]} \n')
    answer = input()

    if answer.lower()== value["answer"].lower():
        score=score+10


if score <70 :
    print("You Failed ")
else:
    print(f"Congratulations , You Passed !! , \n  And Your score is {score}")    