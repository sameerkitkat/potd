def first_unique_character(s):
	dic = {}
	for c in s:
		if c in dic:
			dic[c] = dic[c]+1
		else:
			dic[c] = 1

	for k,v in dic.items():
		if v == 1:
			return k


def main():
	s = "love leetcode"
	print(first_unique_character(s))

if __name__ == '__main__':
	main()