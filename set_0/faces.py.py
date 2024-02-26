def main():
  
  # Acccept input from user
  emoticon = input('Enter the emoticon: ')
  # Convert input to emoticon and print
  print(ConvertEmoticon(emoticon))
  
# Define a function as accept a string as argument
def ConvertEmoticon(s):
    # replace all ':)' with '😊' and all ':(' with '😔'
    # return the results
    return s.replace(':)', '😊').replace(':(', '😔')
  
  
main()
