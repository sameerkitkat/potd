def find_duplicates(nums):
	duplicate = -1
	for i in range(0,len(nums)):
		cur = abs(nums[i])
		if nums[cur] < 0:
			duplicate = cur
			break
		nums[cur] *= -1

	for i in range(0,len(nums)):
		nums[i] = abs(nums[i])

	return duplicate

def main():
	nums = [1,3,4,2,2]
	duplicate = find_duplicates(nums)
	print(duplicate)

if __name__ == '__main__':
	main()