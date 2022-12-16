import sys

def calculateDrainage(arr):
    lenArr = createLengthArray(arr)
    sortedArr = createSortedCoordArr(arr)
    
    return iterateLargest(arr, lenArr, sortedArr)

## Check largest, see if there's anything larger
## If there's something larger that's adjacent, make length +1 of 
## large adjacent thing

def iterateLargest(arr, lenArr, sortedArr):
    maxVal = 0
    for i in sortedArr:
        size = lenArr[i[1]][i[2]]
        lenArr[i[1]][i[2]] = max(size, largestAdjChain(arr, lenArr, i)+1)
        size = lenArr[i[1]][i[2]]
        maxVal = max(maxVal, size)

    return maxVal+1

def largestAdjChain(arr, lenArr, sortedArrObj):
    i = sortedArrObj[1]
    j = sortedArrObj[2]
    length = -1
    if i > 0:
        if arr[i-1][j] > sortedArrObj[0]:
            length = max(length, lenArr[i-1][j])
    if i < len(arr)-1:
        if arr[i+1][j] > sortedArrObj[0]:
            length = max(length, lenArr[i+1][j])
    if j > 0:
        if arr[i][j-1] > sortedArrObj[0]:
            length = max(length, lenArr[i][j-1])
    if j < len(arr[0])-1:
        if arr[i][j+1] > sortedArrObj[0]:
            length = max(length, lenArr[i][j+1])

    return length

def createSortedCoordArr(arr):
    newArr = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            newArr.append((arr[i][j], i, j))
    
    newArr.sort(key=lambda x: x[0], reverse=True)
    return newArr

def createLengthArray(arr):
    lenArr = []
    for i in range(len(arr)):
        lenArr.append([])
        for j in arr[i]:
            lenArr[i].append(-1)
    return lenArr

def processLine(line):
    line = line.split(" ")
    parsedLine = []
    for i in line:
        parsedLine.append(int(i))
    return parsedLine

if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        l = input().rstrip().split(" ")
        title = l[0]
        rows = int(l[1])
        cols = int(l[2])
        arr = []
        for j in range(rows):
            line = input().rstrip()
            arr.append(processLine(line))
        print(title + ": " + str(calculateDrainage(arr)))