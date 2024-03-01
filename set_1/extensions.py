def main():
    fileName = getExt(input('Enter the file name here: '))
    print(getFileType(fileName))


def getFileType(ext):
    extensions = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    return extensions[ext] if ext in extensions else 'application/octet-stream'


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
