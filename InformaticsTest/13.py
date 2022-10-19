number = eval(input("Enter an integer : "))

digit1 = number % 10
digit2 = number // 10 % 10
digit3 = number // 100 % 10
digit4 = number // 1000 % 10

reverse_number = digit1*1000 + digit2*100 + digit3*10 + digit4

print("Reverse number :", reverse_number)
