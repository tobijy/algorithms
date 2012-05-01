def factorial(n):
	if n < 0:
		return ValueError

	if n == 0:
		return 1

	if n > 0:
		tmp = 1
		for i in range(2, n+1):
			tmp *= i		
		return tmp
