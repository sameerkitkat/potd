def add_binary(s1,s2):
	carry = 0
	i = len(s1)-1
	j = len(s2)-1
	res = ""

	while i > -1 or j > -1 or carry:
		if i > -1:
			carry+=int(s1[i])
			i-=1
		if j > -1:
			carry+=int(s2[j])
			j-=1

		res = res+str(carry%2)
		carry = carry // 2

	return res[::-1]


def main():
	s1 = "1111"
	s2 = "1111"
	result = add_binary(s1,s2)
	print(result)

if __name__ == '__main__':
	main()