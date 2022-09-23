print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input(" Do you want to go left or right?\n")
directionl= direction.lower()
if directionl == "left":
   move2 = input(" You see a river do you want to swim or wait\n")
else:
 print("You fell into a hole. GAME OVER\n")
move2l = move2.lower()
if move2l == "wait":
 door= input(" Three magic doors red,blue and yellow have appeared which one will you choose\n")
else:
  print(" Attacked by trout. GAME OVER")
doorl = door.lower()
if doorl =="red":
  print("Burned by fire. GAME OVER")
elif doorl == "blue":
  print("Eaten by beasts. GAME OVER")
elif doorl == "yellow":
  print("You WIN\n")
else:
  print("GAME OVER")
