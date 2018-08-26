T = int(raw_input())

def binInt(lst):
    result = ""
    for i in lst:
        result = str(i) + result
    return int(result,2)

def calcVal(TotalP, result, N):
    s = 0
    for i in range(len(result)):
        if result[i] == 1:
            s += N - TotalP[i]
        else:
            s += TotalP[i]
    return s

def recursiveHelper(TotalP, result, complain, Forbid, ind, N):
    if binInt(result) not in Forbid:
        fin = calcVal(TotalP, result, N)
        complain['val'] = min(complain['val'], fin)
    if ind == len(TotalP):
        return
    # print ind
    # print result
    ress = result[:]
    ress1 = result[:]

    recursiveHelper(TotalP, ress, complain, Forbid,ind+1, N)
    ress1[ind] = (ress1[ind] + 1) %2

    recursiveHelper(TotalP, ress1, complain, Forbid, ind+1, N)

for test in range(1, T+1):
    N, M, P = [int(s) for s in raw_input().split(" ")]
    Order = [int(raw_input(),2) for i in range(N)]
    Forbid = [int(raw_input(),2) for i in range(M)]
    TotalP = [0]*P

    for i in range(N):
        for j in range(P):
            if Order[i] & (1 << j):
                TotalP[j] += 1
    
    # result = [0] * P 
    # for i in range(P):
    #     if TotalP[i] >= P//2:
    #         result[i] = 1
    # print result
    # print TotalP
    # print calcVal(TotalP, result, N)
    
    complain = {}
    complain['val'] = 99999999
    res = [0]* P
    recursiveHelper(TotalP, res, complain, Forbid, 0, N)
    
    print "Case #" + str(test) +": " + str(complain['val'])