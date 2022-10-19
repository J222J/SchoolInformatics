minutes = eval(input("Enter the number of minutes : "))

days = minutes//60//24 % 365
years = minutes//60//24//365

print(minutes, "minutes is approximately", years, "years and", days, "days")
