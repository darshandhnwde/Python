class Item:
    pay_rate = 0.8 # pay rate after the 20% discount 

    def __init__(self,product_name,price,quantity=0) -> None:
        # Run Validation For Recieved Arguments
        assert price >= 0 , F"price{price}is not greater than or equal to zero"
        assert quantity >=0 ,F"quantity{quantity}is not greater thsn or equal to zero"

        # Assign to self object
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def Calculate_total_price(self):
        return self.price * self.quantity
    
    def Pay_after_discount(self):
        return self.price * self.pay_rate
    
    def Products_details(self,):
        print("Product name :"+self.product_name)
        print("Initial price :"+ str(self.price))
        print("Price after discount :"+ str(self.Pay_after_discount()))
        print("The quantity of product :"+str(self.quantity))
        print("The total price all product :"+ str(self.Calculate_total_price()))
        
 
item1 = Item("Laptop",72256,1)
item2 = Item("Keyboard",1000,2)
item3 = Item("Mouse",300,1)
item4 = Item("Cable",200,4)
item5 = Item("USB Hub",1600,3)
#print(item1.Calculate_total_price())
#print(item1.Pay_after_discount())
print(item1.Products_details())
print(item2.Products_details())
print(item3.Products_details())
print(item4.Products_details())
print(item5.Products_details())
         