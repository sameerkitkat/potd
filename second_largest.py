def second_largest(arr):
	first = second = float('-inf')

	for i in arr:
		if i > first:
			second = first
			first = i
		elif i > second and second != first:
			second = i
	return second




def main():
	arr = [3, 6, 12, 1, 5, 8]
	print(second_largest(arr))

if __name__ == '__main__':
	main()
