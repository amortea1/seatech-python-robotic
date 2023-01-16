from abc import ABCMeta, abstractmethod

class UnmannedVehicule():

    _name="DEFAULT"
    
    """  An autonomous vehicle have to do his mission automatically.
    This mission can be configured by an operator. """
    @abstractmethod
    def do_something_interesting(self):
        """"chose"""
    def do_other_things(self):
        """autre chose"""""

class AerialVehicule():
    """ A vehicle made for ground fields."""
    def do_something_aerial_specific(self):
        print("AIR COMBAT initialisé")
    def do_other_things_aerial(self):
        print("protocole d'urgence ON ")

class GroundVehicule():
    """ A vehicle made for ground fields."""
    def do_something_ground_specific(self):
        print("GROUND COMBAT initialisé ")
    def do_other_ground(self):
        print("protocole arret voiture")

class UnderseaVehicule():
    """ A vehicle made for ground fields."""
    def do_something_undersea_specific(self):
        print("UNDERSEA COMBAT initilisé, mission : sauvez wally ")
    def do_something_things_undeesea(self):
        print("annuler la mission")

class UAV(UnmannedVehicule,AerialVehicule):
    """Unmanned Aerial Vehicule"""
    def do_something_interesting(self):
        print("depart vol")
    def do_other_things(self):
        print("mayday mayday")

class UUV(UnmannedVehicule,UnderseaVehicule):
    """Unmanned Undersea Vehicule"""
    def do_something_interesting(self):
        print("plonger")
    def do_other_things(self):
        print("fuite")

class UGV(UnmannedVehicule,GroundVehicule):
    """Unmanned Ground Vehicule"""
    def do_something_interesting(self):
        print("rouler")
    def do_other_things(self):
        print("arret d'urgence")


if __name__ =='__main__':
    uav = UAV()
    uav.do_something_interesting()
    uav.do_other_things()
    uav.do_other_things_aerial()
    uav.do_something_aerial_specific()
    ugv = UGV()
    ugv.do_something_interesting()
    ugv.do_other_things()
    ugv.do_something_ground_specific()
    ugv.do_other_ground()
    uuv = UUV()
    uuv.do_something_interesting()
    uuv.do_other_things()
    uuv.do_something_undersea_specific()
    uuv.do_something_things_undeesea()
