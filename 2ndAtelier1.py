#creationg the binary convertor function with recursion
def binary_conversion(decimal):
    if decimal==0:
        return 0
    else:
        #here we call the function with recursion
        return (decimal%2+10*binary_conversion(decimal//2))

decimal=float(input("enter un nombre decimal"))
binaire=binary_conversion(decimal)
print(binaire)
