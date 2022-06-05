def search(matrix,target):
	start = 0
	end = len(matrix)-1

	while start < end+1 and end > 0:
		if target == matrix[start][end]:
			return True
		elif target < matrix[start][end]:
			end -= 1
		else:
			start += 1
	return False

def main():
	matrix = [[1,2,3],
			  [4,5,6],
			  [7,8,9]]
	target = 90
	print(search(matrix,target))

if __name__ == '__main__':
	main()