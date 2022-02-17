#Header: 
#Krrishiv Kohli
#AP Preformance Task
#2/8/22

#Creating code to import libraries 
import random
from graphics import *
from colorama import Fore, Style

#Function to print rules
def rules(): 
  #Can add more rules
  #Instructions on special cards such as +2 and +4 need to be added
  print("\nHere are some simple rules on how to play this game:")
  print("There is a deck of different colored cards with different numbers")
  print("Each player is given a hand of 7 cards and one card is choosen as the first card in play")
  print("The main objective of the game is to get rid of the cards in your hand as soon as possible")
  print("When your turn arrives you must place down a card of the same color or number as the current card in play")
  print("To place a card simply type the number next to the card ie: 1,2,3,4,...")
  print("If you do not hold such a card in your deck you must draw one card from a pile by pressing (d)")
  print("When you have one card left you must say UNO or you have to draw 3 cards from the pile")
  print("The person with no cards remaining wins!")

print("Welcome to UNO!")
#Call the function to print rules
rules()

readyPlay = input("\nAre you ready to play the game? (Yes to contine, No to see rules again): ")

if (readyPlay == "No" or readyPlay == "no"):
  rules()

print("\nWe will now play the game, if you are ever confused just press (r) to display the rules again")

#Creating lists for colors and numbers
color = ["Red", "Blue", "Green", "Yellow"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
special = [" +2", "+4", "WILD"]

#Actual code of game:
#Creating lists to store the users decks:
userDeckColor = []
userDeckNumber = []
cardColor = random.choice(color)

#creating boolean variable in case user wants to run again:
runAgain = True
runAgain2 = True
errorTrap = True

for i in range (7):
  colors = random.choice(color)
  #Creating a variable special for special cards such as +2, +4, Wild
  special2 = random.randint(0,12)

  #In case random integer is 0-9, appends normal number card
  if (special2 > 0 and special2 < 10):
    userDeckColor.append(colors)
    userDeckNumber.append(special2)

  #If random int returns 10 or above, a special card is appended such as +2, +4, etc...
  elif (special2 == 10):
    #Need to concatenate 
    userDeckColor.append(colors + " +")
    userDeckNumber.append(2)
  elif (special2 == 11):
    userDeckColor.append("Plus")
    userDeckNumber.append(4)
  elif (special2 == 12):
    #Appending space to userDeckNumber so that both lists have the same amount of items in them
    userDeckColor.append("WILD")
    userDeckNumber.append(" ")

#Creating a while loop so that function can keep on running until user as no more cards in hand
while (runAgain == True):
  #Making the first card in play random
  firstCardNumber = random.randint(0,9)
  firstCardColor = cardColor

  #Printing first card in play
  print("\nEveryone else has placed their cards and its your turn now!\nHere is the card in play: ")
  print((firstCardColor), (firstCardNumber))

  cardColor = random.choice(color)
  
  #If statement so program knows which card to print
  if (firstCardColor == "Red"):
    if (firstCardNumber == 0):
      print(Fore.RED + zero)
    elif (firstCardNumber == 1):
      print(Fore.RED + one)
    elif (firstCardNumber == 2):
      print(Fore.RED + two)
    elif (firstCardNumber == 3):
      print(Fore.RED + three)
    elif (firstCardNumber == 4):
      print(Fore.RED + four)
    elif (firstCardNumber == 5):
      print(Fore.RED + five)
    elif (firstCardNumber == 6):
      print(Fore.RED + six)
    elif (firstCardNumber == 7):
      print(Fore.RED + seven)
    elif (firstCardNumber == 8):
      print(Fore.RED + eight)
    elif (firstCardNumber == 9):
      print(Fore.RED + nine)

  elif (firstCardColor == "Blue"):
    if (firstCardNumber == 0):
      print(Fore.BLUE + zero)
    elif (firstCardNumber == 1):
      print(Fore.BLUE + one)
    elif (firstCardNumber == 2):
      print(Fore.BLUE + two)
    elif (firstCardNumber == 3):
      print(Fore.BLUE + three)
    elif (firstCardNumber == 4):
      print(Fore.BLUE + four)
    elif (firstCardNumber == 5):
      print(Fore.BLUE + five)
    elif (firstCardNumber == 6):
      print(Fore.BLUE + six)
    elif (firstCardNumber == 7):
      print(Fore.BLUE + seven)
    elif (firstCardNumber == 8):
      print(Fore.BLUE + eight)
    elif (firstCardNumber == 9):
      print(Fore.BLUE + nine)

  elif (firstCardColor == "Green"):
    if (firstCardNumber == 0):
      print(Fore.GREEN + zero)
    elif (firstCardNumber == 1):
      print(Fore.GREEN + one)
    elif (firstCardNumber == 2):
      print(Fore.GREEN + two)
    elif (firstCardNumber == 3):
      print(Fore.GREEN + three)
    elif (firstCardNumber == 4):
      print(Fore.GREEN + four)
    elif (firstCardNumber == 5):
      print(Fore.GREEN + five)
    elif (firstCardNumber == 6):
      print(Fore.GREEN + six)
    elif (firstCardNumber == 7):
      print(Fore.GREEN + seven)
    elif (firstCardNumber == 8):
      print(Fore.GREEN + eight)
    elif (firstCardNumber == 9):
      print(Fore.GREEN + nine)
    
  elif (firstCardColor == "Yellow"):
    if (firstCardNumber == 0):
      print(Fore.YELLOW + zero)
    elif (firstCardNumber == 1):
      print(Fore.YELLOW + one)
    elif (firstCardNumber == 2):
      print(Fore.YELLOW + two)
    elif (firstCardNumber == 3):
      print(Fore.YELLOW + three)
    elif (firstCardNumber == 4):
      print(Fore.YELLOW + four)
    elif (firstCardNumber == 5):
      print(Fore.YELLOW + five)
    elif (firstCardNumber == 6):
      print(Fore.YELLOW + six)
    elif (firstCardNumber == 7):
      print(Fore.YELLOW + seven)
    elif (firstCardNumber == 8):
      print(Fore.YELLOW + eight)
    elif (firstCardNumber == 9):
      print(Fore.YELLOW + nine)

  #Printing user deck:
  print(Style.RESET_ALL)
  print("Here is your hand: ")
  for k in range (len(userDeckColor)):
    print((k + 1),") ",userDeckColor[k], userDeckNumber[k])

  #Asks user to input on the their cards in deck
  card = input("\nRemember you can always press (r) to view the rules again or (d) to draw a card from the pile\nPlease choose a card to place down: ")

  #Function to check card in play and testing different scenarios 
  def cardInPlay(cardNumb, firstCardColor, firstCardNumber):
    card = cardNumb

    #If else statements to check the card user entered
    if (userDeckColor[card - 1] == firstCardColor or userDeckNumber[card - 1] == firstCardNumber):
      #Printing to user that they choose a correct card
      print("Success! You played a good card!")

      #Updating Card in play so that the game can continue like in real life
      firstCardColor = userDeckColor[card - 1]
      firstCardNumber = userDeckNumber[card - 1]
      #Removing the card in list so that the card is removed from the users hand
      userDeckColor.pop(card - 1)
      userDeckNumber.pop(card - 1)
    
    elif (userDeckColor[card - 1] == (firstCardColor + " +")):
      print("You played a plus 2! Now your friend is mad at you! Uh OH!")

      #Updating Card in play so that the game can continue like in real life
      firstCardColor = userDeckColor[card - 1]
      firstCardNumber = userDeckNumber[card - 1]
      #Removing the card in list so that the card is removed from the users hand
      userDeckColor.pop(card - 1)
      userDeckNumber.pop(card - 1)

    #If card user enters is a +4
    elif (userDeckColor[card - 1] == "Plus"):
      print("You played a plus 4! Now your friends are angry at you and want to target you Uh Oh!")
      
      #Asks user which color they want to play with now
      userChoice = input("What color would you wish to be played? ")

      #Create 4 different if/else statements for each color changing firstCardColor to the one which the user choose
      if (userChoice == "blue" or userChoice == "Blue"):
        #Updating Card in play so that the game can continue like in real life
        cardColor = [1]
        firstCardNumber = " "
        #Removing the card in list so that the card is removed from the users hand
        userDeckColor.pop(card - 1)
        userDeckNumber.pop(card - 1)

      elif (userChoice == "red" or userChoice == "Red"):
        #Updating Card in play so that the game can continue like in real life
        cardColor = color[0]
        firstCardNumber = " "
        #Removing the card in list so that the card is removed from the users hand
        userDeckColor.pop(card - 1)
        userDeckNumber.pop(card - 1)

      elif (userChoice == "green" or userChoice == "Green"):
        #Updating Card in play so that the game can continue like in real life
        cardColor = color[2]
        firstCardNumber = " "
        #Removing the card in list so that the card is removed from the users hand
        userDeckColor.pop(card - 1)
        userDeckNumber.pop(card - 1)

      elif (userChoice == "yellow" or userChoice == "Yellow"):
        #Updating Card in play so that the game can continue like in real life
        cardColor = color[3]
        firstCardNumber = " "
        #Removing the card in list so that the card is removed from the users hand
        userDeckColor.pop(card - 1)
        userDeckNumber.pop(card - 1)

    #If user enters a WILD card
    elif (userDeckColor[card - 1] == "WILD"):
      print("You played a WILD Card! You can choose the color of the cards played now!")

      #Asks user which color they want to play with now
      userChoice = input("What color would you wish to be played? ")

      #Create 4 different if/else statements for each color changing firstCardColor to the one which the user choose
      if (userChoice == "blue" or userChoice == "Blue"):
        #Updating Card in play so that the game can continue like in real life
        cardColor = "Blue"
        firstCardNumber = " "
        #Removing the card in list so that the card is removed from the users hand
        userDeckColor.pop(card - 1)
        userDeckNumber.pop(card - 1)

      elif (userChoice == "red" or userChoice == "Red"):
        #Updating Card in play so that the game can continue like in real life
        cardColor = "Red"
        firstCardNumber = " "
        #Removing the card in list so that the card is removed from the users hand
        userDeckColor.pop(card - 1)
        userDeckNumber.pop(card - 1)

      elif (userChoice == "green" or userChoice == "Green"):
        #Updating Card in play so that the game can continue like in real life
        cardColor = "Green"
        firstCardNumber = " "
        #Removing the card in list so that the card is removed from the users hand
        userDeckColor.pop(card - 1)
        userDeckNumber.pop(card - 1)

      elif (userChoice == "yellow" or userChoice == "Yellow"):
        #Updating Card in play so that the game can continue like in real life
        cardColor = "Yellow"
        firstCardNumber = " "
        #Removing the card in list so that the card is removed from the users hand
        userDeckColor.pop(card - 1)
        userDeckNumber.pop(card - 1)

    else:
      #If the card user enters does not meet any of thr requirments of a valid card
      print("This card can not be played as it does not have the same color or number as the card in play. Your turn is skipped :(")

  #If statements for all values that the user can enter 
  if (card == "1"):
    #ALl parameters needed for function
    cardInPlay(1, firstCardColor, firstCardNumber)
  elif (card == "2"):
    cardInPlay(2, firstCardColor, firstCardNumber)
  elif (card == "3"):
    cardInPlay(3, firstCardColor, firstCardNumber)
  elif (card == "4"):
    cardInPlay(4, firstCardColor, firstCardNumber)
  elif (card == "5"):
    cardInPlay(5, firstCardColor, firstCardNumber)
  elif (card == "6"):
    cardInPlay(6, firstCardColor, firstCardNumber)
  elif (card == "7"):
    cardInPlay(7, firstCardColor, firstCardNumber)
  elif (card == "8"):
    cardInPlay(8, firstCardColor, firstCardNumber)
  elif (card == "9"):
    cardInPlay(9, firstCardColor, firstCardNumber)
  elif (card == "10"):
    cardInPlay(10, firstCardColor, firstCardNumber)
  elif (card == "r"):
    rules()
  elif (card == "d"):
    colors = random.choice(color)
    #Creating a variable special for special cards such as +2, +4, Wild
    special2 = random.randint(0,12)

    #In case random integer is 0-9, appends normal number card
    if (special2 > 0 and special2 < 10):
      userDeckColor.append(colors)
      userDeckNumber.append(special2)

    #If random int returns 10 or above, a special card is appended such as +2, +4, etc...
    elif (special2 == 10):
    #Need to concatenate 
      userDeckColor.append(colors + " +")
      userDeckNumber.append(2)
    elif (special2 == 11):
      userDeckColor.append("Plus")
      userDeckNumber.append(4)
    elif (special2 == 12):
      #Appending space to userDeckNumber so that both lists have the same amount of items in them
      userDeckColor.append("WILD")
      userDeckNumber.append(" ")
  
  computer = random.randint(0,9)

  #Checking is users deck array is empty or not so that program knows when to end loop
  if (len(userDeckColor) == 0 or len(userDeckNumber) == 0):
    print("Nice! Your deck is empty")
    #Printing a message to user if game when finished
    print("Congratulations! You win the game!")
    runAgain = False

  elif (len(userDeckColor) > 9 or len(userDeckNumber) > 9):
    print("\nUh oh! Your deck is too big\nYou lose, but dont worry you can do it next time!")
    runAgain = False
  
  elif (len(userDeckColor) == 1 or len(userDeckNumber) == 1):
    uno = input("\nQuick!\nType UNO and hit enter or else you will have to draw three cards!: ")

    if (uno == "UNO" or uno == "Uno" or uno == "uno"):
      print("\nNice! Your safe!")
      runAgain = True
    else:
      print("Uh Oh! Your friend shouted uno and now you have to draw three cards")
      for i in range(3):
        userDeckColor.append(random.choice(color))
        userDeckNumber.append(random.randint(0,9))
  
  elif (computer == 7):
    print("Uh OH! Your friend places a plus 4 on you! Now you have to draw 4 cards.")
    for i in range(4):
        userDeckColor.append(random.choice(color))
        userDeckNumber.append(random.randint(0,9))
  else:
    #If there is a item in User Deck then the loop will run again 
    runAgain = True