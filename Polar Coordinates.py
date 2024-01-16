import cmath

def polar_coordinates(complex_number):
    r, phi = cmath.polar(complex_number)
    return r, phi

if __name__ == "__main__":
    complex_number = complex(input())
    
    r, phi = polar_coordinates(complex_number)
    
    print(r)
    print(phi)
