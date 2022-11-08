def three_sum_closest(nums,target):
	diff = float('inf')
	nums.sort()

	for i in range(len(nums)):
		low, high = i+1, len(nums)-1

		while (low<high):
			sum_here = nums[i] + nums[low] + nums[high]

			if abs(target-sum_here) < abs(diff):
				diff = target - sum_here

			if sum_here < target:
				low+=1
			else:
				high-=1

		if diff == 0:
			break
	return target - diff



def main():
	nums = [-1,2,1,-4]
	target = 1
	print(three_sum_closest(nums,target))

if __name__ == '__main__':
	main()