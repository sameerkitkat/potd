def search(matrix,target):
	start = 0
	end = len(matrix)*len(matrix[0])-1
	len_col = len(matrix[0])

	while start <= end:
		mid = (start+end)//2
		if target == matrix[mid//len_col][mid%len_col]:
			return [mid//len_col,mid%len_col]
		elif target < matrix[mid//len_col][mid%len_col]:
			end = mid - 1
		else:
			start = mid + 1
	return -1

def main():
	matrix = [[1,2,3],
			  [4,5,6],
			  [7,8,9]]
	target = 3
	print(search(matrix,target))

if __name__ == '__main__':
	main()