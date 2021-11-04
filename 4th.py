def intersection(set1, set2):
    #ici on traverse sur les element du set 1 si en le trouve dans set2 en le met dans set3
    set3 = {element for element in set1 if element in set2}
    return set3
set1 = {74, 9, 1, 17, 11, 22, 28, 54, 26}
set2 = {10, 13, 74, 21, 45, 11, 52, 28, 9}
#l'intersection su set1 et set 2=set3
print(intersection(set1, set2))
set3=intersection(set1,set2)
#on supprime les elements du set3 de set 1 en utilisant la fonction dofference_update puis on affiche
set1.difference_update(set3)
print(set1)




