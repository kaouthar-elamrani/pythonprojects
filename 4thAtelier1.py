def fibonacci(x):
  #fibonacci prints 0 in case x=0 and 1 in case x=1
  if x==0 or x==1:
    return x
  else :
    #we call the function in recursion and it gives (x-1)+(x-2)
    return(fibonacci(x-1)+fibonacci(x-2))
j=0
nbr=int(input("the number"))
print("les",nbr,"premiers termes de la serie de fibonacci:")
#for i=1 to i<=nbr we call the fibonacci func and we give it the j as a parameter then we increment j
for i in range(1,nbr+1):
  print(fibonacci(j))
  j=j+1
  # if the user input n=5 it prints 0 1 1 2 3