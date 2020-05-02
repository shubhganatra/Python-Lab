while (1):
	A=int(input('Enter the non-negative integer: '))
	if A<0 or A>1000:
		print('Invalid Input. Re-enter.')
	else:
		break
b=1
while b<A:
	for a in range(b+1):
		if a==0:
			continue
		if ((a**2 + b**2)==A):
			print('({},{})'.format(a,b))
	b=b+1