def kineticEnergy(m, v):
    KE=0.5*m*(v**2)
    return (KE)


def display(KE):
    print("The value of kinetic energy is", KE)



def main():
    m=float(input("Enter the mass of the object in kilograms: "))
    v=float(input("Enter the velocity of the object in meters per second: "))
    KE=kineticEnergy(m, v)
    display(KE)
main()
