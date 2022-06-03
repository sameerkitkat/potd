def rearrange(arr):
	i = 0
	j = 1
	while True:
		while i < len(arr) and arr[i]%2 == 0:
			i+=2
		while j < len(arr) and arr[j]%2 == 1:
			j+=2
		if i < len(arr) and j < len(arr):
			arr[i], arr[j] = arr[j], arr[i]
		else:
			break

	print(arr)
	return 1





def main():
	arr = [3, 6, 12, 1, 5, 8]
	rearrange(arr)

if __name__ == '__main__':
	main()