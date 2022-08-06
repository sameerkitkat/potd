def remove_duplicates(s):
	stack = []
	for i in s:
		if len(stack) == 0 or stack[-1] != i:
			stack.append(i)
		else:
			stack.pop()			
	print(stack)


def main():
	s = "acaaabbbacdddd"
	remove_duplicates(s)

if __name__ == '__main__':
	main()