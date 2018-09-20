source : https://github.com/MyRobotLab/pyrobotlab/blob/master/service/Adafruit16CServoDriverPi.py
# Nixie build
raspi = Runtime.createAndStart("RasPi","RasPi")
adaFruit16c = Runtime.start("AdaFruit16C","Adafruit16CServoDriver")
adaFruit16c.attach("RasPi","1","0x40")
Oeil = Runtime.createAndStart("Oeil", "Servo")
