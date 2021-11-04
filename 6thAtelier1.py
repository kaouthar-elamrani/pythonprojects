def bullsort(array):
    n = len(array)

    # loop sur les elements du tableau
    for i in range(n-1):
        for j in range(0,n-i-1):

            # loop le tableau du 0 a n-i-1
            #placer le deuxieme au premier s'il est olus petit puis le next element
            if array[j] > array[j+1]:
                #storer l'element array[j] qui est > array[j+1] dans temp puis echanger les elements du array[j+1] qui sera array[j] et array[j+1] sera array[j]
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array
def insertionsort(array):
        # Traverser du 1 a len(arr)
        for i in range(1, len(array)):
            temp = array[i] # recuperer le deuxieme element
            j = i - 1
            while j >= 0 and temp < array[j]:
                arr[j+1] = arr[j] # declarer unen case d'avant
                j =j-1
            array[j+1] = temp # inserer l'element chercher a la position j+1

def selectionsort(array):
    n = len(array)
    for i in range(n):
        # premierement supposer que le premier element du tableau est minimum
        min = i
        for j in range(i+1,n):
            if (array[j]<array[min]):
                # changer la position du min element si on trouve un plus petit element
                min = j
       #changer le min avec le premier element du tableau
        temp = array[i]
        array[i] = array[min]
        array[min] = temp

    return array
# ici je demande a l'utilisateur le remplir le tableau et choisir quelle methode du tri il prefere en utilisant if statement en faisant l'appelle au nos trois fonctions


arr=[]
n=int(input("enter number of elements "))
for i in range(0,n):
    element=int(input("input"))
    arr.append(element)
print("array before sorting it ",arr)
print("please select the sort method: type 1 for bubble sort type 2 for insertion sort and 3 for selection sort")
num=int(input("The choice made?"))
if num==1:
    bullsort(arr)
    print("Sorted array is:")
    for i in range(len(arr)):
        print("% d" % arr[i])
elif num==2:
    insertionsort(arr)
    print("Sorted array is:")
    for i in range(len(arr)):
        print("% d" % arr[i])
else:
    selectionsort(arr)
    print("Sorted array")
    for i in range(len(arr)):
        print("%d" % arr[i])







