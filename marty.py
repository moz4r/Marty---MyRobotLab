import random

raspi = Runtime.createAndStart("raspi","RasPi")
adaFruit16c = Runtime.start("adaFruit16C","Adafruit16CServoDriver")
adaFruit16c.attach(raspi,"1","0x40")

# config des servos

oeil = Runtime.createAndStart("oeil", "Servo")
brasDroit = Runtime.createAndStart("brasDroit", "Servo")
tibiaDroit = Runtime.createAndStart("tibiaDroit", "Servo")
genouDroit = Runtime.createAndStart("genouDroit", "Servo")
hancheDroit = Runtime.createAndStart("hancheDroit", "Servo")
brasGauche = Runtime.createAndStart("brasGauche", "Servo")
genouGauche = Runtime.createAndStart("genouGauche", "Servo")
tibiaGauche = Runtime.createAndStart("tibiaGauche", "Servo")
hancheGauche = Runtime.createAndStart("hancheGauche", "Servo")


oeil.attach(adaFruit16c,8)
brasDroit.attach(adaFruit16c,7)
tibiaDroit.attach(adaFruit16c,6)
genouDroit.attach(adaFruit16c,5)
hancheDroit.attach(adaFruit16c,4)
brasGauche.attach(adaFruit16c,3)
genouGauche.attach(adaFruit16c,2)
tibiaGauche.attach(adaFruit16c,1)
hancheGauche.attach(adaFruit16c,0)

brasDroit.setAutoDisable(True)
tibiaDroit.setAutoDisable(True)
genouDroit.setAutoDisable(True)
hancheDroit.setAutoDisable(True)
brasGauche.setAutoDisable(True)
genouGauche.setAutoDisable(True)
tibiaGauche.setAutoDisable(True)
hancheGauche.setAutoDisable(True)
oeil.setAutoDisable(True)

#Limites Regis
#oeil.map(0.0,180.0,0.0,125.0)
#brasDroit.map(0.0,180.0,0.0,180.0)
#tibiaDroit.map(0.0,180.0,90.0,180.0)
#hancheDroit.map(0.0,180.0,101.0,150.0)
#brasGauche.map(0.0,180.0,0.0,180.0)
#tibiaGauche.map(0.0,180.0,55.0,140.0)
#hancheGauche.map(0.0,180.0,60.0,155.0)

#Limites vincent
#oeil.map(0.0,180.0,0.0,125.0)
#brasDroit.map(0.0,180.0,0.0,180.0)
#tibiaDroit.map(0.0,180.0,90.0,180.0)
#hancheDroit.map(0.0,180.0,101.0,150.0)
#brasGauche.map(0.0,180.0,0.0,180.0)
#tibiaGauche.map(0.0,180.0,55.0,140.0)
#hancheGauche.map(0.0,180.0,60.0,155.0)



hancheDroit.setRest(90)
genouDroit.setRest(90)
tibiaDroit.setRest(80)
hancheGauche.setRest(97)
genouGauche.setRest(95)
tibiaGauche.setRest(90)
oeil.setRest(90)
oeil.map(0,180,66,100)
brasGauche.setRest(90)
brasDroit.setRest(120)


# vie aléatoire

MoveEyesTimer = Runtime.start("MoveEyesTimer","Clock")
MoveArmsTimer = Runtime.start("MoveArmsTimer","Clock")
MoveFootTimer = Runtime.start("MoveFootTimer","Clock")

def MoveEyes(timedata):
  #redefine next loop
  MoveEyesTimer.setInterval(random.randint(1000,5000))
  oeil.setVelocity(random.randint(10,110))
  #wait servo last move
  if not oeil.isMoving():oeil.moveTo(random.uniform(0,180))
    
def MoveEyesStop():  
  oeil.rest()
  
def MoveArms(timedata):
  #redefine next loop
  MoveEyesTimer.setInterval(random.randint(1000,10000))
  brasGauche.setVelocity(random.randint(10,110))
  brasDroit.setVelocity(random.randint(10,110))
  #wait servo last move
  if not brasGauche.isMoving():brasGauche.moveTo(random.uniform(0,180))
  if not brasDroit.isMoving():brasDroit.moveTo(random.uniform(0,180))
    
def MoveArmsStop():  
  brasGauche.rest()
  brasDroit.rest()
  
def MoveFoot(timedata):
  #redefine next loop
  MoveEyesTimer.setInterval(random.randint(1000,5000))
  velo=random.randint(10,30)
  tibiaDroit.setVelocity(velo)
  tibiaGauche.setVelocity(velo)
  
  #wait servo last move
  if not tibiaDroit.isMoving():
    pos=random.uniform(60,120)
    tibiaDroit.moveTo(pos)
    tibiaGauche.moveTo(pos)
    
def MoveFootStop():  
  tibiaDroit.rest()
  tibiaGauche.rest()
    
MoveEyesTimer.addListener("pulse", python.name, "MoveEyes")
MoveEyesTimer.addListener("clockStopped", python.name, "MoveEyesStop")

MoveArmsTimer.addListener("pulse", python.name, "MoveArms")
MoveArmsTimer.addListener("clockStopped", python.name, "MoveArmsStop")

MoveFootTimer.addListener("pulse", python.name, "MoveFoot")
MoveFootTimer.addListener("clockStopped", python.name, "MoveFootStop")

#MoveEyesTimer.startClock()
#MoveArmsTimer.startClock()
#MoveFootTimer.startClock()

runtime.setLogLevel("warn")
