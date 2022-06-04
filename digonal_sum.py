
def digonal_sum(matrix):
	major_digonal=0
	minor_digonal=0

	n = len(matrix[0])

	for i in range(0,n):

		major_digonal+=matrix[i][i]
		minor_digonal+=matrix[i][n-i-1]
		
	print(major_digonal)
	print(minor_digonal)

def main():
	matrix = [[1,2,3,4],
			  [5,6,7,8],
			  [9,10,11,12],
			  [13,14,15,16]]
	digonal_sum(matrix)

if __name__ == '__main__':
 	main()