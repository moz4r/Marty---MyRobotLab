raspi = Runtime.createAndStart("raspi","RasPi")
adaFruit16c = Runtime.start("adaFruit16C","Adafruit16CServoDriver")
adaFruit16c.attach(raspi,"1","0x40")

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