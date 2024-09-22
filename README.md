# Reto 7 Dilan Porras


Para este reto se agregó la clase OrderIterator que hereda de Order, su principal objetivo es proporcionar los productos del menú usando un generador, las demás funciones se dejan intactas de la clase padre, Order.
````mermaid
classDiagram
    Order <|-- OrderIterator
    Order *-- MenuItem
    OrderIterator *-- Item

    MenuItem <|-- MainCourse
    MenuItem <|-- Appetizer
    MenuItem <|-- Beverage





    class Order{
        + items: list[MenuItem]
        + total: int
        + calculate_price(discount)
        + add_item(item)
        + print_bill()
    }

    class MenuItem{
        + price: int
        + name: str
        + quantity: int
    }

    class MainCourse{
        + grammage: int
    }
    class Appetizer{
        + customers: int
    }
    class Beverage{
        + size: int
    }

    class Item{
        + _class
        + args: list
        + get_item(quantity)
    }

    class OrderIterator{
        + main_course: list
        + appetizer: list
        + Beverage: list
        + __iter__()
        + mainloop()
    }
````

### OrderIterator
````python
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
````

Primero se crean los productos que se van a mostrar, estos se guardan como variables de clase por lo que solo se guardan una vez en todo el programa.
Para disminuir el consumo de memoria se crea una clase Item que guarda los argumentos necesarios para crear cada tipo de producto, **no instancia el producto**.

````python
class Item():
    def __init__(self, _class, *args) -> None:
        self._class = _class
        self.args = args
    def get_item(self, quantity):
        return self._class(*self.args, quantity)
    
    def __str__(self) -> str:
        return f"{self.args[2]} - ${self.args[0]}"

````
Cuando se decida obtener la instancia del producto se llama a get_item junto con la cantidad

### Generador en OrderIterator
````python
# Dentro de la clase OrderIterator
    def __iter__(self):
        for product in OrderIterator.main_course:
            yield product
        for product in OrderIterator.appetizer:
            yield product
        for product in OrderIterator.beverage:
            yield product
````
Al usar una instancia de OrderInterator como un iterador este retorna un generador que dará cada Item de uno en uno. En caso de no usar un generador se retorna la lista completa lo cual resulta inecesario porque esta lista ya se encuentra guardada como variable de clase, no hace falta crear otra referencia a esta.

### Uso del generador
````python
# Dentro de la clase OrderIterator
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
````

Se crea un método mainloop que recorre los productos usando el generador de la misma clase con ```for product in self``` luego usando cada ```product``` que retorna el generador se crean o no los items que el usuario elija, al finalizar el bucle se continua con la ejecución del código usando las funciones heredadas de ```Order```.