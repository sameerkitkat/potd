def rotate_matrix(matrix):
	rows = len(matrix)
	columns = len(matrix[0])
	ans = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for i in range(rows):
		for j in range(columns):
			ans[i][j] = matrix[j][i]

	for k in ans:
		reverse_arr(k)

	return ans

def reverse_arr(arr):
	i = 0 
	j = len(arr)-1

	while i<j:
		arr[i],arr[j] = arr[j], arr[i]
		i+=1
		j-=1

def main():
	matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
	ans = rotate_matrix(matrix)
	print(ans)


if __name__ == '__main__':
	main()