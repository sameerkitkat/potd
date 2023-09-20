def minimum_manipulation_to_make_anagram(s1,s2):
    count = 0
    ch_arr = [0]*256
    
    for ch in s1:
        print(ord(ch))
        ch_arr[ord(ch)]+=1
    print("===")
    for ch in s2:
        print(ord(ch))
        ch_arr[ord(ch)]-=1
    print(ch_arr)
    for ch in range (len(ch_arr)):
        if ch_arr[ch] != 0:
            count += abs(ch_arr[ch])
    return count//2

    
    

if __name__ == "__main__":
    s1 = "leetcode"
    s2 = "practice"
    print(minimum_manipulation_to_make_anagram(s1,s2))



	
