# implementation of card game - Memory
import random
import simplegui
global t,p7
p7=0
turns=0
qq=0
t=0
l1=[]
l2=[]
g=[]
for n in range(0,8,1):
    l1.append(qq)
    l2.append(qq)
    qq=qq+1
l3=l1+l2
random.shuffle(l3)
#print l3
num={}
uu=0
for tt in l3:
    num[uu]=l3[uu]
    uu=uu+1
print num    
points={0:[(0,0),(50,0),(50,100), (0, 100)] }    
for i in range(1,17,1):
    points[i]=[(0,0),(0,0),(0,0),(0,0)]
c=0
for i in range(1,16,1):
    points[i][0]=(points[i-1][0][0]+50,0)
    points[i][1]=(points[i-1][1][0]+50,0)
    points[i][2]=(points[i-1][2][0]+50,100)
    points[i][3]=(points[i-1][3][0]+50,100)
#print points 
f=[]


def mouseclick(pos):
    global t
    t=t+1
    print "t",t
    global state,flag,p7
    for key, p in points.items():
        #print key,
        if pos[0]>p[0][0] and pos[0]<p[1][0]:
            #print pos,key
            break
    if key==16:
        key=2
    #print flag
    #print f.count(key),"C"
   # if f.count(key)==0:
    if len(f)==2:
        f.pop(1)
        f.pop(0)
    if f.count(key)==0:       
        f.append(key)
    if len(f)==2:
        if num[f[0]]==num[f[1]]:
            g.append(f[0])
            g.append(f[1])
    #print f
    #print num[f[p7]],"i" 
    #p7=p7+1    
    label1.set_text("Turns:"+str(t))

    print f            
    #print turns,"t"
    #print f            
    #print num[key]
    
def new_game():
    global t
    t=0
    i=0
    uu=0
    while len(g) > 0:
        g.pop()
    while len(f) > 0:
        f.pop()
    label1.set_text("Turns:"+str(t)) 
    random.shuffle(l3)
    while len(num)>0:
        num.pop(i)
        i=i+1
    for tt in l3:
        num[uu]=l3[uu]
        uu=uu+1
    pass 
text={0:(10,40)}
for i in range(1,17,1):
    text[i]=(text[i-1][0]+50,text[i-1][1])
   # print text[i]
print text
def draw(canvas):
    for i in range(0,16,1):
        canvas.draw_text(str(num[i]), text[i], 48, 'White')
    
    for i in range(0,16,1):
        
        if i in f or i in g:
            pass
        else:
            canvas.draw_polygon(points[i], 5,'Silver', 'Gray')
    

        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label1 = frame.add_label("Turns:"+str(t))



# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
        
    