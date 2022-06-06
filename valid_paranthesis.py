def valid_paranthesis(s):
	stack = []
	for c in s:
		if c == "{" or c == "(" or c == "[":
			stack.append(c)
		elif len(stack) != 0 and is_valid(stack[-1],c):
			stack.pop()
		else:
			return False
	return len(stack) == 0

def is_valid(a,b):
	if a == "{" and b == "}":
		return True
	if a == "[" and b == "]":
		return True
	if a == "(" and b == ")":
		return True
	else:
		return False


def main():
	s = "{[{()}]}[({[]})]({[][]})"
	print(valid_paranthesis(s))

if __name__ == '__main__':
	main()