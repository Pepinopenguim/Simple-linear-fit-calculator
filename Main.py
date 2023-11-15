def Solve_LS_2x2(a11, a12, a21, a22, b1, b2):
    # Solves a 2x2 linear system of equations using Gaussian elimination
    if a11 != 0:
        a22 = a22 - a12*(a21/a11)
        b2 = b2 - b1*(a21/a11)

        x2 = b2/a22
        x1 = (b1 - a12*x2)/a11
    elif a12 != 0:
        x2 = b1/a12
        x1 = (b2-a22*x2)/a21
    else:
        return (0,0)

    return (x1, x2)

def Main_code():

    plist = []

    # Read input points from the user until an empty line is entered
    x, y = map(float, input().split())
    loop = True

    while loop:
        plist.append((x, y))

        try:
            x, y = map(float, input().split())
        except ValueError:
            loop = False

    # Check if there are at least two points
    if len(plist) == 1:
        print("There must be at least two points!\n Please try again.")
        Main_code()

    # Compute coefficients for the linear regression
    a11, a21, a12, a22, b1, b2 = 0, 0, 0, 0, 0, 0
    for point in plist:
        xi, yi = point[0], point[1]
        a11 += xi**2
        a21 += xi
        a12 = a21
        a22 += 1
        b1 += xi*yi
        b2 += yi

    # Solve the system of equations to get the regression coefficients
    Alpha_Vector = Solve_LS_2x2(a11, a21, a12, a22, b1, b2)
    alpha1, alpha2 = Alpha_Vector[0], Alpha_Vector[1]

    # Print the equation of the regression line
    if alpha2 > 0:
        print(f"y = {alpha1}x + {alpha2}")
    elif alpha2 < 0:
        print(f"y = {alpha1}x - {abs(alpha2)}")
    else:
        print(f"y = {alpha1}x")

run = True

print("""Welcome to LineCan v0.1!
Please type x and y values, separated by spacebar
When done, press return on an empty line.""")

while run:
    
    
    Main_code()

    finalinput = input("Type 1 to run the code again: ")

    if finalinput != "1":
        run = False
    else:
        print("-"*20)
