try:
	pin=int(input("Enter the pin: "))
	if(pin==4949):
		print("Lock Opened")
		exit()
except ValueError:
	print("Full alarm")
	exit()
	
print("Wrong PIN! Try again")
try:
	pin=int(input("Enter the pin: "))
	if(pin==4949):
		print("Lock Opened")
	else:
		print("Full alarm")
except ValueError:
	print("Full alarm")
