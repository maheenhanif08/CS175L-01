#Maheen Hanif Ghaffar
#CS 175L
#Average and Grade Assignment

def main():
    s1, s2, s3, s4, s5 = input_scores()
    calc_average(s1, s2, s3, s4, s5)

def input_scores():
    score_1 = float(input("Enter score 1: "))
    score_2 = float(input("Enter score 2: "))
    score_3 = float(input("Enter score 3: "))
    score_4 = float(input("Enter score 4: "))
    score_5 = float(input("Enter score 5: "))    
    return score_1, score_2, score_3, score_4, score_5

def determine_grade(score):
    if score < 60:
        return 'F'
        
    elif score < 70:
        return 'D'

    elif score < 80:
        return 'C'

    elif score < 90:
        return 'B'

    else:
        return 'A'

def calc_average(s1, s2, s3, s4, s5):
    average = (s1 + s2 + s3 + s4 + s5) / 5
    print("")
    print("Score            Numeric Grade           Letter Grade")
    print("----------------------------------------------------------")
    print("Score 1:",  "              ", s1,"                             ", determine_grade(s1))
    print("Score 2:",  "              ", s2, "                             ", determine_grade(s2))
    print("Score 3:",  "              ", s3, "                             ", determine_grade(s3))
    print("Score 4:", "              ",  s4, "                             ", determine_grade(s4))
    print("Score 5:",  "              ", s5, "                           ", determine_grade(s5))
    print("Average score:",  "   ",  average, "                             ", determine_grade(average))

main()

print("")

response = input("Enter 'yes' if you would like to do another calculation: ").lower()

while response == "yes":
    print("")
    main()
    print("")
    response = input("Enter 'yes' if you would like to do another calculation: ").lower()




