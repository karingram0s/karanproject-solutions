
#####---- checks if input is numerical. loop will break when an integer is entered
def checkInput(myinput) :
	while (myinput.isnumeric() == False) :
		print('Invalid input, must be a number greater than 0')
		myinput = input('Enter number: ')
	return int(myinput)

#####---- main
print('This will print the Fibonacci sequence up to the desired number.')
intinput = checkInput(input('Enter number: '))

while (intinput < 1) :
	print('Number is 0, please try again')
	intinput = checkInput(input('Enter number: '))

a = 0
b = 1
temp = 0

for i in range(intinput) :
	print('{0} '.format(a+b), end='', flush=True)
	if (i < 1) :
		continue
	else :
		temp = a + b
		a = b 
		b = temp 
	
print('')
