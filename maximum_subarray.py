def maximum_subarray(nums):
	temp_sum = max_sum = float('-inf')
	for i in nums:
		temp_sum = max(temp_sum+i,i)
		max_sum = max(temp_sum,max_sum)
	return max_sum


def main():
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	print(maximum_subarray(nums))

if __name__ == '__main__':
	main()