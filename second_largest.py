def second_largest(arr):
	first = second = float('-inf')

	for i in range(0,len(arr)):
		if arr[i] > first:
			second = first
			first = arr[i]
		elif arr[i] > second and arr[i] != first:
			second = arr[i]
	return second



def main():
	arr = [3, 6, 12, 1, 5, 8]
	print(second_largest(arr))

if __name__ == '__main__':
	main()