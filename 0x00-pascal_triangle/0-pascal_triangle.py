def pascal_triangle(n):
        """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
            listToReturn = []
                for i in range(n):
                            tempList = []
                                    for j in range(i + 1):
                                                    if j == 0 or j == i:
                                                                        tempList.append(1)
                                                    else:
                                                                        tempList.append(listToReturn[i - 1][j - 1] + listToReturn[i - 1][j])
                                                                                listToReturn.append(tempList)

                                                                                    return listToReturn
