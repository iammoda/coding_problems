def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while j > i:
        while j > i and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] == array[j], array[i]
        i += 1
    return array
