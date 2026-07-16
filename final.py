import random

word_bank = ['fruits', 'pineapple', 'smoothie', 'jambajuice', 'apples', 'strawberry', 'grapes', 'lemonade', 'bananas', 'oranges', 'peaches'] #intializes usable wordbank
secret_word = random.choice(word_bank) #chooses random word
lives = 6 #default lives is 6
valid = False #boolean to check if guess results in success or loss
underscores = "" #intializes underscores as empty 

for letter in secret_word: #sets up underscores
    underscores = underscores + "_"
    if letter != secret_word[-1]:
        underscores = underscores + " " #adds space between underscores but not after the last one


print("\nLet’s play hangman!") #introduction prompt
print("Guess all the letters one at a time of the secret word to win! You have six lives, and you lose one when your guessed letter is not in the word.") #introduction prompt

while True: 
    print()
    print (underscores) #print progress each time 
    print ("Lives: " + str(lives)) #lives

    guess = input("Guess?\n") #asks for user input
    

    if len(guess) == 1 and guess.isalpha: #checks input validaity  
        if guess.lower() in underscores:
            print ("\nYou already guesssed " + guess.lower() + "!")
        else:
            for letter in secret_word: #goes through each character of the secret word and checks the guess against the character
                    if guess.lower() == letter: #lowercases the letter to account for both capital and lowercase inputs since case sensitive inputs are annoying
                        underscores = underscores[:(secret_word.index(letter))*2] + letter + underscores[(secret_word.index(letter)*2)+1:] #splices the underscores based on the position of the letter in the secret word and replaces underscore with letter
                        secret_word = secret_word[:secret_word.index(letter)] + "`" + secret_word[secret_word.index(letter)+1:] #changes the corresponding letter in the secret word to a "`" because secret_word.index(letter) only looks for the first instance of that letter in the string, ignoring words that have multiple instances of the same letter, and so replacing it allows consideration of other instances of the ltter in the for loop. using "'" because no one uses it and its not a valid input anyway.
                        valid = True #if an instance of the gussed letter is found in the secret word, the guess is valid and no life is lost
            if valid == False and guess.lower() not in underscores: #if an instance is not found after going through the whole word, life is lost.
                print ("\nLetter Not Found!")
                lives -=1
            valid = False #resets to default as false
    else:
        print("\nNot a valid guess. Please enter a single letter.") #for when input is not a valid input.


    if lives <= 0 or "_" not in underscores: #checks for winning/losing/endgame event after each guess (when lives are gone or no more underscores)
        if lives <= 0:
            print ("\nOut of Lives! Game Over!")
        if "_" not in underscores:
            print ("\nYou win!")   
        response = input ("Play Again? (yes/no)") #in either event (winning or losing), play again is prompted
        while True:
            if response != "yes" and response != "no":
                response = input ("Invalid Input. Play Again? (yes/no)") #checks input is valid. 
            if response == "yes":
                lives = 6 #resets lives and the loop comes again. 
                secret_word = random.choice(word_bank) #chooses random word again
                underscores = "" #intializes underscores as empty 
                for letter in secret_word: #sets up underscores
                    underscores = underscores + "_"
                    if letter != secret_word[-1]:
                        underscores = underscores + " " #adds space between underscores but not after the last one
                print("\nLet’s play hangman!") #introduction prompt
                break 
            if response == "no":    
                raise SystemExit() #execute terminal if no
    
            
    
    
            
    
