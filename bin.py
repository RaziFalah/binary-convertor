#Updated version
#Go to https://github.com/RaziFalah/binary-convertor/releases/tag/1.0.0v in order to download the .exe file
#=========================================================================================================================
#Made by Razi Falah
#Copyright (C) 2022 razifalah.com
#https://razifalah.com
#According to the applied license: LICENSE GNU General Public License v3.0
#You do not have the right to republish sell or edit this project, use it only for private use or educational purposes






# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  Please note, this program is meant to use on weeker devices such as calculators that's why it has basic functionalities such as else if. # 
#  since it does not have any external resources and powerful functions it should be convert friendly with basic langugaes  ################# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 









from re import A
from time import sleep
from cv2 import repeat

def repeat():
  bin = input("enter binary number: ")
  if len(bin) < 8:
      print("Binary number should not be any less than 8 digits")
      repeat()
  elif len(bin) > 8:
      print("Binary number should not execute 8 digits")
      repeat()
  elif len(bin) == 8:
      pass
  else:
      print("Unkown error")
      repeat()

  
  
  try:
      is_bin = int(bin,2)
      is_bin = True
      pass
  except ValueError:
      is_bin = False
      print("not a binary number")
  
  ask = input("Convert to hex or dec or both?: ")
  ask = ask.upper()
  ask = ask.strip()
  
  
  
  def bin2dex(bin):
    global bin_list
    bin_list = []
    
    for y in bin:
        bin_list.append(y)
    
    _1 = int(bin_list[0])
    _2 = int(bin_list[1])
    _3 = int(bin_list[2])
    _4 = int(bin_list[3])
    _5 = int(bin_list[4])
    _6 = int(bin_list[5])
    _7 = int(bin_list[6])
    _8 = int(bin_list[7])
    
    caculate_1 = _1 * 128
    caculate_2 = _2 * 64
    caculate_3 = _3 * 32
    caculate_4 = _4 * 16
    caculate_5 = _5 * 8
    caculate_6 = _6 * 4
    caculate_7 = _7 * 2
    caculate_8 = _8 * 1
    
    FINAL = caculate_1 + caculate_2 + caculate_3 + caculate_4 + caculate_5 + caculate_6 + caculate_7 + caculate_8
    print(FINAL)
  
  def bin2hex(bin):
      global list_a
      list_a = []
      for x in bin:
          list_a.append(x)
      a = list_a[0] + list_a[1] + list_a[2] + list_a[3]
      b = list_a[4] + list_a[5] + list_a[6] + list_a[7]
      if a == "0000":
          ans_a = ("0")
      elif a == "0001":
          ans_a = (1)
      elif a == "0010":
          ans_a = (2)
      elif a == "0011":
          ans_a = (3)
      elif a == "0100":
          ans_a = (4)
      elif a == "0101":
          ans_a = (5)
      elif a == "0110":
          ans_a = (6)
      elif a == "0111":
          ans_a = (7)
      elif a == "1000":
          ans_a = (8)
      elif a == "1001":
          ans_a = (9)
      elif a == "1010":
          ans_a = ("a")
      elif a == "1011":
          ans_a = ("b")
      elif a == "1100":
          ans_a = ("c")
      elif a == "1101":
          ans_a = ("d")
      elif a == "1110":
          ans_a = ("e")
      elif a == "1111":
          ans_a = ("f")
  
      if b == "0000":
          ans_b = ("0")
      elif b == "0001":
          ans_b = (1)
      elif b == "0010":
          ans_b = (2)
      elif b == "0011":
          ans_b = (3)
      elif b == "0100":
          ans_b = (4)
      elif b == "0101":
          ans_b = (5)
      elif b == "0110":
          ans_b = (6)
      elif b == "0111":
          ans_b = (7)
      elif b == "1000":
          ans_b = (8)
      elif b == "1001":
          ans_b = (9)
      elif b == "1010":
          ans_b = ("a")
      elif b == "1011":
          ans_b = ("b")
      elif b == "1100":
          ans_b = ("c")
      elif b == "1101":
          ans_b = ("d")
      elif b == "1110":
          ans_b = ("e")
      elif b == "1111":
          ans_b = ("f")
      print(str(ans_a) + str(ans_b))
  
  if ask == "DEC":
      bin2dex(bin)
  elif ask == "HEX":
      bin2hex(bin)
  elif ask == "BOTH":
      bin2dex(bin)
      bin2hex(bin)
  else:
      print("Unkown action!")
  

while 0 != 1:
 repeat()
