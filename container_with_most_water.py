def max_area(height):
	left = 0
	right = len(height)-1
	maxarea = area = 0 

	while left < right :
		width = right - left
		area = min(height[left], height[right]) *  width
		maxarea = max(maxarea, area)
		if height[left] <= height[right]:
			left+=1
		else:
			right-=1
	return maxarea


def main():
	height = [1,8,6,2,5,4,8,3,7]
	print(max_area(height))

if __name__ == '__main__':
	main()