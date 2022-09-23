def longest_substring_without_repeating_chars(s):
	str_list = []
	max_length = 0
	for x in s:
		if x in str_list:
			#str_list = str_list[str_list.index(x)+1:]
			str_list = str_list.pop(str_list.index(x))
			print(str_list)

		str_list.append(x)    
		max_length = max(max_length, len(str_list))
		print(max_length)
	return max_length

def main():
	s = "abcabcbb"
	print(longest_substring_without_repeating_chars(s))

if __name__ == '__main__':
	main()