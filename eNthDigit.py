import math
from decimal import getcontext, Decimal

#####---- checks if input is numerical. loop will break when an integer is entered
def checkInput(myinput) :
	while (myinput.isnumeric() == False) :
		print('Invalid input, must be a number less than 13')
		myinput = input('Enter number: ')
	return int(myinput)

#####---- main
print('This will print the value of e up to the desired number of decimal places. Limit is up to 12 places.')
intinput = checkInput(input('Enter number: '))

while (intinput > 12) :
	print('Number is greater than 12, please try again')
	intinput = checkInput(input('Enter number: '))

# set number of decimal places	
getcontext().prec = intinput + 1
# print value of e with /intinput/ number of places
print(Decimal(math.e)/1)
