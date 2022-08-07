def isomorphic_strings(s,t):
	if len(s) != len(t):
		print("Invalid input")
		return
	l1 = [0] * 256
	l2 = [0] * 256

	for i in range(len(s)):
		if l1[ord(s[i])] != l2[ord(t[i])]:
			return False
		l1[ord(s[i])] = i+1
		l2[ord(t[i])] = i+1
	return True	


def main():
	s = "paper"
	t = "title"
	print(isomorphic_strings(s,t))
	
if __name__ == "__main__":
	main()
