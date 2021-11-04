def letter_frequence(string):
    counter = {}
    for l in string:
        if l != ' ':
            if l in counter:
                counter[l] += 1
            else:
                counter[l] = 1
    return counter
string=str(input("enter a string"))
print(letter_frequence(string))


