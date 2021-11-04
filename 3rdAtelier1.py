#defining function
def sum(n):
  if n==1:
    return 1
  else:
    #here is the recursion part we add n to its previous number
    res=n+sum(n-1)
    return res
som=0
# we ask the user for input
#the som variable received the function with a parameter'n'
n=int(input("n"))
som=sum(n)
print(sum(n))
#if the user inputs 5 it gives 15 as output