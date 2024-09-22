class Order():
    def __init__(self) -> None:
        self.items = []
        self.total = None

    def calculate_price(self, discount=0):
        self.total = sum([item.price * item.quantity for item in self.items])
        self.discount = self.total * (discount / 100)
        self.total -= self.discount

    def add_item(self, item):
        self.items.append(item)

    def print_bill(self):
        print("-----  Factura  -----")
        print("Item - Precio - Cantidad")
        for item in self.items:
            print(f"+ {item.name} - {item.price} - {item.quantity}")
        print("-------------------------")
        print("Descuento:", self.discount)
        print(f"Total: {self.total}")

class MenuItem():
    def __init__(self, price, name, quantity) -> None:
        self.price = price
        self.name = name
        self.quantity = quantity

class Beverage(MenuItem):
    def __init__(self, price, size, name, quantity) -> None:
        super().__init__(price, name, quantity)
        self.size = size

class Appetizer(MenuItem):
    def __init__(self, price, customers, name, quantity) -> None:
        super().__init__(price, name, quantity)
        self.customers = customers

class MainCourse(MenuItem):
    def __init__(self, price, grammage, name, quantity) -> None:
        super().__init__(price, name, quantity)
        self.grammage = grammage


# Clase para guardar elementos para crear un MenuItem, solo se crea hasta llamar al método get_item
class Item():
    def __init__(self, _class, *args) -> None:
        self._class = _class
        self.args = args
    def get_item(self, quantity):
        return self._class(*self.args, quantity)
    
    def __str__(self) -> str:
        return f"{self.args[2]} - ${self.args[0]}"


class OrderIterator(Order):
    main_course = [
        Item(MainCourse, 12000, 150, "Hamburguesa sencilla"),
        Item(MainCourse, 16000, 300, "Hamburguesa doble"),
        Item(MainCourse, 20000, 200, "Hamburguesa ranchera"),
        Item(MainCourse, 23000, 250, "Hamburguesa todo terreno")
    ]
    appetizer = [
        Item(Appetizer, 4000, 3, "Canasta de pan"),
        Item(Appetizer, 6000, 1, "Sopa"),
        Item(Appetizer, 8000, 5, "Papas fritas")
    ]
    beverage = [
        Item(Beverage, 2000, 500, "Agua"),
        Item(Beverage, 3000, 500, "Refresco"),
        Item(Beverage, 5000, 600, "Jugo")
    ]


    def __iter__(self):
        for product in OrderIterator.main_course:
            yield product
        for product in OrderIterator.appetizer:
            yield product
        for product in OrderIterator.beverage:
            yield product


    def mainloop(self):
        print("-----  Menú  -----")
        for product in self:
            print("Desea: ", product, "(s/n): ", end="")
            selection = input()
            if selection == "s":
                quantity = int(input("Cantidad: "))
                self.add_item(product.get_item(quantity))

        
        discount = 0
        selection = input("¿Tiene cupón de descuento? (s/n): ")
        if selection == "s":
            discount = int(input("Porcentaje de descuento: "))
        
        self.calculate_price(discount)
        self.print_bill()


    
    


order = OrderIterator()

order.mainloop()
print("Gracias por su compra, vuelva pronto")
