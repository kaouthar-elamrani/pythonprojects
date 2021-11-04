def nmber_digit(x):
 #si le nombre<10 le nombre de ses chiffres est 1
  if x<10:
    return 1
  else:
    # la fonction nmber_digit(n/10) donne le nombre de division effectuee quand n>=10 , quand n<10 on donne 1
    return 1+nmber_digit(x/10)
n=int(input(" input n"))
print(nmber_digit(n))
#if the input is 2141546578 the output is 10