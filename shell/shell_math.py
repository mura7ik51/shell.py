import sys
sys.set_int_max_str_digits(1000000)

def math():
#Addition
 b=input("math:")
 if b == "+":
    c = int(input("number0:"))
    d = int(input("number1:"))
    print(c+d)
 elif b == "+3":
    c = int(input("number0:"))
    d = int(input("number1:"))
    e = int(input("number2:"))
    print(c+d+e)
 elif b == "+4":
    c = int(input("number0:"))
    d = int(input("number1:"))
    e = int(input("number2:"))
    f = int(input("number3:"))
    print(c+d+e+f)
#Subtraction
 elif b == "-":
    c = int(input("number0:"))
    d = int(input("number1:"))
    print(c-d)
#Multiplication
 elif b == "*":
    c = int(input("number0:"))
    d = int(input("number1:"))
    print(c*d)
 elif b == "*3":
    c = int(input("number0:"))
    d = int(input("number1:"))
    e = int(input("number2:"))
    print(c*d*e)
#Division
 elif b == "/":
    c = int(input("number0:"))
    d = int(input("number1:"))
    print(c/d)
#PiCalculation
 elif b=="pi":
  PiX,PiY = 1,3
  while PiX < 2**64:
    PiZ=(4/(
        (2+2*(PiX-1))*(3+2*(PiX-1))*(4+2*(PiX-1))
        ))*((-1)**(PiX+1))
    PiY+=PiZ
    print(PiY,PiX,PiZ)
    PiX+=1


 