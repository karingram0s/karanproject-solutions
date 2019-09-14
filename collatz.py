def even(n) :
	return (n/2)

def odd(n) :
	return (n*3 + 1)

steps = 0

a = input('Enter integer greater than zero:')
a_prev = a

while (a > 1) :
	if (a%2 == 0) :
		a = even(a)
#		print(a)
	else :
		a = odd(a)
#		print(a)
	steps = steps + 1

print('It takes %d steps for %d to reach 1') % (steps,a_prev)
