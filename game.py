    import random
    
    #1, 2
    word_bank = ['fruits', 'pineapple', 'smoothie', 'jambajuice', 'apples', 'strawberry', 'grapes', 'lemonade', 'bananas', 'oranges', 'peaches']
    secret_word = random.choice(word_bank)
    lives = 6
    user_input = null
    
    print("Let’s play hangman!")
    #5, 6
    while True:
        user_input = input("Guess a letter: ")
    
        if len(user_input) == 1 and user_input.isalpha():
            break
    
        print("Not a valid guess. Please enter a single letter.")
        #7, 8
if "_" not in display:
    break

if lives <= 0:
    print("Out of lives, game over!")
    break
    #9, 10, 11
    if lives == 0 or user_input == secret_word:
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
    
            
    
    
            
    
