# Solving Quadratic Equation
coeffs = int(input("Enter co-efficient of x^2 : ")), int(input("Enter co-efficient of x : ")), int(input("Enter constant : "))
D = ( coeffs[1] ** 2 ) - ( 4 * coeffs[0] * coeffs[2] )
if (D < 0):
    print("No Real Roots Possible!")
elif (D > 0):
    print(f'''First Root : {
        ( (-coeffs[1]) - ( D ** 0.5 ) ) / ( 2 * coeffs[0] )
    }\n Second Root : {
        ( (-coeffs[1]) + ( D ** 0.5 ) ) / ( 2 * coeffs[0] )
    }''')
else:
    print(f'''Root : {
        (-coeffs[1]) / ( 2 * coeffs[0] )
    }''')