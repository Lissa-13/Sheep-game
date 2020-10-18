from turtle import *                
from random import randint
                                                       
w=650
h=650
turn=0
pocitadlozradla = 50

#pohyb
def klavesaVlevo():                           
    global turn 
    turn=1 

def klavesaVpravo():
    global turn
    turn=2 

#obrazovka
s = Screen()                        
s.setup(w ,h)
s.bgpic ("grafika/plocha.gif")
s.title ("Hungry sheep")
s.register_shape ("grafika/poo.gif", shape=None)
s.register_shape ("grafika/ovce.gif", shape=None)
s.register_shape ("grafika/ovceotoc.gif", shape=None)
s.register_shape ("grafika/ovcepr.gif", shape=None)
s.register_shape ("grafika/ovcele.gif", shape=None)
s.register_shape ("grafika/jabko.gif", shape=None)

#ovce
ovce = Turtle()   
ovce.speed (1)
ovce.penup()
ovce.screen.onkey(klavesaVlevo, "Left")
ovce.screen.onkey(klavesaVpravo, "Right")
ovce.screen.listen()
ovce.shape("grafika/ovce.gif")

#žrádlo
jabko = Turtle()                        
jabko.penup()
jabko.speed(0)
jabko.goto (80,80)
jabko.shape("grafika/jabko.gif") 

#zelva na hlášky
zprava=Turtle()                          
zprava.color ("red")
zprava.hideturtle()

bobky = []

bezi = True

while bezi:
    
    if turn==1:
        ovce.left(90)
        turn=0
    if turn==2:
        ovce.right(90)
        turn=0
    ovce.forward (10) 
    
    #otáčení ovce podle směru
    if ovce.heading ()== 0:
        ovce.shape("grafika/ovcepr.gif")
    elif ovce.heading ()== 90:
        ovce.shape("grafika/ovce.gif")
    elif ovce.heading ()== 180:
        ovce.shape("grafika/ovcele.gif")
    elif ovce.heading ()== 270:
        ovce.shape("grafika/ovceotoc.gif")

    pocitadlozradla = pocitadlozradla -1
    if pocitadlozradla == 0:
        x = randint (-15, 15)*10
        y = randint (-15, 15)*10
        jabko.goto (x,y)
        pocitadlozradla =50

    if ovce.distance (jabko) < 15:
        x = randint (-15, 15)*10
        y = randint (-15, 15)*10
        jabko.goto (x,y)
        pocitadlozradla =50

        bobek = Turtle()
        bobek.penup()
        bobek.speed(0)
        bobek.goto(ovce.xcor(),ovce.ycor())
        bobek.shape("grafika/poo.gif")
        bobek.speed(1)

        bobky.append (bobek)

        if ovce.heading() == 0:
            bobek.goto(ovce.xcor()-20,ovce.ycor())
        elif ovce.heading() == 90:
            bobek.goto(ovce.xcor(),ovce.ycor()-20)
        elif ovce.heading() == 180:
            bobek.goto(ovce.xcor()+20,ovce.ycor())
        elif ovce.heading ()== 270:
            bobek.goto(ovce.xcor(),ovce.ycor()+20)

        body = len(bobky)
        print ("počet bodů", body)
        if body == 5:
            zprava.write ("VICTORY", font =("Algerian",50), align = ("center"))
            jabko.hideturtle()
            bezi = False 
       
    for bobek in bobky:
        if ovce.distance(bobek) < 15: 
            zprava.write ("OH SHIT!", font =("Algerian",50), align = ("center"))
            bezi = False

    if ovce.xcor()>230 or ovce.xcor()<-230 or ovce.ycor()>230 or ovce.ycor()<-230:
        zprava.write ("GAME OVER", font =("Algerian",50), align = ("center"))
        bezi = False 

exitonclick()