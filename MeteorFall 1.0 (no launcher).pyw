#Imports
from tkinter import *
from time import sleep, time
from random import randint
from math import sqrt
HEIGHT = 900
WIDTH = 800
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
harry_spd = 10
METEOR_CHANCE = 20
TIME_LIMIT = 0
end = time() + TIME_LIMIT

#Make Tk()
win1 = Tk()
win1.title('MeteorFall 1.0')
c = Canvas(win1, width=WIDTH, height=HEIGHT, bg='lightblue')
c.pack()

#Make Harry
HARRY_R = 25
face = c.create_rectangle(0, 0, 50, 50, fill='gold', outline='black')
eyeb1 = c.create_rectangle(5, 15, 20, 30, fill='white')
eyeb2 = c.create_rectangle(30, 15, 45, 30, fill='white')
eye1 = c.create_rectangle(9, 19, 16, 26, fill='black')
eye2 = c.create_rectangle(34, 19, 41, 26, fill='black')
hair = c.create_rectangle(0, 0, 50, 10, fill='brown')
mouth = c.create_rectangle(9, 40, 41, 42, fill='black')
c.move(face, MID_X, MID_Y)
c.move(eyeb1, MID_X, MID_Y)
c.move(eyeb2, MID_X, MID_Y)
c.move(eye1, MID_X, MID_Y)
c.move(eye2, MID_X, MID_Y)
c.move(hair, MID_X, MID_Y)
c.move(mouth, MID_X, MID_Y)

#Make stone
STONE_R = 500
stone = c.create_oval(0, 0, 1000, 1000, fill='gray', outline='darkgray')
c.move(stone, MID_X - 100, MID_Y + 50)
c.move(stone, -400, 0)

#Move Harry
def move_left(event):
    c.move(face, -harry_spd, 0)
    c.move(eyeb1, -harry_spd, 0)
    c.move(eyeb2, -harry_spd, 0)
    c.move(eye1, -harry_spd, 0)
    c.move(eye2, -harry_spd, 0)
    c.move(hair, -harry_spd, 0)
    c.move(mouth, -harry_spd, 0)
def move_right(event):
    c.move(face, harry_spd, 0)
    c.move(eyeb1, harry_spd, 0)
    c.move(eyeb2, harry_spd, 0)
    c.move(eye1, harry_spd, 0)
    c.move(eye2, harry_spd, 0)
    c.move(hair, harry_spd, 0)
    c.move(mouth, harry_spd, 0)
c.bind_all('<KeyPress-Left>', move_left)
c.bind_all('<KeyPress-Right>', move_right)

#Meteor ID
meteor_id = list()
meteor_r = list()
meteor_spd = list()
MIN_MET_R = 10
MAX_MET_R = 20
MET_SPD = 2
GAP = 100

#Create meteor
def create_meteor():
    x = randint(0, WIDTH)
    y = GAP - HEIGHT
    r = randint(MIN_MET_R, MAX_MET_R)
    id1 = c.create_rectangle(x - r, y - r, x + r, y + r, fill='red', outline='black')
    meteor_id.append(id1)
    meteor_r.append(r)
    meteor_spd.append(MET_SPD)
def move_meteor():
    for i in range(len(meteor_id)):
        c.move(meteor_id[i], 0, meteor_spd[i])

#Meteor delete
def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x, y
def del_meteor(i):
    del meteor_r[i]
    del meteor_spd[i]
    c.delete(meteor_id[i])
    del meteor_id[i]
def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
def collision():
    points = 0
    for meteor in range(len(meteor_id)-1, -1, -1):
        if distance(stone, meteor_id[meteor]) < (STONE_R + meteor_r[meteor]):
            points += (meteor_r[meteor] + meteor_spd[meteor])
            del_meteor(meteor)
            return points

#Game over!
def game_over():
    text_gameover = c.create_text(MID_X, MID_Y, text='GAME OVER', fill='brown', font=('AcmeFont', 100,))
    c.itemconfig(face, state=HIDDEN)
    c.itemconfig(eyeb1, state=HIDDEN)
    c.itemconfig(eyeb2, state=HIDDEN)
    c.itemconfig(eye1, state=HIDDEN)
    c.itemconfig(eye2, state=HIDDEN)
    c.itemconfig(hair, state=HIDDEN)
    c.itemconfig(mouth, state=HIDDEN)
    text_end = c.create_text(MID_X, MID_Y + 100, text='(: Goed gedaan! Jij bent écht goed! ;)', font=('AcmeFont', 30))
    text_copyright = c.create_text(MID_X, HEIGHT - 200, text='© NertGames - NertPower', fill='white', font=('Agency FB', 30))

#Outch!
def collision2():
    for meteor in range(len(meteor_id)-1, -1, -1):
        if distance(face, meteor_id[meteor]) < (HARRY_R + meteor_r[meteor]):
            del_meteor(meteor)
            game_over()

#Time
text_time1 = c.create_text(50, 30, text='TIME', fill='brown', font=('BN Machine', 13))
text_time2 = c.create_text(50, 50, fill='darkblue', font=('BN Machine', 20))
def show_time(time_left):
    c.itemconfig(text_time2, text=str(time_left))

#MAIN GAME LOOP
while True:
    if randint(1, METEOR_CHANCE) == 1:
        create_meteor()
    move_meteor()
    collision2()
    collision()
    show_time(int(time() - end))
    win1.update()
    sleep(0.01)
