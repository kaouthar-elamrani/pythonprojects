list=[97,876,69,14,76,71,97]
counter = {'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
for l in list:
    if l in counter.values():
        list=counter.values()
print(list)