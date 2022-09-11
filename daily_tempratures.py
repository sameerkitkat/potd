def daily_tempratures(nums):
	n = len(nums)
	ans = [0]*n
	hottest = 0
	for i in range(n-1,-1,-1):
		curr_temp = nums[i]
		if curr_temp >= hottest:
			hottest = curr_temp
			continue
		days = 1
		while nums[i+days] <= curr_temp:
			days+=ans[i+days]
		ans[i] = days
	return ans


def main():
	nums = [73,74,75,71,69,72,76,73]
	ans = daily_tempratures(nums)
	print(ans)

if __name__ == '__main__':
	main()