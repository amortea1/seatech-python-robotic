from time import sleep

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutdown', 'running']

    def __init__(self, name):
        self.__name = name
        # self.currentState = input("Robot allumer ou etteint ?")

    def set_power(self,state):
        if state=="ON":
            self.__power=True
        elif state=="OFF":
            self.__power=False
            self.__current_speed=0

    def chargeBattery(self):
        print(self.__name + " is charging ...")
        for i in range(101):
            sleep(0.1)
            self.__battery_level = i
            print(self.__name + " is charged at " + str(self.__battery_level) + " %")
        print(self.__name + " has been fully charged")

    def setCurrentSpeed(self, speed):
        if self.__power==True:
            self.__current_speed = speed
            #input("Vitesse souhaiter ? \n")
            print(self.__name + " has been set to " + str(self.__current_speed) + " mm/s")


    def getCurrentSpeed(self):
        return self.__current_speed

    def stop(self):
        if self.__power == True:
            if input("voulez vous vous areter? si oui ecrit stop \n") == "stop":
                self.__current_speed = 0

                print("arret reussi, vitesse actuel  ",r1.getCurrentSpeed(), "km/h \n\n")

    def getPower(self):
        print("Etat power : " + str(self.__power))

    def getEtat(self):
        print("\nEtat génerale du systeme\n")
        print("Nom du robot :" + self.__name)
        print("Etat power : " + str(self.__power))
        print("la batterie est a "+str(self.__battery_level)+"%")
        print("speed is "+ str(self.__current_speed))

if __name__=="__main__":
    
    r1 = Robot('Ahmed');
    r1.chargeBattery()
    r1.set_power(input("ON OU OFF\n"))
    r1.getPower()
    r1.set_power("ON")
    r1.getPower()
    r1.setCurrentSpeed(input("vitesse souhaiter "))
    r1.stop()
    r1.getEtat()

