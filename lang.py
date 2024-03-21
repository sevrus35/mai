def lang():

  language = input("Enter your language: ")
  amount = int(input("Enter the number of times to greet: "))

  if language.lower() == 'english':
    greeting = 'hello'
  elif language.lower() == 'chinese':
    greeting = '你好'
  elif language.lower() == 'russian':
    greeting = 'привет'
  else:
    print("Language not supported")
    return  

  for _ in range(amount):
    print(greeting)

lang()