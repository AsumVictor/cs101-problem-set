def main():
    fileName = getExt(input('Enter the file name here: '))
    print(getFileType(fileName))


def getFileType(ext):
    extension = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    return extension[ext] if ext in extension else 'application/octet-stream'


def getExt(s):
    return s.strip().split('.')[-1].lower()


main()

# .gif - image/gif
# .jpg - image/jpeg
# .jpeg - image/jpeg
# .png - image/png
# .pdf - application/pdf
# .txt - text/plain
# .zip - application/zip
