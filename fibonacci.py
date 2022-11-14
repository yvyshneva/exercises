num = int(input())

def fibonacci(n):

	def recursive_fibonacci(n):
		if n <= 1:
			return n
		else:
			return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
      
	for i in range(n):
		print(recursive_fibonacci(i))


fibonacci(num)
