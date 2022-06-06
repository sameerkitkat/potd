def two_sum(nums,target):
	dic = {}
	for i in range(0,len(nums)):
		complement = target - nums[i]
		if complement in dic:
			return [dic[complement], i]
		dic[nums[i]] = i



def main():
	nums = [2,7,11,15]
	target = 9
	print(two_sum(nums,target))

if __name__ == '__main__':
	main()