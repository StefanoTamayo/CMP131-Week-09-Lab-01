def celsius(Ftemp):
    C=0.3333334*(Ftemp-32)
    return C

def display(C):
    print("Temperature in celsius is", C)

def main ():
    Ftemp=float(input("Enter temperature in Fahrenheit: "))
    C=celsius(Ftemp)
    display(C)
main()
