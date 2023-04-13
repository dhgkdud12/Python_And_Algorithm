T = 10
for t in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))

    resultCnt = 0

    for i in range(2, N - 2):
        maxLeftHeight = max(buildings[i - 1], buildings[i - 2])
        maxRightHeight = max(buildings[i + 1], buildings[i + 2])

        maxHeight = max(maxLeftHeight, maxRightHeight)

        curHeight = buildings[i]

        if curHeight > maxHeight:
            resultCnt += curHeight - maxHeight

    print('#'+str(t), resultCnt)