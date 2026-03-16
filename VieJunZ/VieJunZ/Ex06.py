class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Giá phải > 0!")
            self._price = 0

    def __str__(self):
        return f"Price: {self._price}"
try:
    user_price = float(input("Nhập giá sản phẩm: "))
    p = Product(user_price)
    print(p)
except:
    print("Vui lòng nhập số!")
