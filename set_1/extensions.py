def main() -> None:
    file = splitFileName(input('Enter the file name: '))
    print(extractFile(file))


def extractFile(ext: str) -> str:
    match_extension = {"gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"}
    return ext if ext.lower() in match_extension else 'application/octet-stream'


def splitFileName(fileName: str) -> str:
    return fileName.split('.')[-1]


main()
