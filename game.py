# -*- coding:utf-8 -*-
import sys
from random import randint as rd

#第一次做游戏，做的不好，请见谅
#The first time to coding the game, do not do well, please understand.

#这是一个数字游戏
#this is a number game.

print("数字炸弹\n
      the number boom\n
      我想一个数，在1到100间，你猜，我会告诉你大了还是小了\n
      I think a number, between 1 and 100, you guessed it, I‘ll tell you whether it’s big or small\n")

playercoin = 200


def guess(numberis):
  guesssb = 1
  print("start guess!")
  while guesssb:
    plgue = int(input("your guess:"))
    playercoin = playercoin - 15
    if plgue == numberis:
      print("yes!it is!")
      playercoin = playercoin + 300
      guesssb = 0
    elif plgue < numberis:
      print("the number is bigger.")
    elif pigue > numberis:
      print("the number is smaller.")
      

while True:
  if playercoin == 100000:
    print("you are verry rich!")
    break
  elif playcoin <= 0:
    print("gameover")
    break
  else:
    numis = rd(1,99)
    guess(numis)
    
    
print("thanks for @indexoffire's help.")

      
