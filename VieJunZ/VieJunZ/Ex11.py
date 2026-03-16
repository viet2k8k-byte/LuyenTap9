class SinhVien:
    so_luong = 0
    def __init__(self, ten):
        self.ten = ten
        SinhVien.so_luong += 1
    @classmethod
    def lay_so_luong(cls):
        return f"Tổng số sinh viên hiện có: {cls.so_luong}"

sv_a = SinhVien("Vie")
sv_b = SinhVien("JunZ")


print(SinhVien.lay_so_luong())