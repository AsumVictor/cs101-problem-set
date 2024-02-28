def main():
  
  answer = print('''What is the Great Question of Life, the Universe and Everything:  ''')
  
  print(checkAnswer(answer))

def checkAnswer(s):
    s = s.lower()
    match s:
      case '42' | 'forty two' | 'forty-two':
        return 'Yes'
      case _ :
        return 'No'
     

  
main()
