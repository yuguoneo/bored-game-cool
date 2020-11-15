# -*- coding:utf-8 -*-
import sys
from random import randint as rd

#第一次做游戏，做的不好，请见谅
#The first time to coding the game, do not do well, please understand.

#这是一个数字游戏
#this is a number game.

print('''数字炸弹
the number boom
我想一个数，在1到100间，你猜，我会告诉你大了还是小了
I think a number, between 1 and 100, you guessed it, I‘ll tell you
it’s big or small''')

playercoin = 200
print("you have %d now." % playercoin)
print("你有 %d 元了。" % playercoin)



def guess(numberis, playercoin):
  guesssb = 1
  print("start guess!开始猜测！")
  while guesssb:
    if playercoin <= 0:
        break
    if playercoin > 1000:
        break
    plgue = int(input("your guess--你的猜测:"))
    if plgue == numberis:
      print("yes!it is!--猜对啦！")
      playercoin = playercoin + 300
      print("you win 300!--你赢了300元！")
      guesssb = 0
    elif plgue < numberis:
      print("the number is bigger.--你猜的太小了。")
      playercoin = playercoin - 15
      print("you have %d now." % playercoin)
      print("你有 %d 元了。" % playercoin)
    elif plgue > numberis:
      print("the number is smaller.--你猜的太大了。")
      playercoin = playercoin - 15
      print("you have %d now." % playercoin)
      print("你有 %d 元了。" % playercoin)
      

  return playercoin
      
while True:
  if playercoin == 1000:
    print("you are verry rich!--哇！猜数字首富！")
    break
  elif playercoin <= 0:
    print("gameover.--你穷的一塌糊涂。")
    break
  else:
    numis = rd(1,99)
    playercoin=guess(numis, playercoin)
    print("you have %d now" % playercoin)
    print("你现在有 %d 元。" % playercoin)


#thanks for indexofire's help
