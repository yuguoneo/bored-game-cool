# -*- coding:utf-8 -*-
import sys
from random import randint as rd

#第一次做游戏，做的不好，请见谅
#The first time to coding the game, do not do well, please understand.

#这是一个数字游戏
#this is a number game.

print('''      数字炸弹
      the number boom
      我想一个数，在1到100间，你猜，我会告诉你大了还是小了
      I think a number, between 1 and 100, you guessed it, I‘ll tell you
      it’s big or small''')

playercoin = 200



def guess(numberis, playercoin):
  guesssb = 1
  print("start guess!")
  while guesssb:
    if playercoin <= 0:
        break
    plgue = int(input("your guess:"))
    if plgue == numberis:
      print("yes!it is!")
      playercoin = playercoin + 300
      print("you win 300!")
      guesssb = 0
    elif plgue < numberis:
      print("the number is bigger.")
      playercoin = playercoin - 15
    elif plgue > numberis:
      print("the number is smaller.")
      playercoin = playercoin - 15

  return playercoin
      
while True:
  if playercoin == 1000:
    print("you are verry rich!")
    break
  elif playercoin <= 0:
    print("gameover")
    break
  else:
    numis = rd(1,99)
    playercoin=guess(numis, playercoin)
    print("you have %d now" % playercoin)
    
    
    
print("thanks for @indexofire's help.")

