def rob(nums):
	rob1, rob2 = 0, 0

	#[rob1,rob2,n,n+1]
	for n in nums:
		temp = max(rob1+n,rob2)
		rob1 = rob2
		rob2 = temp

	return rob2


def main():
	nums = [1,2,3,1]
	rob(nums)

if __name__ == '__main__':
	main()