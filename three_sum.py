def three_sum(nums):
	n,p,z = [], [], []

	for num in nums:
		if num > 0:
			p.append(num)

		if num == 0:
			z.append(num)

		if num < 0:
			n.append(num)

	N, P = set(n), set(p)

	res = []

	if z:
		for num in P:
			if -num in N:
				res.append([-num,0,num])

	if len(z)>=3:
		res.append([0,0,0])

	for i in range(len(n)):
		for j in range(i+1,len(n)):
			target = -(n[i]+n[j])
			if target in P:
				res.append(sorted([n[i],n[j],target]))

	for i in range(len(p)):
		for j in range(i+1,len(p)):
			target = -(p[i]+p[j])
			if target in N:
				res.append(sorted([p[i],p[j],target]))

	return res


def main():
	nums = [-1,0,1,2,-1,-4]
	print(three_sum(nums))

if __name__ == '__main__':
	main()