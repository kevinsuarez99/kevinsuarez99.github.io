#Item class

class Item:#marks the biginning of the class

    def __init__(self, price, weightInOunces, description):#the initial function that takes 3 parameters
        self.price = price#each of the parameters
        self.weightInOunces = weightInOunces
        self.description = description
        self.quantity = 1#in this case the quantity will be set to 1 as default

    def getOrderPrice(self):#determines the price of the oder
        oPrice = self.quantity * self.price#it takes the quantity and the price parameters
        return oPrice

    def getOrderWeightInOunces(self):#determines the weight of the order
        wghtOz = self.weightInOunces * self.quantity#takes the weight and the quantity parameters
        return wghtOz

    def set_quantity(self, qtt):#sets the quantity
        self.quantity = qtt#the quantity can be changed to any value qtt

    def __str__(self):#the final string function that prints out everything as a string
        outItemStr = ""
        outItemStr += "The price of the item is " + "$" + str(self.price) + "\n" #the price of the item 
        outItemStr += "The quantity of the item is " + str(self.quantity) + "\n" #the quantity of the item
        outItemStr += "The description of the item is " + str(self.description) + "\n" #the description of the item
        return outItemStr
    

    
