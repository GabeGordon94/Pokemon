print("Gabriel Gordon, Pokemon")
'''
#GUI
from tkinter import *
window=Tk()
window.title("Pokemon Battle")

frame1=Frame(window)
frame1.pack()

name=Label(frame1,text="Hello, What can i call you?")
aname=StringVar()
bname=Entry(frame1,textvariable=aname)
name.grid(row=1,column=1)
bname.grid(row=1,column=2)
'''


pokemonfile=open("Pokemon.txt","r")
pmoves=open("Pokemonmoves.txt","r")

import random
#import pokemon
poke=[]
for line in pokemonfile:
    poke.append(line.rstrip())
#import moves
moves=[]
for line in pmoves:
    moves.append(line.rstrip())
    
print()
print("Hello, what can i call you?")
name=input()
#Picking random pokemon (opponent)
position=random.randrange(0,len(poke))
battlepoke=poke[position]
if battlepoke == " ":
    position=random.randrange(0,len(poke))
    battlepoke=poke[position]

print("Hello", name,"! A", battlepoke, "has appeared and wants to battle!")
print("Entering battle...")
print()
print(name, "pick your pokemon!!!")
#Giving option for 3 pokemon to choose
for i in range(0,3,1):
    pos=random.randrange(0,len(poke))
    if i ==0:
        poke1=poke[pos]
    if i ==1:
        poke2=poke[pos]
    if i ==2:
        poke3=poke[pos]
print(poke1,",", poke2,",",poke3)
choice=input()
print()
#check if chose real pokemon
if choice == poke1:
    print(name," chooses", poke1,"!")
    player=poke1
elif choice == poke2:
    print(name," chooses",  poke2,"!")
    player=poke2
elif choice == poke3:
    print(name," chooses", poke3,"!")
    player=poke3
else:
    print("Error, Start Program Again")
print()

#Display moves for your pokemon
print(name," here are moves for", player)
bmove=[]
for i in range(1,5,1):
      mpos=random.randrange(0,len(moves))
      battlemoves=moves[mpos]
      bmove.append(battlemoves)
      print(i,battlemoves)
      
#Display moves for opponent pokemon
print()
print(battlepoke,"has these moves")
opmove=[]
for i in range(0,4,1):
    opppos=random.randrange(0,len(moves))
    oppmoves=moves[opppos]
    opmove.append(oppmoves)
    print(oppmoves)
print()
health1=100 #battlepoke
health2=100 #player
#Battle Sequence 
while health1>0 or health2>0:
    print("Choose your attack number")
    attack=int(input())
    attack=attack-1
    #choose damage randomly based on attacks (TRY TO FIND ANOTHER WAY)
    if attack == 0 or attack == 2:
        dmg=random.randrange(0,40)
    if attack ==1 or attack ==3:
        dmg=random.randrange(20,80)
    print(player, "dealt", dmg, "using", bmove[attack], "to", battlepoke)
    #Health of battlepoke
    health1=health1-dmg
    #If health is 0 or below, then they lose
    if health1 <= 0:
        health1=0
        print(battlepoke, "has fallen", player, "wins!!!!")
        break
    print("Health of", battlepoke, "is", health1)
    print()
    #Opponent uses random number to pick attack
    attackpos=random.randrange(0,4)
    print(battlepoke, "used", opmove[attackpos])
    opattack=random.randrange(1,5)
    if opattack == 1 or opattack == 3:
        dmg=random.randrange(0,40)
    if opattack ==2 or opattack ==4:
        dmg=random.randrange(20,80)
    print(battlepoke, "dealt", dmg, "using", opmove[attackpos], "on", player)
    #Players health
    health2=health2-dmg
    if health2 <= 0:
        health2=0
        print(player,"has fallen", battlepoke, "wins!!!!")
        break
    print("Health of", player, "is", health2)
    print()
    
