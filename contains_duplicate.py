def contains_duplicate(nums):
	n = len(nums)

	if  n > 1:
		slow = nums[0]
		fast = nums[nums[0]]

		while fast != slow :
			slow = nums[slow]
			fast = nums[nums[fast]]

		fast = 0

		while slow != fast:
			slow = nums[slow]
			fast = nums[fast]

		return slow
	return -1

def main():
	nums = [1,2,3,1]
	print(contains_duplicate(nums))

if __name__ == '__main__':
	main()