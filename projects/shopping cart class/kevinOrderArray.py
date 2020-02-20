#second main file
#file that takes the Item class and creates a list of items
#and then uses a for loop to determine the dTotalPrice and iTotalWeight

import Item

def main():#2nd main that prints the same as the given main but instead uses a for loop

    dTotalPrice = 0.0#initial total price of the order      
    iTotalWeight = 0#initial total weight of the whole order

    #all the items and their descriptions
    item1 = Item.Item(24.99, 14, "Wireless Mouse")         
    item2 = Item.Item(22.49, 27, "USB Keyboard")         
    item3 = Item.Item(24.99, 12, "HDMI Cable")         
    item4 = Item.Item(7.99, 7, "Reading Glasses")         
    item4.set_quantity(2)

    itemLst = []#empty list created to add all the items into it

    #all the iems getting appended to the empty list
    itemLst.append(item1)
    itemLst.append(item2)
    itemLst.append(item3)
    itemLst.append(item4)

    for i in itemLst:#for loop used to print the descriptions for each item as well as to calculate the total order price and weight
        print(i)#prints each item's description
        dTotalPrice += i.getOrderPrice()#adds the prices of each item to calculate the total item price
        iTotalWeight += i.getOrderWeightInOunces()#adds the weight of each item to calculate the total weight of the order

    #prints the total value of the order price and weight
    print("The price of your order is $" + str(dTotalPrice));       
    print("The shipping weight is", (int)(iTotalWeight / 16),
          "pounds", iTotalWeight % 16 , "ounces") 
    

    

main()
    
