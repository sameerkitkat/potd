def longest_substring_without_repeating_chars(s):
	n = len(s)
	ans = 0
	m = {}
	i = 0

	for j in range(n):
		if s[j] in m:
			i = max(m[s[j]],i)
		ans = max(ans, j-i+1)
		m[s[j]]=j+1
	return ans 


def main():
	s = "abcabcbb"
	print(longest_substring_without_repeating_chars(s))

if __name__ == '__main__':
	main()