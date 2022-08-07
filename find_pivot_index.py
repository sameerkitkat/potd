def find_pivot_index(nums):
	left_sum=[0]*len(nums)
	right_sum=[0]*len(nums)
	
	ans = -1
	left_sum[0] = nums[0]
	right_sum[len(nums)-1] = nums[-1]


	for i in range(1,len(nums)):
		left_sum[i] = left_sum[i-1] + nums[i] 

	
	for i in reversed(range(0,len(nums)-1)):
		right_sum[i] = right_sum[i+1] + nums[i]

	print(left_sum)
	print(right_sum)
	count = 0 
	for i, j in zip(left_sum, right_sum):
		if i - j == 0:
			return count	
		count += 1	

def main():
	nums = [-1,-1,0,-1,-1,0]
	find_pivot_index(nums)	


if __name__ == "__main__":
	main()
