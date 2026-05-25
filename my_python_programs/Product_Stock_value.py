class Product:
    def __init__(self):
        pass
        
    def total_stock_value(self):
        return self.p_price * self.p_quantity
    
    def show_data(self):
        print(f"Product : {self.p_name} \t with Price : {self.p_price} \t has Quantity : {self.p_quantity}")
        
    def get_data(self,p_name, p_price, p_quantity):
        self.p_name=p_name
        self.p_price=p_price
        self.p_quantity=p_quantity

p=Product()
p.get_data("Cycle",2000, 15)
p.show_data() 
print(f"Total Stock Value is : {p.total_stock_value()}")
        
