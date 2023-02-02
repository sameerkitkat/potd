def second_largest(arr):
	first = second = float('-inf')

	for n in arr:
		if n > first:
			second = first
			first = n
		if n > second and n != first:
			second = n 
	return second 



def main():
	arr = [11, 3, 6, 12, 1, 5, 8, 10, -1, 1000, 2000, 999]
	print(second_largest(arr))

if __name__ == '__main__':
	main()
