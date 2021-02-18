import random
import os #clear screen

os.system('cls')


file = open("Items to pick from.txt", "r")
choices = []

for line in file:
  if (line != '\n'): #if line not empty
    choices.append(line)


itemPicked = random.choice(choices)
print("The randomly picked item that has been selected is:\n" + itemPicked)

file.close()