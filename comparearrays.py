def compareTriplets(a, b):
    loopLen = 0
    if len(a) > len(b):
        loopLen = len(a)
    elif len(a) == len(b):
        loopLen = len(a)
    elif len(a) < len(b):
        loopLen = len(b)
    bob = 0
    alice = 0
    for i in range(0, loopLen):
        if a[i] > b[i]:
            bob += 1
        elif a[i] == b[i]:
            bob += 0
            alice += 0
        elif a[i] < b[i]:
            alice += 1
        i += 1
        
    return bob, alice
