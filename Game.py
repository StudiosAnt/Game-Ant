import turtle
import time
import os
import random

punkty = 0

pozycja_lizaka_x = random.randint(0, 2000)
pozycja_lizaka_y = random.randint(0, 984)

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.title("Game Ant")
screen.bgcolor("black")


# Pierwszy napis
t = turtle.Turtle()
t.color("blue")
t.penup()
t.goto(0, 0)
t.write("Studios Mrówka", align="center", font=("Arial", 60, "normal"))

time.sleep(2)
t.clear()
t.hideturtle()

tekst_punkty = turtle.Turtle()
tekst_punkty.hideturtle()
tekst_punkty.penup()
tekst_punkty.goto(-390, 270)  # miejsce w lewym górnym rogu

folder = os.path.dirname(os.path.abspath(__file__))
gif_path = os.path.join(folder, "postac.gif")# Desktop/Game/postac.gif

ffolder = os.path.dirname(os.path.abspath(__file__))  # folder, w którym jest Game.py
plik = os.path.join(ffolder, "punkt.wav")

screen.register_shape(gif_path)

screen.bgcolor("blue")

# Drugi turtle (sterowany)
t2 = turtle.Turtle()
t2.penup()
t2.shape(gif_path)
t2.penup()

lizak = turtle.Turtle()
lizak.shape("circle")
lizak.color("red")
lizak.penup()            # nie rysuje linii

# zmniejszamy rozmiar lizaka
lizak.shapesize(0.5, 0.5)  # teraz lizak jest mniejszy

# margines od krawędzi ekranu
MARGINES = 20

# funkcja teleportująca lizaka losowo
def teleportuj():
    width = screen.window_width()
    height = screen.window_height()
    
    x = random.randint(-width//2 + MARGINES, width//2 - MARGINES)
    y = random.randint(-height//2 + MARGINES, height//2 - MARGINES)
    
    lizak.goto(x, y)
    
teleportuj()

def sprawdz_dotyk():
    global punkty
    MARGINES_KOLIZJI = 10  # jak blisko ma być dotyk

    if abs(t2.xcor() - lizak.xcor()) < MARGINES_KOLIZJI and abs(t2.ycor() - lizak.ycor()) < MARGINES_KOLIZJI:
        punkty += 1
        print("Punkt! Masz teraz:", punkty)
        teleportuj()
        pokaz_punkty()    # aktualizujemy wyświetlanie
        
def pokaz_punkty():
    tekst_punkty.clear()
    tekst_punkty.write(f"Punkty: {punkty}", font=("Arial", 24, "normal"))        

# Funkcje ruchu
def gora():
    t2.setheading(90)
    t2.forward(20)
    sprawdz_dotyk()  # sprawdzamy po ruchu

def dol():
    t2.setheading(270)
    t2.forward(20)
    sprawdz_dotyk()

def lewo():
    t2.setheading(180)
    t2.forward(20)
    sprawdz_dotyk()

def prawo():
    t2.setheading(0)
    t2.forward(20)
    sprawdz_dotyk()

# Nasłuchiwanie klawiszy
screen.listen()
screen.onkey(gora, "Up")
screen.onkey(dol, "Down")
screen.onkey(lewo, "Left")
screen.onkey(prawo, "Right")

# Uruchomienie pętli
turtle.mainloop()