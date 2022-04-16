#I tried something different 
#The teacher said there is always more than one way to do something so I tried a new code using Python and I think it worked
import bge
from bge import logic
path = logic.expandPath("//customers.text/")

cont = logic.getCurrentController()
own = cont.owner
keys = cont.sensors["Keyboard"]

var1 = 20
var2 = 60

def save():
  global var1
  global var2
  for key,status in keys.events:
    if status == logic.KK_INPUT_JUST_ACTIVATED:
       string = bge.events.EventToString(key)

       if string == "SKEY":
          info = str(var1)+","+str(var2)
          file = open(path+str(own)+".txt","w")
          file.write(str(info)) 

       if string == "LKEY":
          file = open(path+str(own)+".txt","r")
          line = file.readline().replace("\n","").split(",") 
          var1 = int(line[0])
          var2 = int(line[1])

       if string == "AKEY":
          var1 +=1
          var2 +=2
  own["prop"] = var1
  own["prop0"] = var2

from bge import logic
path = logic.expandPath("//customers.txt/")

cont = logic.getCurrentController()
own = cont.owner
keys = cont.sensors["Keyboard"]

for key,status in keys.events:
  if status == logic.KX_INPUT_JUST_ACTIVATED:
      string = bge.events.EventToString(key)
   
#Saving "prop" and "prop0" to customers.txt file
  if string == "SKEY":
       info = str(own["prop"])+","+str(own["prop0"])
       file = open(path+str(own)+".txt","w")
       file.write(str(info))

#Loading "prop" and "prop0" from the customers.txt file
  if string == "LKEY":
       file = open(path+str(own)+".txt", "r")
       line = file.readline().replace("\n","").split(",")
       own["prop"] = int(line[0])
       own["prop0"] = int(line[1])

#Changing the values
  if string == "AKEY":
       own["prop"]+=1
       own["prop0"]+=1.3 