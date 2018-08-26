T = int(raw_input())

for test in range(1, T+1):
    N, K = [int(s) for s in raw_input().split(" ")]
    A = [int(s) for s in raw_input().split(" ")]
    A = sorted(A)
    result = 0
    ctr = 0
    day = 0
    for i in range(N):
        if day < A[i] and ctr < K:
            result += 1
            ctr += 1
        
        if ctr == K:
            ctr = 0
            day += 1
    print "Case #" + str(test) +": " + str(result)