def listcount(list1):
    counter = {}
    for l in list:
            if l in counter:
                counter[l] += 1
            else:
                counter[l] = 1
    return counter
list=[14,51,7,8,8,8,51,17,14,71,71]
print(listcount(list))


