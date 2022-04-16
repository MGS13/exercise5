#I'VE MADE A MISTAKE
import os, time
#empty list/array
phoneSales=[]
try:
  f = open("crustomers.txt", "r")
  phoneSales = eval(f.readline())
  f.close()
except:
  pass
#Function will initialize 4 variables from input and store them in a row array which will then be appended to phoneSales
def order():
  item=input("Item: ")
  price=float(input("Price: "))1
  num_phones=int(input("How many? "))
  total= round(price*num_phones, 2)

  row=[item, price, num_phones, total]
  phoneSales.append(row)

  print("Order added")
  time.sleep(3)

def promptSales():
  print("SALES HISTORY")
  for row in phoneSales:
    for item in row:
      print(item, end="\t")
    print()
  time.sleep(3)

while(True):
  print("PHONE SALES")
  print("===========")
  print("Press 1 to add new Sale")
  print("Press 2 to view Sales")
  menuChoice = input("> ")

  if(menuChoice=="1"):
    order()
  elif(menuChoice=="2"):
    promptSales()
  else:
    print("ERROR: Unknown Option")
    time.sleep(3)
  
  time.sleep(3)
  os.system('clear')
  
  f = open("crustomers.txt", "w")
  f.write(str(phoneSales))
  f.close()