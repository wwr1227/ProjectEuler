import math
def gcd(m, n):
	return m if n==0 else gcd(n, m%n)
def is_prime(n):
	for i in range(2,n):
		if n%i == 0 :
			return False
	return True
max = 1
for i in range(1,21):
	if max%i!=0 and is_prime(i):		
		max*=i
		print max, i
print '========='
for i in range(1,21):
	if max%i!=0:
		g = gcd(max, i)
		max*=g
		print max, g
print max