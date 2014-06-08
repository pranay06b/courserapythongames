#Stopwatch: The Game"
import simplegui
import random
# template for "Stopwatch: The Game"

# define global variables

global test 
global time
global t,minute
time=0
t=0
minute=0
point=lose=0
#to check if timer is running

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def start():
    global check
    timer.start()
    check=0
    
    pass    
def stop():
    global point,lose,t,check
    timer.stop()
    if check==0:
        if t==0:
            point=point+1
        lose=lose+1    
        check=1
        print t
    pass    

def reset():
    global time,t,minute,point,lose
    point=lose=0
    time=t=minute=0
    pass    
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval


# define draw handler
def draw_handler(canvas):
        global time,t,minute,point,lose
        game=str(point)+"/"+str(lose) 
        canvas.draw_text(str(minute),(100,100), 40, 'White')
        canvas.draw_text(str(time),(150,100), 40, 'White')
        canvas.draw_text(str(t),(200,100), 40, 'White')
        canvas.draw_text(game,(260,20), 20, 'Green')               
def timer_handler():
    global time,t,minute
    i=0
    t=t+1
    t=(t%10)
    if(t==9):
        time=time+1
    if(time==60):      
        time=0
        minute=minute+1
    pass
# create frame
f = simplegui.create_frame('Timer', 300, 200)
# register event handlers


f.set_canvas_background('Black')
button1 = f.add_button('Start', start,75)
button2 = f.add_button('Stop', stop,75)
button3 = f.add_button('Reset', reset,75)
f.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)


# start frame

f.start()

# Please remember to review the grading rubric
