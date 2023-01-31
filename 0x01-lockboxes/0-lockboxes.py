def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened
    """
    foundKey = False

    i = 0

    while (i < len(boxes)):
        foundKey = False
        j = 0
        while j < len(boxes):
            k = 0
            while k < len(boxes[j]):
                if (boxes[j][k] == i) and i != j:
                    foundKey = True
                    break
                k += 1
            if foundKey:
                break

            j += 1

        i += 1

    if foundKey:
        return True
    else:
        return False
