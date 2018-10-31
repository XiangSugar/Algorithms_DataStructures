# coding = utf - 8
# 2018-10-30  20:30

##################################################################
# coinValueList: 零钱面值列表
# change: 需要找零的钱

def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)
            if minCoins > numCoins:
                minCoins = numCoins
    return minCoins
##################################################################
# knownResult: 记录下之前计算过的面值的最小找零数，以免重复计算

def recDC(coinValueList, change, knownResult):
    minCoins = change
    if change in coinValueList:
        knownResult[change] = 1
        return 1
    elif knownResult[change] > 0:
        return knownResult[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knownResult)
            if minCoins > numCoins:
                minCoins = numCoins
                knownResult[change] = minCoins
    return minCoins
###################################################################

# minCoins: 记录部分找零的最优解
def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(change + 1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
        minCoins[cents] = coinCount
    return minCoins[change]
###################################################################
# coinUsed: 用来找零所使用的硬币的列表
def dpMakeChange2(coinValueList, change, minCoins, coinUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinUsed[cents] = newCoin
    return minCoins[change]
def printCoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin
#################################################################

def main():
    amnt = 59
    clist = [1, 5, 10, 21, 25]
    coinUsed = [0] * (amnt + 1)
    coinCount = [0] * (amnt + 1)
    print("Making chenge for ", amnt, "requires")
    print(dpMakeChange2(clist, amnt, coinCount, coinUsed), "coins")
    print("They are:")
    printCoins(coinUsed, amnt)
    print("The used list is as follows:")
    print(coinUsed)

if __name__ == "__main__":
    main()
