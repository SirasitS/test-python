coursework = 'English'
score_theory = 53
score_practical = 35

if (coursework=='Science' or coursework == 'science'):
    if (score_theory > 50):
        print("Please check the input score for 'Science: Theory'.")
    elif (score_practical > 50):
        print("Please check the input score for 'Science: Practical'.")
    else:
        print('Score validated for Science. Your total is:', score_theory + score_practical)