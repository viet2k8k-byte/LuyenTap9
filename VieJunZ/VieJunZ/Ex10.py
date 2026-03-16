class SinhVien:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

    def __eq__(self, other):
        if isinstance(other, SinhVien):
            return self.diem == other.diem
        return False

print("Vui lòng nhập thông tin cho sinh viên 1:")
ten1 = input("Tên: ")
diem1 = float(input("Điểm: "))
sv1 = SinhVien(ten1, diem1)

print("\nVui lòng nhập thông tin cho sinh viên 2:")
ten2 = input("Tên: ")
diem2 = float(input("Điểm: "))
sv2 = SinhVien(ten2, diem2)

print("\nKết quả so sánh")
if sv1 == sv2:
    print(f"Hai sinh viên {sv1.ten} và {sv2.ten} có điểm bằng nhau ({sv1.diem}).")
else:
    print(f"Hai sinh viên {sv1.ten} và {sv2.ten} có điểm không bằng nhau.")