def find_numbers(low,high):
	digits_in_low = get_digits(low)
	digits_in_high = get_digits(high)
	ans = []
	while digits_in_low <= digits_in_high:
		temp = generate_numbers(digits_in_low)
		for i in temp:
			if low <= i <= high:
				ans.append(i)
		digits_in_low+=1
	return ans

def generate_numbers(n):

	ans = []
	num = 0
	for i in range(0,n):
		num = num * 10 + (i + 1)

	add = 0
	for j in range(0,n):
		add = add * 10 + 1

	while 0 < num%10 <=9:
		ans.append(num)
		num += add

	return ans  

def get_digits(num):
	count = 0
	while num > 0:
		num = num//10
		count += 1
	return count 

def main():
	low = 100
	high = 3000200
	print(find_numbers(low,high))


if __name__ == '__main__':
	main()