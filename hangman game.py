import random

def get_word():
    words= [ 'Woodstock',
         'Gray',
         'Hello',
         'Gopher',
         'Spikepike',
         'green',
         'blue',
         'Willy',
         'Rex',
         'yes',
         'Roo',
         'Littlefoot',
         'Baagheera',
         'Remy',
         'good',
         'Kaa',
         'Rudolph',
         'Banzai',
         'Courage',
         'Nemo',
         'Nala',
         'other',
         'Sebastin',
         'lago',
         'head',
         'car',
         'Dory',
         'Pumbaa',
         'Garfield',
         'Manny',
         'bubble',
         'ball',
         'Flik',
         'Marty',
         'Gloria',
         'Donkey',         
         'Timon',         
         'Baloo',         
         'Thumper',         
         'Bambi',         
         'Goofy',         
         'Tom',
         'Sylvester',
         'Jerry',
         'Tiger']
    return random.choice(words).upper()

def Check(word,guesses,guess):
    guess=guess.upper()
    status=''
    i=0
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '*'
           
        if letter == guess:
            matches += 1
    if matches > 1:
        print ('yes! The word contains', matches, '"'+guess + '"' + 's')
    elif matches == 1:
        print ('Yes! The word containes the letter"'+ guess + '"')
    else:
        print('Sorry. the word does not cpontain the letter " '+ guess + '"')
    return status
    
def main():
    word = get_word()
    guesses=[]
    guessed = False
    print ('The word contains',len(word) ,'letters.')
    while not guessed:
        text= 'please enter one letter or whole word    '
        guess = input(text)
        guess = guess.upper()
        if(len(guesses)>=8):
            print("GAME OVER")
            break;
        if guess in guesses:
            print ('you already guessed"' + guess + '"')
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print('Sorry, thst is incorrect')
        elif len(guess) == 1:
            guesses.append(guess)
            result = Check(word,guesses,guess)
            if result == word:
                guessed = True
            else:
                print (result)
        else:
            print('invalid entry')
    
    print ('The word is', word + '! you took ',len(guesses),'tries.')
    
   

    
main()
    