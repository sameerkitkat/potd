def equlibrium_point(nums):
	#[1,4,9,11,13]
	#[13,12,9,4,2]
	n = len(nums)
	prefix_sum = [0]*n
	suffix_sum = [0]*n

	for i in range(1,len(nums)):
		prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

	for i in range(n-2,-1,-1):
		suffix_sum[i] = suffix_sum[i+1] + nums[i+1]

	print(prefix_sum)
	print(suffix_sum)

	for (i,j) in zip(prefix_sum,suffix_sum):
		if i == j:
			return prefix_sum.index(i)+1
		

def main():
	nums = [1,3,5,2,2]
	print(equlibrium_point(nums))

if __name__ == '__main__':
	main()