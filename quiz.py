import time
dots = "-----------------------------"

# <<<<<<<<<<<<<<<<<<<<<<<<<questions>>>>>>>>>>>>>>>>
questions = {
    "What is the capital of Iran ?": "B",
    "What is the capital of Turkey ?": "C",
    "What is the capital of America ?": "D",
    "What is the capital of azerbaijan ?": "A",
}

# <<<<<<<<<<<<<<<<<<<<<<<<< options >>>>>>>>>>>>>>>>
options = [
    ["A) Urmia", "B) Tehran", "C) Isfahan", "D) Paris"],
    ["A) Istanbul", "B) berlin", "C) Ankara", "D) Antalya"],
    ["A) New York", "B) Baku", "C) California", "D) Washington"],
    ["A) Baku", "B) Berlin", "C) Tehran", "D) Tabriz"]
]

def new_game():

    # We use this list to append the answers to it!
    guesses = []

    # We use it no know how many correct guesses we have.
    # And it will be increase when user answered the question correctly.
    correct_guesses = 0

    # We use question number to show the number of the question.
    # It's important for the for loop in down below to show the right answers for each question.
    question_num = 0

    # We will use this variable for the answer of the user
    guess = None

    # The items in the list will be only options that user can use.
    guess_options = ["A", "B", "C", "D"]


    for key in questions:
        print(dots)

        # We used for loop for printing questions one by one and key is the question!
        print(f"{question_num+1}) {key} \n")

        for i in options[question_num]:
            # We used this for loop for printing the options
            # accordingly for the related question.
            print(i)

        # here after we printed the question and all the related answers for each question,
        # we use while to get correct option that are among of guess_options variable.
        while guess not in guess_options:
            guess = input("$ Enter (A, B, C or D) :").upper()

        # Here we have added user's answer to the guesses list.
        guesses.append(guess)

        # Here we called check_answer function to check the result and return
        # the value 0 or 1.
        correct_guesses += check_answer(questions.get(key), guess)

        # Here we changed the value of guess to None for the next round of for loop.
        guess = None

        question_num += 1

    # When the questions overed display_score will be called for printing the result!
    display_score(correct_guesses, guesses)

# -----------------------------

def check_answer(answer, guess):
    # In this function we are checking user's answer if it's true of not!
    # If it wes correct 1 will be returned, if it was false 0 will be returned!
    if answer == guess:
        print("CORRECT!")
        return 1
    print("WRONG!")
    return 0

# -----------------------------

def display_score(correct_guesses, guesses):

    # Here we are calculating the result!
    score = correct_guesses / len(guesses)
    score = int(score*100)

    # We have created result list to print result fancier!
    result = ["Your", "score", "is", score, "%"]
    print(dots)

    print("The result :\n")
    print("The correct answers :", end=" ")
    # In the for loop below, the correct answers will be printed side by side!
    for i in questions.values():
        print(i, end=" ")
    print()

    print("Your answers :", end=" ")
    # In the for loop below, the user's answers will be printed side by side!
    for i in guesses:
        print(i, end=" ")
    print()

    time.sleep(3)
    # We used the code in top line to stop printing for 3 sec!
    # We used bottom loop to print the result fancier!
    for i in result:
        print(i, end=" ")
        time.sleep(1)
    print()
# -----------------------------

def play_again():
    # Here we are asking for one more round; If user printed y or yes,
    # function will return true otherwise it will return false.
    response = input("Would you like to play again ?(y/n)").lower()
    if response == "y" or response == "yes":
        return True
    else:
        return False

# Everything starts from here I mean everything!
new_game()

# According to this while loop, if play_again function returns true,user
# will play for one more round otherwise will be done!
while play_again():
    new_game()
# Last thing that user will see:)!
print("We will miss you. Please back again ;)")
