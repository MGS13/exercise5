import time, os

gameRentals = []

def addRental():
  customer = input("Customer: ")
  item = input("Game: ")
  price = float(input("Price per night: "))
  nights = int(input("Nights: "))
  total = round(price*nights,2)
  returned = False

  #You'll probably want to start here

  print("Added successfully")
  time.sleep(1)

def viewRentals():
  print("RENTAL HISTORY")
  for row in gameRentals:
    for item in row:
      print(item, end="\t")
    print()
  time.sleep(1)

while(True):#lol emoji
  print("🎮 GAME RENTALS 🎮")
  print("   ===========")
  print("Press 1 to add new Rental")
  print("Press 2 to view Rentals")
  menuChoice = input("> ")

  if(menuChoice=="1"):
    addRental()
  elif(menuChoice=="2"):
    viewRentals()
  else:
    print("ERROR: Unknown Option")
    time.sleep(1)
  
  time.sleep(1)
  os.system('clear')

  
#HOW DO I SAVE THIS FILE WTF
#I DONT KNOW IM HAVING THE SAME PROBLEM