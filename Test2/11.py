num = eval(input("Enter an integer: "))
d1 = num%10
d2 = num//10%10
d3 = num//100%10
d4 = num//1000

revnum = d1*1000 + d2*100 + d3*10 + d4
print(f"The reversed number is {revnum:04d}")
