from sys import stdin


def multiply(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


def getProductArrayExceptSelf(arr, n):
    return [multiply(arr[:i] + arr[i + 1:]) for i, x in enumerate(arr)]


def takeInput():
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    t = int(stdin.readline().rstrip())
    while t > 0:
        arr, n = takeInput()
        product = getProductArrayExceptSelf(arr, n)
        printList(product, n)
        t -= 1
