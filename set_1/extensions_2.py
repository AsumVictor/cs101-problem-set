def main():
    fileName = (input('Enter the file name here: ')).strip().lower()
    
# .gif - image/gif
# .jpg - image/jpeg
# .jpeg - image/jpeg
# .png - image/png
# .pdf - application/pdf
# .txt - text/plain
# .zip - application/zip
    if fileName.endswith('.gif'):
        print('image/gif')
    elif fileName.endswith('.jpg'):
        print('image/jpg')
    elif fileName.endswith('.jpeg'):
        print('image/jpeg')
    elif fileName.endswith('.png'):
        print('image/png')
    elif fileName.endswith('.text'):
        print('text/plain')
    elif fileName.endswith('.pdf'):
        print('application/pdf')
    elif fileName.endswith('.zip'):
        print('application/gif')
    else:
        print('application/octet-stream')
    
    
  


main()

