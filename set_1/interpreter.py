def main() -> None:
    math_input: str = input(' Enter your Arithemetic: ')
    x, y, z = math_input.split(' ')
    print(calculate(int(x), y, int(z)))


def calculate(x: int, y: str, z: int) -> str:
    math_bank: dict[str, function] = {
        '+': add(x, z),
        '-': substrate(x, z),
        '/': divide(x, z),
        '*': multiply(x, z)
    }
    return round(float(math_bank[y]), 1)


def add(x: int, z: int) -> int:
    return x + z


def divide(x: int, z: int) -> int:
    return x / z


def multiply(x: int, z: int) -> int:
    return x * z


def substrate(x: int, z: int) -> int:
    return x - z


main()
