def main() -> None:
    math_input: str = input(' Enter your Arithemetic: ')
    x, y, z = math_input.split(" ")
    print(calculate(float(x), y, float(z)))

def calculate(x: int, y: str, z: int) -> str:
    calculate_match = {
        '+': add(x, z),
        '-': substrate(x, z),
        '/': divide(x, z),
        '*': multiply(x, z)
    }
    result = round(calculate_match[y], 1)
    return result

def add(x: int, z: int) -> int:
    return x + z

def divide(x: int, z: int) -> int:
    return x / z

def multiply(x: int, z: int) -> int:
    return x * z

def substrate(x: int, z: int) -> int:
    return x - z


main()
