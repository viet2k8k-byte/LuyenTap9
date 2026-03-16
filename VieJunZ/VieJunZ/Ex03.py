def chuan_hoa_ten(name):
    cac_tu = name.split()
    ten_tam_thoi = " ".join(cac_tu)
    ten_chuan_hoa = ten_tam_thoi.title()
    return ten_chuan_hoa
input_name = input("Nhập tên : ")
result = chuan_hoa_ten(input_name)
print(f"Trước: '{input_name}'")
print(f"Sau:  '{result}'")