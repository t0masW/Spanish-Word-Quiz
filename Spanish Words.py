# Spanish Word Quiz

import random
import time


def randomizing_file():
  lines = open('Spanish Words.txt', 'r').readlines()
  random.shuffle(lines)
  open('Spanish Words.txt', 'w').writelines(lines)
  new_file(lines)
  
def new_file(new_list):
  filename = "Spanish Words Randomized.txt"
  with open(filename, "w") as fout:
    for line in new_list:
      fout.write(line)
  main()

def main():
    score = 0
    with open ("Spanish Words Randomized.txt", "r") as fin :  
        text = [line.strip() for line in fin.readlines() if len(line) > 1]

    for line in text :
      q, a = line.split(",")    
      answer = input("What is '" + q + "' in Spanish?:")
      if answer == a :
           print("correct")
           score = score +1
      else :
           print("It was", a)
           score = score -1

      time.sleep(1)
    print("You scored", score)
      
randomizing_file()

