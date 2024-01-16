import math

def find_angle(ab, bc):
    ac = math.sqrt(ab**2 + bc**2)
    theta = round(math.degrees(math.asin(ab/ac)))
    return theta

if __name__ == "__main__":
    ab = int(input())
    bc = int(input())

    theta = find_angle(ab, bc)
    print(f"{theta}\u00b0")
