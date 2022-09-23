def group_anagrams(strs):
	temp = []
	for word in strs:
		temp.append(''.join(sorted(word)))

	dic = {}
	for word in temp:
		dic[word]=[]

	for word in strs:
		item = ''.join(sorted(word))
		if item in dic:
			dic.get(item).append(word)
	
	ans = []
	for k,v in dic.items():
		ans.append(v)
	print(ans)


def main():
	strs = ["eat","tea","tan","ate","nat","bat"]
	group_anagrams(strs)

if __name__ == '__main__':
	main()