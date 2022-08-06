def running_sum(nums):
	ans = [0]*len(nums)
	ans[0] = nums[0]
	for i in range(0,len(nums)-1):
		sum = nums[i] + nums[i+1]
		ans[i+1]= ans[i-1] + sum
	return ans

def main():
	nums =[1,2,3,4]
	print(running_sum(nums))


if __name__ == "__main__":
	main()
