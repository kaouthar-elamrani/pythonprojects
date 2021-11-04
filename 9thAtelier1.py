def chercher(matrice, n, x):
    i = 0
    # les indexes du top droit element
    # n est j sont <n et >=0
    j = n - 1
    while (i < n and j >= 0):

        if (matrice[i][j] == x):
            print("element is at position ", i, ", ", j)
            return 1
        # if (i == n or j == -1 ) l'element n'existe pas
        if (matrice[i][j] > x):
            j -= 1

        # if matrice[i][j] < x
        else:
            i += 1

    print("Element doensn't exist")
    return 0

mat = [[11, 12, 41],
       [41, 14, 45],
       [45, 30, 79]]
chercher(mat, 3, 41)

