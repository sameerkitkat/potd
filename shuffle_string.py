def shuffle_string(s, indices):
	temp = [None] * len(indices)
	j = 0
	for i in indices:
		temp[i] = s[j]
		j+=1
	return ''.join(temp)


def main():
	s = "codeleet"
	indices = [4,5,6,7,0,2,1,3]
	print(shuffle_string(s,indices))

if __name__ == '__main__':
	main()