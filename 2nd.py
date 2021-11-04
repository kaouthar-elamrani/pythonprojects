l = [13, 52, 34, 788, 45, 41, 7, 99, 10]
# pour i de 0 au lieme-1 element avec un pas de 3
for i in range(0,len(l),3):
  # x sont les listes pris de list l de 3 element
  x=l[i:i+3]
  # en inverse x avec fonction reverse
  x.reverse()
  print(x)

