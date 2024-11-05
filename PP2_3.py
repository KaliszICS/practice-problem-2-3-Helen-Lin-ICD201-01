'''
  Lesson: Else If
  Author: Helen Lin
  Date Created: October 16, 2024
  Date Last Modified: October 16, 2024
'''

def q1(): 
  #Write Assignment code here
  word = input("In: ")
  if word[-1] == "y":
    print("-ies")
  elif word[-1] == "ey": 
    print("-eys")
  elif word[-1] == "ife":
    print("-ives")
  else:
    print("-s")

def q2(): 
  #Write Assignment code here
  num = input("In: ")
  num = int(num)
  if num > 0:
    print(f'{num} is Positive')

  elif num < 0:
    print(f'{num} is Negative')

def q3():
  side1 = float(input("Input a number: "))
  side2 = float(input("Input another number: "))
  side3 = float(input("Input a third number: "))
  

  if side1 == side2 and side1 == side3 and side2 == side3: 
    print("Equalateral")
  elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles")
  elif side1 != side2 or side1 != side3 or side2 != side3:
    print("Scalene")
  elif side1 + side2 < side3 or side1 + side3 < side2 or side3 + side2 < side1:
    print("No triangle")
  

#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
#q3()