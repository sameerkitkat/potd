def product_of_array_except_self(nums):
	n = len(nums)
	prefix_product = [1]*n
	suffix_product = [1]*n
	final_product = [1]*n

	'''prefix_product[0] = 1
	suffix_product[n-1] = 1'''

	for i in range(1,n):
		prefix_product[i] = prefix_product[i-1] * nums[i-1]

	for i in reversed (range(n-1)):
		suffix_product[i] = suffix_product[i+1] * nums[i+1]

	for i in range(n):
		final_product[i] = prefix_product[i]*suffix_product[i]

	print(final_product)		



def main():
	nums = [1,2,3,4]
	product_of_array_except_self(nums)


if __name__ == '__main__':
	main()