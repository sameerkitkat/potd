def is_subsequence(s,t):
    if len(s) == 0:
        return True

    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i+=1
        j+=1 
    return i == len(s)


def main():
    s = "abc"
    t = "abhgdc"
    print(is_subsequence(s,t))

if __name__ == "__main__":
    main()
