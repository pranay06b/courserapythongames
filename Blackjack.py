#Blackjack

global flag,msg,msg1,score
score=0
flag=0
global stand
msg1=" "
msg=" "
myflag=0
import simplegui
import random
# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# define globals for cards
SUITS1 = ['C', 'S', 'H', 'D']
RANKS1 = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
            #print "Invalid card: ", suit, rank
        else:
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)

##########HAnd
class Hand:
    
    #mysuit=[]
    #mysuit1=[]
    #myrank=[]
    #myrank1=[]
    def __init__(self,i):
        self.i=i
        self.mysuit=[]
        self.myrank=[]
        
        # create Hand object

    def __str__(self):
    #    if self.i==0:
     #       self.i=self.i+1
      #      return "Hand contains"
       #     
        #else:
         #   print "Hand has"
          #  for ii in range(0,len(Hand.mysuit),1):
           #     print Hand.mysuit[ii],Hand.myrank[ii]
            #return ""
    # return a string representation of a hand
        return ' '

    def add_card(self, card):
        if (card.suit in SUITS) and (card.rank in RANKS):
            self.mysuit.append(card.suit)
            self.myrank.append(card.rank)
            print self.mysuit
            print self.myrank
          #  print self.suit,self.rank,"0"
        else:
            print "Invalid card: ", suit, rank
            
                    


    def get_value(self):
        value=0
        for ii in self.myrank:
            value=value+VALUES[ii]
        return value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
            # compute the value of the hand, see Blackjack video
    def over(self):
        for ii in range(len(self.mysuit),0,-1):
            self.mysuit.pop()
            self.myrank.pop()
            
            
    def draw(self, canvas, pos):
        if self.i==0:
            if len(self.mysuit)>0 and len(self.myrank)>0:
                #print "r",self.myrank[0],self.mysuit[0]
                card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS1.index(self.myrank[0]), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS1.index(self.mysuit[0]))
                canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                pos[0]=pos[0]+80
                card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS1.index(self.myrank[1]), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS1.index(self.mysuit[1]))
                
                canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                if len(self.mysuit)>=3:
                    pos[0]=pos[0]+80
                    card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS1.index(self.myrank[2]), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS1.index(self.mysuit[2]))
                
                    canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                if len(self.mysuit)>=4:
                    #print self.mysuit[3]
                    pos[0]=pos[0]+80
                    card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS1.index(self.myrank[3]), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS1.index(self.mysuit[3]))
                
                    canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                if len(self.mysuit)>=5:
                    pos[0]=pos[0]+80
                    card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS1.index(self.myrank[4]), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS1.index(self.mysuit[4]))
                    canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                if len(self.mysuit)>=6:
                    pos[0]=pos[0]+80
                    card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS1.index(self.myrank[5]), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS1.index(self.mysuit[5]))
                    canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

        elif self.i==1:    
            pos[1]=pos[1]-150
            if len(self.mysuit)>0 and len(self.myrank)>0:
                #print "r",self.myrank[0],self.mysuit[0]
                card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS1.index(self.myrank[0]), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS1.index(self.mysuit[0]))
                canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                if flag==1:
                    pos[0]=pos[0]+80
                    card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS1.index(self.myrank[1]), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS1.index(self.mysuit[1]))
                    
                    canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                    if len(self.mysuit)>=3:
                        pos[0]=pos[0]+80
                        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS1.index(self.myrank[2]), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS1.index(self.mysuit[2]))
                    
                        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                    if len(self.mysuit)>=4:
                        #print self.mysuit[3]
                        pos[0]=pos[0]+80
                        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS1.index(self.myrank[3]), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS1.index(self.mysuit[3]))
                    
                        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                    if len(self.mysuit)>=5:
                        pos[0]=pos[0]+80
                        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS1.index(self.myrank[4]), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS1.index(self.mysuit[4]))
                        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                    if len(self.mysuit)>=6:
                        pos[0]=pos[0]+80
                        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS1.index(self.myrank[5]), 
                            CARD_CENTER[1] + CARD_SIZE[1] * SUITS1.index(self.mysuit[5]))
                        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

        # draw a hand on the canvas, use the draw method for cards
 

#####################################################
# Student should insert code for Deck class here
class Deck:
    count=0
    c=dict()
    
    #global SUITS,RANKS
    def __init__(self):
        pass
    # create a Deck object

    def shuffle(self):
        random.shuffle(SUITS)
        random.shuffle(RANKS)
        for ii in range(0,len(SUITS),1):
            for jj in range(0,len(RANKS),1):
                Deck.c[Deck.count]=Card(SUITS[ii],RANKS[jj])
                Deck.count=Deck.count+1
        print "d",Deck.c[0]
        #print SUITS
        #print RANKS
        # shuffle the deck 
        
            # use random.shuffle()

    def deal_card(self):
        pass	# deal a card object from the deck
    
    def __str__(self):
        return " "
        pass	# return a string representing the deck
        


#define event handlers for buttons
d=Deck()
player=Hand(0) 
pc=Hand(1)
  
def deal():
    global flag
    flag=0
    #print 'h'
    d.shuffle()
    player.over()
    pc.over()
    player.add_card(d.c[random.randint(0, 51)])
    player.add_card(d.c[random.randint(0, 51)])
    pc.add_card(d.c[random.randint(0, 51)])
    pc.add_card(d.c[random.randint(0, 51)])        
def hit():
    global msg,msg1,st,flag,score
        #print type(d)
    d.shuffle()
    #player=Hand() 
    player.add_card(d.c[random.randint(0, 51)])
    if player.get_value()>21:
        msg1= "Player Busted"
        msg="Dealer wins"
        score=score-1
        st=msg+msg1
        flag=1
#        player.over()
    if pc.get_value()<17:
        pc.add_card(d.c[random.randint(0, 51)])
    if pc.get_value()>21:
        msg1= "Dealer busted"
        msg="Player wins"
        st=msg+"and"+msg1
        score=score+1
        flag=1
    print st
 #       pc.over()
       
# Test code
def stand():
    global msg,msg1,flag,score,st
    print pc.get_value()
    if pc.get_value()<17:
        pc.add_card(d.c[random.randint(0, 51)])
    if pc.get_value()>21:
        msg1 ="Pc busted"
        msg="Player wins"
        score=score+1
        pass
    if pc.get_value()<player.get_value():        
        msg="Player wins"
        score=score+1
        flag=1
    else:
        msg="Dealer wins"
        flag=1
    st=msg
#DRaw fns    
st="Stand or Hit?"
def drawp(canvas):
    global st,flag
    # test to make sure that card.draw works, replace with your code below
    #card = Card("S", "A")
    canvas.draw_text(st, (400, 280), 22, 'White', 'serif')
    canvas.draw_text('BlackJack', (80, 50), 32, 'White', 'serif')
    canvas.draw_text('Player', (300, 280), 32, 'White', 'serif')
    canvas.draw_text("Score:", (500, 40), 22, 'White', 'serif')
    canvas.draw_text(str(score), (580, 40), 22, 'White', 'serif')
    if flag==1:
        canvas.draw_text("New Deal?", (400, 100), 22, 'White', 'serif')
    else:
        st="Stand or Hit?"        
    canvas.draw_text('Dealer', (300, 140), 32, 'White', 'serif')
    player.draw(canvas, [200, 300])
    pc.draw(canvas, [200, 300])
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 800, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
# get things rolling
deal()
frame.set_draw_handler(drawp)
frame.start()