def TypeAnalize(data):
    lst = []
    if type(data) is tuple or type(data) is list:
        for i in data:
            if type(i) not in lst:
                lst.append(type(i))
        return len(lst)
    else:
        return type(data)

def IntFloatFilter(data):
    lst = []
    for i in data:
        if type(i) is int or type(i) is float:
            lst.append(i)
    for i in range(len(lst)):
        idxMin = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[idxMin]:
                idxMin = j
        tmp = lst[idxMin]
        lst[idxMin] = lst[i]
        lst[i] = tmp
    return lst


