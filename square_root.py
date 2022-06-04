def floor_sqrt(x): 
    start = 1
    end = x//2 + 1
    while start <= end:
        mid = (start+end)//2
        if mid * mid == x:
            return mid 
        elif mid * mid < x:
            start = mid + 1
        else:
            end = mid - 1
    return end 

def main():
    x = 19
    print(floor_sqrt(x))

if __name__ == '__main__':
    main()
