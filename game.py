import random

word_bank = ["word1", "word2", "word3"]
word = random.choice(word_bank)
lives = 6
user_input = null


#9, 10, 11
if lives == 0 or user_input == word:
    if lives == 0:
        print ("Out of Lives! Game Over!")
    if user_input == word:
        print ("You win!")   
    response = input ("Play Again? (yes/no)")
    while True:
        if response != "yes" and response != "no":
            response = input ("Invalid Input. Play Again? (yes/no)")
        if response == "yes":
            break 
        if response == "no":
            raise SystemExit()

        


        

