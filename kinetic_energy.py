# Main program
def main():
    print("Area Calculator")
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rect_area = rectangle_area(length, width)
    print(f"The area of the rectangle is: {rect_area}")
    # Get input for circle radius
    radius = float(input("Enter the radius of the circle: "))
    circ_area = circle_area(radius)
    print(f"The area of the circle is: {circ_area}")
# Calling the main function to run the program
main()

m=float(input("Enter objects mass in kg: "))
v=float(input("Enter objects velocity in meters/second: "))
KE=1/2*m*(v**2)
print(KE)