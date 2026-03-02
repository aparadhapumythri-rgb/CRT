'''Bug -> Error
finding and fixing of errors is called debugging .10
10

Types of Errors:
1) syntax Errors -->Missing of colon, Missing of Indentation
2) Runtime Error --> Division of any num with Zero
3) Logical Errors --> Missing of logics
Debugging Techniques:
1)print()
2)try -except
3)using of pdb
'''
try:
    a=int(input("Enter a"))
    print(10/a)
except ZeroDivisionError:
    print("Can not divisible by zero")
except ValueError:     
    print("Invalid input")