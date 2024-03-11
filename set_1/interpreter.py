def main() -> None:
    math_input: str = input(' Enter your Arithemetic: ')
    x, y, z = math_input.split(" ")
    print(calculate(int(x), y, int(z)))

def calculate(x: int, y: str, z: int) -> str:
    calculate_match = {
        '+': add(x, z),
        '-': substrate(x, z),
        '/': divide(x, z),
        '*': multiply(x, z)
    }
    
    return float(calculate_match[y])

def add(x: int, z: int) -> int:
    return x + z

def divide(x: int, z: int) -> int:
    return x / z

def multiply(x: int, z: int) -> int:
    return x * z

def substrate(x: int, z: int) -> int:
    return x - z


main()
