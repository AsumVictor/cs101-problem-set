def main():
    video = input('Enter any sentence:  ')
    print(reduceSpeed(video))

def reduceSpeed(s):
    return s.replace(' ','...')


main()

# Accept a user input
# Replace every ' ' with '...'
# return the results