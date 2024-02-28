def main() -> None:
    greeting: str = formatGreeting(input('Type your greeting message: '))
    value: int = check_greeting_value(greeting)
    print(f'GHC {value}')


def check_greeting_value(greeting: str) -> int:
    if (greeting[:5] == 'hello'):
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100


def formatGreeting(s: str) -> str:
    return s.strip().lower()


main()
