import turtle
import pygame

wn = turtle.Screen()
wn.title("Pong by @NoobDs Based @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#pontuação
pontuacao_1 = 0
pontuacao_2 = 0

#paleta 1
paleta_1 = turtle.Turtle()
paleta_1.speed(0)
paleta_1.shape("square")
paleta_1.color("white")
paleta_1.shapesize(stretch_wid=5, stretch_len = 1)
paleta_1.penup()
paleta_1.goto(-350, 0)

#paleta 2
paleta_2 = turtle.Turtle()
paleta_2.speed(0)
paleta_2.shape("square")
paleta_2.color("white")
paleta_2.shapesize(stretch_wid=5, stretch_len = 1)
paleta_2.penup()
paleta_2.goto(350, 0)

#bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 5
bola.dy = 5

#placar
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Player 1 : 0   Player 2: 0", align="center", font=("Arial", 24, "normal"))

#funções
def subir_paleta1():
    y = paleta_1.ycor()
    if y < 230:
        y += 40
    paleta_1.sety(y)

def descer_paleta1():
    y = paleta_1.ycor()
    if y > -230:
        y -= 40
        paleta_1.sety(y)
    else:
        paleta_1.sety(y)

#definindo botão
wn.listen()
wn.onkeypress(subir_paleta1, "w")
wn.onkeypress(descer_paleta1, "s")

def subir_paleta2():
    y = paleta_2.ycor()
    if y < 230:
        y += 40
        paleta_2.sety(y)
    else:
        paleta_2.sety(y)

def descer_paleta2():
    y = paleta_2.ycor()
    if y > -230:
        y -= 40
        paleta_2.sety(y)
    else:
        paleta_2.sety(y)

#definindo botão
wn.listen()
wn.onkeypress(subir_paleta2, "Up")
wn.onkeypress(descer_paleta2, "Down")

#while maingame loop
while True:
    pygame.time.Clock().tick(50)
    wn.update()

    #mover bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #checar borda
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
    
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
    
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontuacao_1 += 1
        placar.clear()
        placar.write("Player 1 : {}   Player 2: {}".format(pontuacao_1, pontuacao_2), align="center", font=("Arial", 24, "normal"))
    
    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontuacao_2 += 1
        placar.clear()
        placar.write("Player 1 : {}   Player 2: {}".format(pontuacao_1, pontuacao_2), align="center", font=("Arial", 24, "normal"))

    #colisão da paleta e da bola
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < paleta_2.ycor() + 50 and bola.ycor() > paleta_2.ycor() - 50):
        bola.setx(340)
        bola.dx *= -1
               
        bola.color("red")
    
    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < paleta_1.ycor() + 50 and bola.ycor() > paleta_1.ycor() - 50):
        bola.setx(-340)
        bola.dx *= -1
        
        bola.color("blue")