def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    if arrayOne[0] != arrayTwo[0]:
        return False

    leftOne = smallerThan(arrayOne)
    leftTwo = smallerThan(arrayTwo)
    rightOne = largerThan(arrayOne)
    rightTwo = largerThan(arrayTwo)

    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)


def smallerThan(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller


def largerThan(array):
    larger = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            larger.append(array[i])
    return larger
