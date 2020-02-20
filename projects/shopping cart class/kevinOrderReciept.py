
import Item

def main():
    dTotalPrice = 0.0         
    iTotalWeight = 0
    # Put the 4 items being ordered in item1 through item 4         
    item1 = Item.Item(24.99, 14, "Wireless Mouse")         
    item2 = Item.Item(22.49, 27, "USB Keyboard")         
    item3 = Item.Item(24.99, 12, "HDMI Cable")         
    item4 = Item.Item(7.99, 7, "Reading Glasses")         
    item4.set_quantity(2);   
		
    # Show the details of the order using show()         
    print("Here are your shopping cart contents.")         
    print(item1);         
    print(item2);        
    print(item3);         
    print(item4); 
		
    # Compute the total price and total weight in this section        
    dTotalPrice += item1.getOrderPrice()         
    dTotalPrice += item2.getOrderPrice()         
    dTotalPrice += item3.getOrderPrice()         
    dTotalPrice += item4.getOrderPrice()         
    iTotalWeight += item1.getOrderWeightInOunces()        
    iTotalWeight += item2.getOrderWeightInOunces()         
    iTotalWeight += item3.getOrderWeightInOunces()         
    iTotalWeight += item4.getOrderWeightInOunces()         
    # Here we show the order details        
    print("The price of your order is $" + str(dTotalPrice));         
    print("The shipping weight is", (int)(iTotalWeight / 16),
          "pounds", iTotalWeight % 16 , "ounces");     

    
main()
