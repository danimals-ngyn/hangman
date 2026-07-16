    import random
while True:  
    #1, 2
    word_bank = ['fruits', 'pineapple', 'smoothie', 'jambajuice', 'apples', 'strawberry', 'grapes', 'lemonade', 'bananas', 'oranges', 'peaches']
    secret_word = random.choice(word_bank)
    lives = 6
    user_input = None
    
    print("Let’s play hangman!")
    #3, 4
    display = ["_" for letter in secret_word]
    print(" ".join(display))
    print("Lives left:", lives)
    #5, 6
    while True:
        print(" ".join(display))
        print("Lives left:", lives)
        user_input = input("Guess a letter: ")
    
        if len(user_input) != 1 or not user_input.isalpha():
            continue
        if user_input in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == user_input:
                    display[i] = user_input

        else:
            lives-=1
            print("Letter not found!")
            
        #7, 8
        if "_" not in display:
            print("You win!")
            break
        
        if lives == 0 or user_input == secret_word:
            if lives == 0:
                print ("Out of lives! Game over!")
                break
            #9, 10, 11
            if user_input == secret_word:
                print ("You win!")
                break
    response = input ("Play Again? (yes/no)")
    while True:
             if response != "yes" and response != "no":
                  response = input ("Invalid Input. Play Again? (yes/no)")
             if response == "yes":
                            break 
             if response == "no":
                        raise SystemExit()                     
    
            
    
    
            
    
