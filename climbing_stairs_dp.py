def climbing_stairs(n):
	one, two = 1, 1

	for i in range(n-1):
		temp = one 
		one = one+two
		two = temp

	return one 

def main():
	n = 5
	print(climbing_stairs(n)) 

if __name__ == '__main__':
	main()