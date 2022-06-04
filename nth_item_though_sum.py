def nth_item(L1, L2, A, B, N):
    seen = set()
    new =[]
    for i in range(len(A)):
        for j in range(len(B)):
            s = A[i]+B[j]
            if s not in seen:
                new.append(s)
                seen.add(s)
    new.sort()
                
    if N>len(new):
        return -1
    else:
        return new[N-1]

def main():
    L1 = 2
    L2 = 2
    A = [1,2,3,4]
    B = [1,2,3,4]
    N = 16
    print(nth_item(L1,L2,A,B,N))


if __name__ == '__main__':
    main()