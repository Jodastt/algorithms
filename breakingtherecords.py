def breakingRecords(scores):
    high = low = scores[0]
    countH = countL = 0
    for i in scores:
        if high < i:
            countH += 1
            high = i
        if low > i:
            countL += 1
            low = i
        i += 1
    return countH, countL
