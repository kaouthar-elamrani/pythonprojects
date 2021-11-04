# we define the factorial function
def factorial(x):
   if x==1:
       return 1
   else:
       return (x*factorial(x-1))
#we declare the variables i and sum
i=1
sum=0
#we ask the user to input the number
n=int(input("input the number"))
#here we loop throught the values of i from 1 to n
while(i<=n):
    # here is where we call the factorial function , so the sum adds its old value in each loop
    sum += (factorial(i)/ i)
    i+=1

print(sum)

#gives 34.0 as output
