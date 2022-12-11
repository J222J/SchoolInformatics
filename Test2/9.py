name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week (e.g. 10): "))
pay = eval(input("Enter hourly pay rate (e.g. 9.75): "))
federaltax = eval(input("Enter federal tax withholding rate (e.g. 20%): "))
statetax = eval(input("Enter state tax withholding rate (e.g. 9%): "))

print(f"Employee Name: {name}\n",
	  f"Hours Worked: {hours}\n",
	  f"Pay Rate: ${pay}\n",
	  f"Gross Pay: ${pay*hours}\n",
	  f"Deductions:\n",
	  f"\tFederal Withholding ({(federaltax*100):0.2f}%): ${(pay*hours*federaltax):0.2f}\n",
	  f"\tState Withholding ({(statetax*100):0.2f}%): ${(pay*hours*statetax):0.2f}\n",
	  f"\tTotal Deduction: {((pay*hours*federaltax) + (pay*hours*statetax)):0.2f} Net Pay {((pay*hours) - (pay*hours*federaltax) - (pay*hours*statetax)):0.2f}", sep="")