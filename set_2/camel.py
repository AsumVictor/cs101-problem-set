def main():
    camel_input = input('Enter your camel case here:  ')
    snake_case = toSnakeCase(camel_input)
    print(snake_case)


def toSnakeCase(camel):
    result = ''
    for i in camel:
        if i.upper() == i:
            result += '_'
            result += i.lower()
        else:
            result += i.lower()

    return result


main()
