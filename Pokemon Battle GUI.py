from tkinter import *
import random


player=""
health1="100" #opponent health
health2="100" #your health


def greetprocess():
   global player
   start["text"]="Hello " + name.get() +  " a "+ battlepoke + " has appeared and wants to battle"
   pick["text"]=name.get()+ " pick your pokemon!!!"
   ur_name["text"]=player

def choice1():
   global player
   print(name," chooses", poke1,"!")
   player=poke1
def choice2():
   global player
   print(name," chooses",  poke2,"!")
   player=poke2
def choice3():
   global player
   print(name," chooses", poke3,"!")
   player=poke3

#Setting battle
def war():
    global health1
    global health2
    dmg1=random.randrange(10,60)
    dmg2=random.randrange(10,60)
    ihealth1=int(health1)
    ihealth1=ihealth1-dmg1
    op_health["text"]=health1
    ihealth2=int(health2)
    ihealth2=ihealth2-dmg2
    ur_health["text"]=health2
    if ihealth1 <=0 or ihealth2 <=0:
        op_health["text"]="Over"
        ur_health["text"]="Game"
    health1=str(ihealth1)
    health2=str(ihealth2)
    
    
        
print("Gabriel Gordon, Pokemon GUI")

pokemonfile=open("Pokemon.txt","r")
pmoves=open("Pokemonmoves.txt","r")

#import pokemon
poke=[]
for line in pokemonfile:
    poke.append(line.rstrip())
#import moves
moves=[]
for line in pmoves:
    moves.append(line.rstrip())

#Picking random pokemon (opponent)
position=random.randrange(0,len(poke))
battlepoke=poke[position]
if battlepoke == " ":
    position=random.randrange(0,len(poke))
    battlepoke=poke[position]

#GUI

window=Tk()
window.title("Pokemon Battle")

frame1=Frame(window)
frame1.pack()

#name
aname=Label(frame1,text="Hello, What can i call you?")
name=StringVar()
bname=Entry(frame1,textvariable=name)
aname.grid(row=1,column=1)
bname.grid(row=1,column=2)

#prints
greeting="Hello " + name.get()+  " a "+ battlepoke + " has appeared and wants to battle"
start=Label(frame1,text=greeting)
greet=Button(frame1, text="Greet" ,command=greetprocess)
ent=Label(frame1,text="Entering battle...")
start.grid(row=2,column=1)
greet.grid(row=2, column=2)
ent.grid(row=3,column=1)

print(name.get()) 

for i in range(0,3,1):
    pos=random.randrange(0,len(poke))
    if i ==0:
        poke1=poke[pos]
    if i ==1:
        poke2=poke[pos]
    if i ==2:
        poke3=poke[pos]

        
#Pick Pokemon
pick=Label(frame1,text=" ")
choose1=Button(frame1,text=poke1,command=choice1)
choose2=Button(frame1,text=poke2,command=choice2)
choose3=Button(frame1,text=poke3,command=choice3)
pick.grid(row=4,column=1)
choose1.grid(row=4,column=2)
choose2.grid(row=5,column=2)
choose3.grid(row=6,column=2)

#Name and health

ur_name=Label(frame1,text=player)
ur_health=Label(frame1,text=health2)
ur_name.grid(row=14,column=1)
ur_health.grid(row=15,column=1)
    
op_name=Label(frame1,text=battlepoke)
op_health=Label(frame1,text=health1)
op_name.grid(row=14,column=2)
op_health.grid(row=15,column=2)

#your moves
bmove=[]
for i in range(0,4,1):
      mpos=random.randrange(0,len(moves))
      battlemoves=moves[mpos]
      bmove.append(battlemoves)

ymov=Label(frame1,text="Here are your moves:")
m1=Button(frame1,text=bmove[0],command=war)
m2=Button(frame1,text=bmove[1],command=war)
m3=Button(frame1,text=bmove[2],command=war)
m4=Button(frame1,text=bmove[3],command=war)
ymov.grid(row=8,column=1)
m1.grid(row=9,column=1)
m2.grid(row=10,column=1)
m3.grid(row=11,column=1)
m4.grid(row=12,column=1)

#Opponents Moves
opmove=[]
for i in range(0,4,1):
    opppos=random.randrange(0,len(moves))
    oppmoves=moves[opppos]
    opmove.append(oppmoves)

hmov=Label(frame1,text="Here are your opponents moves")
h1=Button(frame1,text=opmove[0])
h2=Button(frame1,text=opmove[1])
h3=Button(frame1,text=opmove[2])
h4=Button(frame1,text=opmove[3])
hmov.grid(row=8,column=2)
h1.grid(row=9,column=2)
h2.grid(row=10,column=2)
h3.grid(row=11,column=2)
h4.grid(row=12,column=2)





             
