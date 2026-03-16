#Bài 1 :
can_nang = float(input("Vui lòng nhập cân nặng của bạn : "))
chieu_cao = float(input("Vui lòng nhập chiều cao của bạn : "))
bmi = can_nang / (chieu_cao*chieu_cao)
print(f"Chỉ số cân nặng ( BMI ) của bạn là :  {bmi:.2f}")



#Bài 2 :
n = input("Nhập một số bất kỳ: ")
total = 0
for ch in n:
    if ch.isdigit():
        total += int(ch)
print(f"Tổng các chữ số là : {total}")




#Bài 3 :
def chuan_hoa_ten(name):
    cac_tu = name.split()
    ten_tam_thoi = " ".join(cac_tu)
    ten_chuan_hoa = ten_tam_thoi.title()
    return ten_chuan_hoa
input_name = input("Nhập tên : ")
result = chuan_hoa_ten(input_name)
print(f"Trước: '{input_name}'")
print(f"Sau:  '{result}'")




#Bài 4:
s = input("Nhập chuỗi: ")

hoa = 0
thuong = 0
so = 0
dac_biet = 0
khoang_trang = 0
nguyen_am = 0
phu_am = 0

nguyen_am_ds = "aeiouAEIOU"

for ch in s:
    if ch.isupper():
        hoa += 1
    elif ch.islower():
        thuong += 1

    if ch.isdigit():
        so += 1
    elif ch == " ":
        khoang_trang += 1
    elif not ch.isalpha() and not ch.isdigit():
        dac_biet += 1

    if ch.isalpha():
        if ch in nguyen_am_ds:
            nguyen_am += 1
        else:
            phu_am += 1

print(f"Chữ hoa: {hoa}")
print(f"Chữ thường: {thuong}")
print(f"Chữ số: {so}")
print(f"Ký tự đặc biệt: {dac_biet}")
print(f"Khoảng trắng: {khoang_trang}")
print(f"Nguyên âm: {nguyen_am}")
print(f"Phụ âm: {phu_am}")



#Bài 5 :
class User:
    def __init__(self, id):
        self._id = id
    @property
    def id(self):
        return self._id
u = User(101)
print(f"User id: {u.id}")



#Bài 6 :
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




#Bài 7 :
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, s):
        name, age = s.split("-")
        return cls(name, int(age))

    def __str__(self):
        return f"Tên: {self.name}, Tuổi: {self.age}"
p = Person.from_string("Nam-20")
print(p)




#Bài 8 :
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Kết quả cộng (v1 + v2): {v3}")




#Bài 9 :
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Cũng tùy loài mà kêu...")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f"{self.name} kêu: Gâu Gâu!")

my_dog = Dog("Lulu")
my_dog.sound()
