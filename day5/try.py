try:
    num1 = int(input("enter n1:"))
    num2 = int(input("enter n2:"))
    result = num1 / num2
    print(f"result is:{result}")
except ZeroDivisionError:
    print(" zero is not divisiable!")
else:
    
finally:
    print("end of the program")
