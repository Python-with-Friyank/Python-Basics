startCarCommand = 'START'
stopCarCommand = 'STOP'
QuitGameCommand = 'QUIT'
helpGameCommand = 'HELP'
userInput = input(">").upper()
while userInput != QuitGameCommand:
   if userInput == startCarCommand :
       print('Your Car is started, Drive Safe.')
   elif userInput == stopCarCommand :
       print('Your Car is stopped. Thank you.')
   elif userInput == helpGameCommand :
       print("Enter 'start' - To Start a car.")
       print("Enter 'Stop' - To Stop a car.")
       print("Enter 'Quit' - To Quit the Game.")
   else:
       print('Sorry, I don\'t understand that')
   userInput = input(">").upper()


for item in ['a','b','c','d']:
    print(item)