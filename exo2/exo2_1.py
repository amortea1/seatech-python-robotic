from exo1 import Robot

class Human():   
    __manger = []
    def __init__(self,sexe) -> None:
        self.__sexe = sexe

    def eat(self,food):
        if type(food) is str: 
            self.__manger.append(food)
        elif type(food) is list:
            self.__manger += food
        print("j'ai mangé': " + str(self.__manger))

    def digest(self):
        self.__manger.clear()

    pass

    

class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):   
        Robot.__init__(self, name)
        Human.__init__(self, sexe)
        self.name = name
        self.sexe=sexe

if __name__ =='__main__':
    cyborg = Cyborg('Deux Ex Machina', 'M')

print(cyborg.name, 'sexe', cyborg.sexe)
print('Charging battery...')
cyborg.chargeBattery()
cyborg.getEtat()
cyborg.eat('banana')
cyborg.eat(['coca', 'chips'])
cyborg.digest()