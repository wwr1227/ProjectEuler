def isPali(num):
	string1 = str(num)
	string2 = string1[::-1]
	if string1 == string2:
		print('It is a palindrome')
		return True
	else:
		print('It is not a palindrome')
		return False


num1 = 999
num2 = 999
n1 = -1
n2 = -1
max = -1
product = 1
while num1 > 0:
	while num2 > 0:
		print num1, num2
		if isPali(num1 * num2) and num1 + num2 > max:
			n1 = num1
			n2 = num2
			product =num1 * num2
			max = num1+num2
			print product
			break
		else :
			num2-=1
	num1-=1
	num2=num1
else:
	print 'The while loop is over.'
	print product, max, n1, n2

