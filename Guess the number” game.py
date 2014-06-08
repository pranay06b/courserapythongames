#Mini-project description — “Guess the number” game One of the simplest two-player games is “Guess the number”. The first player thinks of a secret number in #some known range while the second player attempts guess the number. After each guess, the first player answers either “Higher”, “Lower” or “Correct!” #depending on whether the secret number is higher, loweor equal to the guess.
import simplegui
import random
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

num_range=100
num=0
count = 7
# initialize global variables used in your code



# helper function to start and restart the game
def new_game():
    global num_range
    global num,count
    print 'New game'
    count=7
    print 'Range is from 0 to '+str(num_range)
    print 'Total number of guesses left are :'+str(count)
    num=random.randrange(0,num_range)
    
    

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    if num_range!=100:
        num_range=100
        count=7
        new_game()
        

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    if num_range!=1000:
        num_range=1000
        count=10
        new_game()
        
    # remove this when you add your code
    
def input_guess(guess):
    # main game logic goes here	
    global num_range,num,count
    count=count-1
    if(count>0):
        g=int(guess)
        if g<num:
            print 'Higher'
        elif g>num:
            print 'Lower'
        elif g==num:
            print 'correct'
            new_game()
        print 'Guess was '+str(guess)
        print "Remaining guesses are "+str(count)       
        
    else:        	
        print 'Lost!'
        new_game()
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200, 300)
# register event handlers for control elements
frame.add_button('0 to 100', range100)
frame.add_button('0 to 1000', range1000)
frame.add_input('Input the Number', input_guess, 50)
# call new_game and start frame
new_game()
frame.start()


