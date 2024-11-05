'''
  Lesson: Else If
  Author: Helen Lin
  Date Created: October 16, 2024
  Date Last Modified: October 16, 2024
'''

def q1(): 
  #Write Assignment code here
  word = input("In: ")
  if word.endswith("ey"): 
    print("-eys")
  elif word.endswith("y"):
    print("-ies")
  elif word.endswith("ife"):
    print("-ives")
  else:
    print("-s")

def q2(): 
  #Write Assignment code here
  num = int(input("In: "))
  if num > 0:
    print(f'{num} is positive')
  elif num < 0:
    print(f'{num} is negative')

def q3():
  side1 = float(input("Input a number: "))
  side2 = float(input("Input a number: "))
  side3 = float(input("Input a number: "))
  

  if side1 == side2 and side1 == side3 and side2 == side3: 
    print("Equilateral")
  elif side1 == side2 and side1 != side3 or side1 == side3 and side1 != side2 or side2 == side3 and side2 != side1:
    print("Isosceles")
  elif (side1 + side2 < side3) or (side1 + side3 < side2) or (side2 + side3 < side1):
    print("No Triangle")
  elif side1 != side2 and side1 != side3 and side2 != side3:
    print("Scalene")
  

#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
#q3()